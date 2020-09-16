import _pickle
import os
import pickle
import re
import time
from datetime import date
from decimal import Decimal
from typing import Any, List
from PyQt5 import QtCore, QtWidgets, QtGui
import my_form


# метод для заставки
def load_data(sp):
    for i in range(1, 6):  # Имитируем процесс
        time.sleep(1)  # Что-то загружаем
        sp.showMessage("Загрузка данных... {0}%".format(i * 20), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom,
                       QtCore.Qt.yellow)  # надпись внизу картинки якобы считает ппроценты загрузки
        QtWidgets.qApp.processEvents()  # Запускаем оборот цикла


# отккрывает файл для дальнейшего использования
def load_data_file(a):
    f = open('save_dates/' + a, 'rb')  # открываем файл
    b = pickle.load(f)  # загружаем файл в словарь
    f.close()  # закрываем файл
    return b  # возвращает объект загруженный из файла


# сохраняет данные в файл
def save_data_files(a, b):
    f = open('save_dates/' + a, 'wb')  # открывает файл
    pickle.dump(b, f)  # записывает данные в файл
    f.close()  # закрывает файл


# создаёт инфориационное сообщение
def create_dialog_message(a, b, c):
    QtWidgets.QMessageBox.information(a, b, c, defaultButton=QtWidgets.QMessageBox.Ok)


# возвращает список файлов месяцев рабочих смен
def name_month_list(a: str):
    names_files_list = os.listdir(a)  # возвращает список всех файлов в в папке
    name_file = []  # список для файлов месяцев
    for i in range(len(names_files_list)):  # перебирает список всех файлов
        if re.search('\d+', names_files_list[i]) is not None:  # если в названии файла есть цифры
            name_file.append(names_files_list[i][:-4])  # имя файла добавляется в список
    name_file.sort()  # сортируем список
    return name_file  # возвращает список файлов месяцев


# расчитываем выплаты и долг и заполняем comboBox_selectMonth
def calculation_debt(debt, salary, pay, comboBox):
    name_month = name_month_list('save_dates')  # получаем названия файлов месяцев
    salary_list = []  # лист для заработанных денег
    payOut_list = []  # лист для полученных денег
    for i in range(len(name_month)):  # цикл для перебора файлов месяцев
        dateMonth = load_data_file(name_month[i] + '.txt')  # поочерёдно загружает файлы месяцев
        key_dateMonth: str  # названия смен в месяце они же ключи словаря
        for key_dateMonth in dateMonth.keys():  # цикл для перебора смен по ключам
            salary_list.append(Decimal(dateMonth[key_dateMonth][8]))  # заполняем лист заработка
            payOut_list.append(Decimal(dateMonth[key_dateMonth][9]))  # заполняем лист с полученными
        f_salary = Decimal(sum(salary_list))  # общий заработок
        payOut = Decimal(sum(payOut_list))  # общая получка
        debt.setText(str(f_salary - payOut))  # заполняем QLabel данными о долге
        salary.setText(str(f_salary))  # # заполняем QLabel данными о заработке
        pay.setText(str(payOut))  # # заполняем QLabel данными о выплатах
    comboBox.clear()  # очищаем comboBox
    comboBox.addItems(name_month)  # заполняем comboBox актуальным списком месяцев


def filling_table_settingTariff(dictTariff: dict, stItModel: QtGui.QStandardItemModel):
    tariff_keys = list(dictTariff.keys())  # список для ключей
    tariff_list: List[Any] = list(dictTariff.values())  # список для настроек тарифов
    for row in range(len(dictTariff)):  # цикл для заполнения таблицы по строкам
        if type(tariff_list[row]) == list:  # если строка является списком
            percent_list = ''  # лист для процентов если список
            percent_list_final = ''  # общий лист для процентов
            for j in range(len(tariff_list[row])):  #
                percent = str(Decimal(tariff_list[row][j] * Decimal('100')).quantize(Decimal('1.00')))[:-3]  #
                percent_list += percent + ' / '  #
                percent_list_final = percent_list[:-2]  #
            item_l0 = QtGui.QStandardItem(str(tariff_keys[row]))  #
            item_l1 = QtGui.QStandardItem(percent_list_final)  #
            stItModel.setItem(row, 0, item_l0)  #
            stItModel.setItem(row, 1, item_l1)  #
        else:
            item_0 = QtGui.QStandardItem(str(tariff_keys[row]))  # модель для заполнения первой колонки
            item_1 = QtGui.QStandardItem(str(Decimal(tariff_list[row] * 100).quantize(Decimal('1.00')))[:-3])
            # модель для заполнения второй колонки

            stItModel.setItem(row, 0, item_0)  # заполняем первую колонки
            stItModel.setItem(row, 1, item_1)  # заполняем вторую колонку


def filling_table_shifts(month: str, stItModel: QtGui.QStandardItemModel):
    try:
        dictMonth = load_data_file(month + '.txt')  #
    except(FileNotFoundError, EOFError):  #
        # диалоговое окно с информацией о отсутствии смен в текущем месяце
        create_dialog_message(splash, 'Нет смен в выбраном месяце.', 'Попробуйте выбрать другой месяц.')
        # если файл существует то заполняем таблицу смен
    except _pickle.UnpicklingError:  #
        create_dialog_message(splash, 'Файл повреждён!!!', 'Требуется восстановление файла')
    else:  #
        index = QtCore.QModelIndex()  # просто индекс
        stItModel.removeColumns(0, stItModel.columnCount(index), parent=index)  #
        shiftsNameList = list(dictMonth.keys())  # список названий смен
        stItModel.setHorizontalHeaderLabels(shiftsNameList)
        date_list = []  # список для временного хранения данных по сменам
        for key_dateMonth in dictMonth.keys():  # цикл для заполнения списка данных по сменам
            date_list.append(dictMonth[key_dateMonth])  # заполняем список с данными по сменам
        for j in range(stItModel.columnCount(index)):  # цикл по колонкам
            for row in range(stItModel.rowCount(index)):  # цикл по строкам
                stItModel.setItem(row, j, QtGui.QStandardItem(date_list[j][row]))  # заполнение таблицы
                # данными по сменам


class MyWindow(QtWidgets.QMainWindow, my_form.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # действия для таблицы смен
        self.action_addShift = QtWidgets.QAction('Добавить смену')  # действие для создания смены в таблице
        self.action_removeShift = QtWidgets.QAction('Удалить смену')  # действие для удаления смены
        self.action_addMonth = QtWidgets.QAction('Добавить месяц')  # действие для добавления месяца
        self.action_removeMonth = QtWidgets.QAction('Удалить месяц')  # действие для удаления месяца
        self.action_calculationShift = QtWidgets.QAction('Расчитать смену')  # действие для расчёта смены
        self.action_saveData = QtWidgets.QAction('Сохранить данные')  # действие для сохраненя данных

        # подключаем действия к таблице
        self.tableView_shifts.addAction(self.action_addShift)
        self.tableView_shifts.addAction(self.action_removeShift)
        self.tableView_shifts.addAction(self.action_addMonth)
        self.tableView_shifts.addAction(self.action_removeMonth)
        self.tableView_shifts.addAction(self.action_calculationShift)
        self.tableView_shifts.addAction(self.action_saveData)

        # действия для comboBox_setting
        self.action_addTariff = QtWidgets.QAction('Добавить тариф')  # добавление еарифа
        self.action_removeTariff = QtWidgets.QAction('Удалить тариф')  # удаление тарифа
        self.action_saveTariffName = QtWidgets.QAction('Сохранить название тарифа')  # сохраняет тариф

        # добавляем действия в comboBox
        self.comboBox_selectTariff.addAction(self.action_addTariff)
        self.comboBox_selectTariff.addAction(self.action_removeTariff)
        self.comboBox_selectTariff.addAction(self.action_saveTariffName)

        # действия для таблицы настроек
        self.action_addRow = QtWidgets.QAction('Добавить строку')  # добавляет строку
        self.action_removeRow = QtWidgets.QAction('Удалить строку')  # удаляет строку
        self.action_saveTariff = QtWidgets.QAction('Сохранить тариф')  # сохраняет тариф
        self.action_saveSettings = QtWidgets.QAction('Сохранить настройки')  # сохраняет данные настроек

        # подключаем действия к таблице
        self.tableView_settingTariff.addAction(self.action_addRow)
        self.tableView_settingTariff.addAction(self.action_removeRow)
        self.tableView_settingTariff.addAction(self.action_saveTariff)
        self.tableView_settingTariff.addAction(self.action_saveSettings)

        # настройка dateEdit
        self.date_shift = date  # экземпляр QDate
        self.dateEdit_shifts.setDate(self.date_shift.today())  # устанавливаем текущую дату в editDate

        # вертикальный HeaderList в таблице смен
        self.shiftVerticalHeaderList = ('Яндекс', 'Gett', 'City', 'Штрафы', 'Аванс', 'Общий накат', 'Тариф',
                                        'Мой процент', 'За смену', 'Выплата')

        # настройка comboBox
        self.tariff_ComboBox_model = QtCore.QStringListModel()  # модель для comboBox
        self.comboBox_selectTariff.setModel(self.tariff_ComboBox_model)  # настраиваем модель для comboBox

        # подготовка таблицы для настройки тарифов
        self.table_settingTariffsModel = QtGui.QStandardItemModel()  # модель для талицы настроек тарифов
        self.tableView_settingTariff.setModel(self.table_settingTariffsModel)  # подключаем модель к таблице
        self.tableHeaderList = ['Накат', 'Проц.']  # список названий колонок
        self.table_settingTariffsModel.setHorizontalHeaderLabels(self.tableHeaderList)  # подключаем названия колонок
        # к таблице

        # настраиваем таблицу смен
        self.StIM_shiftsTable = QtGui.QStandardItemModel()  # модель для талицы смен
        self.StIM_shiftsTable.setVerticalHeaderLabels(self.shiftVerticalHeaderList)  # подключаем лист с названиями
        # строк к таблице
        self.tableView_shifts.setModel(self.StIM_shiftsTable)  # подключаем модель к таблице

        # если файлы, с сохранёнными настройками, существуют то они загружаются для дальнейшего использования
        try:
            self.settingTariffDict = load_data_file('settingTariffDict.txt')  # открываем файл с настройками тарифа
            self.current_index = load_data_file('comboBox_currentIndex.txt')  # открываем файл с настройкой
            # выбранного тарифа
        # если  файлов с настпройками тарифов нет, то выполняется этот код
        except (FileNotFoundError, EOFError):
            # диалоговое окно с информацией о отсутствии настроеных тарифов
            create_dialog_message(splash, 'Тарифы не настроены!', 'Вам нужно настроить тарифы для расчёта зарплаты.')
        # если тарифы настроены то выполняется этот код
        else:
            self.comboBox_selectTariff.addItems(self.settingTariffDict.keys())  # заполнение comboBox названиями тарифов
            self.comboBox_selectTariff.setCurrentIndex(self.current_index)  # настойка ранее выбраного тарифа
            tariff_dict = self.settingTariffDict[self.comboBox_selectTariff.currentText()]  # выбор соответствующих
            # данных

            # по выбраному тарифу заполняется таблица настроек тарифов
            filling_table_settingTariff(tariff_dict, self.table_settingTariffsModel)

        # загружаем данные смен из сохранённого файла dateMont
        filling_table_shifts(self.dateEdit_shifts.text()[3:], self.StIM_shiftsTable)
        # расчитываем выплаты и долг
        calculation_debt(self.label_debt, self.label_salary, self.label_payOut, self.comboBox_selectedMonth)

        # действие при выборе тарифа
        self.comboBox_selectTariff.activated[str].connect(self.comboBox_setting_activated)  # смена тарифа в comboBox
        # действия при выборе месяца
        self.comboBox_selectedMonth.activated[str].connect(self.comboBox_selectedMonth_activated)
        self.action_addTariff.triggered.connect(self.add_new_tariff)  # добавляет тариф
        self.action_removeTariff.triggered.connect(self.remove_tariff)  # удаляет тариф
        self.action_addRow.triggered.connect(self.tableTariff_addRow)  # добавляет строку в таблицу
        self.action_removeRow.triggered.connect(self.tableTariff_removeRow)  # удаляет строку из таблицы
        self.action_saveTariff.triggered.connect(self.tableTariff_saveTariff)  # сожраняет настройки тарифов в словарь
        self.action_saveTariffName.triggered.connect(self.tableTariff_saveTariff)
        self.action_saveSettings.triggered.connect(self.saveSettings)  # сохранят настройки тарифов и программы
        self.action_addShift.triggered.connect(self.addShift_tableShifts)  # добавляем смену
        self.action_calculationShift.triggered.connect(self.calculatedShift)  # расчитываем смену
        self.action_saveData.triggered.connect(self.save_month)  # сохраняем данные по сменам
        self.action_removeShift.triggered.connect(self.removeShift_tableShifts)  # удаляем смену
        self.pushButton_calculation.clicked.connect(self.calculate_dept)  # расчитываем долг
        self.action_addMonth.triggered.connect(self.add_month)  # добавляем месяц
        self.action_removeMonth.triggered.connect(self.remove_month)  # удаляем месяц

    # метод добавляет новый тариф в comboBox
    def add_new_tariff(self):
        self.comboBox_selectTariff.blockSignals(True)  # блокируем сигналы от
        self.comboBox_selectTariff.setEditable(True)  # разрешение на редактирование
        self.comboBox_selectTariff.setEditText('Новый тариф')  # добавляем "Новый тариф"
        index_clear = QtCore.QModelIndex()  # индекс
        self.table_settingTariffsModel.removeRows(0, self.table_settingTariffsModel.rowCount(index_clear),
                                                  parent=index_clear)  # очищаем таблицу тарифов

    # метод удаляет тариф
    def remove_tariff(self):
        ind = self.comboBox_selectTariff.currentIndex()  # индекс выбранного тарифа
        if self.comboBox_selectTariff.currentText() in self.settingTariffDict:  # если название тарифа есть в списке то
            del self.settingTariffDict[self.comboBox_selectTariff.currentText()]  # удаляем тариф из списка
        self.comboBox_selectTariff.removeItem(ind)  # удаляем название тарифа из comboBox

    # метод добавляет строку в таблицу настроек тарифов
    def tableTariff_addRow(self):
        L = []  # лист для заполнения строки
        for i in range(0, 2):  # цикл для заполнения листа
            L.append(QtGui.QStandardItem('0'))  # заполняем лист QStandartItem
        self.table_settingTariffsModel.appendRow(L)  # добавляем строку в таблицу

    # метод удаляет выбранную строку из таблицы настроек тарифов
    def tableTariff_removeRow(self):
        ind_remove = self.tableView_settingTariff.currentIndex()  # индекс выделенной строки
        if ind_remove.isValid():  # если индекс валидный
            self.table_settingTariffsModel.removeRow(ind_remove.row())  # удаляем строку

    # метод сохраняет настройки тарифа в settingTariffDict
    def tableTariff_saveTariff(self):
        key_list = []  # лист для ключей
        date_list = []  # лист для процентов
        settingDateDict = {}  # словарь для данных по настройкам
        ind = QtCore.QModelIndex()  # индекс
        for i in range(0, self.table_settingTariffsModel.rowCount(ind)):  # цикл для перебора по строкам
            if '/' in self.table_settingTariffsModel.index(i, 1).data():  # если колонке с процентами есть этот символ
                percent_list = str(self.table_settingTariffsModel.index(i, 1).data()).split(sep='/')  #
                percent_list[0] = Decimal(percent_list[0]) / Decimal(100)  #
                percent_list[1] = Decimal(percent_list[1]) / Decimal(100)  #
                settingDateDict[self.table_settingTariffsModel.index(i, 0).data()] = percent_list  #
            else:
                date_list.append(Decimal(str(self.table_settingTariffsModel.index(i, 1).data())) / Decimal(100))  #
                key_list.append(str(self.table_settingTariffsModel.index(i, 0).data()))  #
        settingDateDict1 = dict(zip(key_list, date_list))  #
        settingDateDict1.update(settingDateDict)  #
        self.settingTariffDict.update({self.comboBox_selectTariff.currentText(): settingDateDict1})  #
        self.comboBox_selectTariff.blockSignals(False)  #
        self.comboBox_selectTariff.setEditable(False)  #
        return self.settingTariffDict  #

    # метод сохраняет настройки тарифов в файлы
    def saveSettings(self):
        save_data_files('settingTariffDict.txt', self.settingTariffDict)  #
        save_data_files('comboBox_currentIndex.txt', self.comboBox_selectTariff.currentIndex())  #

    # метод активирует выбранный тариф и показывает его настройки
    def comboBox_setting_activated(self, v):
        if v in self.settingTariffDict:  #
            index_clear = QtCore.QModelIndex()
            self.table_settingTariffsModel.removeRows(0, self.table_settingTariffsModel.rowCount(index_clear),
                                                      parent=index_clear)
            tariff_dict = self.settingTariffDict[v]  #
            filling_table_settingTariff(tariff_dict, self.table_settingTariffsModel)

            ind = self.tableView_shifts.currentIndex()  #
            sel = self.tableView_shifts.selectionModel()  #
            if sel.isColumnSelected(ind.column(), QtCore.QModelIndex()):  #
                self.StIM_shiftsTable.setItem(6, ind.column(), QtGui.QStandardItem(self.comboBox_selectTariff.
                                                                                   currentText()))

    #
    def comboBox_selectedMonth_activated(self, v):

        filling_table_shifts(v, self.StIM_shiftsTable)
        # переключаем месяц на выбранный в comboBox
        self.dateEdit_shifts.setDate(self.date_shift.today().replace(month=int(self.comboBox_selectedMonth.
                                                                               currentText()[:-3])))

    #
    def add_month(self):
        self.dateMonth = {}  #
        save_data_files(self.dateEdit_shifts.text()[3:] + '.txt', self.dateMonth)  #
        name_file = name_month_list('save_dates')  #
        self.comboBox_selectedMonth.clear()  #
        self.comboBox_selectedMonth.addItems(name_file)  #

    #
    def remove_month(self):
        index = QtCore.QModelIndex()  # просто индекс
        self.StIM_shiftsTable.removeColumns(0, self.StIM_shiftsTable.columnCount(index), parent=index)  #
        self.dateMonth = {}  #
        os.remove(r'save_dates/' + self.dateEdit_shifts.text()[3:] + '.txt')  #
        name_file = name_month_list('save_dates')  #
        self.comboBox_selectedMonth.clear()  #
        self.comboBox_selectedMonth.addItems(name_file)  #

    # метод добавлят смену в таблицу
    def addShift_tableShifts(self):
        list_row = []  #
        for i in range(0, 9):  #
            list_row.append(QtGui.QStandardItem('0'))  #
        list_row.insert(6, QtGui.QStandardItem(self.comboBox_selectTariff.currentText()))  #
        self.StIM_shiftsTable.appendColumn(list_row)  #
        index = QtCore.QModelIndex()  #
        self.StIM_shiftsTable.setHorizontalHeaderItem(self.StIM_shiftsTable.columnCount(index) - 1,
                                                      QtGui.QStandardItem(self.dateEdit_shifts.text()))  #

    #
    def removeShift_tableShifts(self):
        index = self.tableView_shifts.currentIndex()  #
        if index.isValid():  #
            self.StIM_shiftsTable.removeColumn(index.column())  #

    # метод расчитывает смену
    def calculatedShift(self):
        coefficient = 0  #
        key_reverse_dict: str = ''  #
        ind = self.tableView_shifts.currentIndex()  #
        sel = self.tableView_shifts.selectionModel()  #

        if sel.isColumnSelected(ind.column(), QtCore.QModelIndex()):  #
            fullSalary = sum([Decimal(self.StIM_shiftsTable.index(0, ind.column()).data(role=0)),
                              Decimal(self.StIM_shiftsTable.index(1, ind.column()).data(role=0)),
                              Decimal(self.StIM_shiftsTable.index(2, ind.column()).data(role=0))])  #
            self.StIM_shiftsTable.setItem(5, ind.column(), QtGui.QStandardItem(str(fullSalary)))  #
            reverse_dict = self.settingTariffDict[self.comboBox_selectTariff.currentText()]  #
            for key_reverse_dict in sorted(reverse_dict, reverse=True):  #
                if Decimal(fullSalary) >= Decimal(key_reverse_dict):  #
                    coefficient = reverse_dict[key_reverse_dict]  #
                    break

            if type(coefficient) == list:  #
                over_plan = fullSalary - Decimal(key_reverse_dict)  #
                my_percent = Decimal(key_reverse_dict) * coefficient[0] + over_plan * coefficient[1]  #
                self.StIM_shiftsTable.setItem(7, ind.column(), QtGui.QStandardItem(str(my_percent)))  #
            else:  #
                my_percent = Decimal(fullSalary) * Decimal(coefficient)  #
                self.StIM_shiftsTable.setItem(7, ind.column(), QtGui.QStandardItem(str(my_percent)))  #
            my_salary = my_percent - Decimal(self.StIM_shiftsTable.index(3, ind.column()).data(role=0)) - \
                        Decimal(self.StIM_shiftsTable.index(4, ind.column()).data(role=0))  #
            self.StIM_shiftsTable.setItem(8, ind.column(), QtGui.QStandardItem(str(my_salary)))  #
            self.StIM_shiftsTable.setItem(6, ind.column(), QtGui.QStandardItem(self.comboBox_selectTariff.
                                                                               currentText()))  #
        #
        else:
            create_dialog_message(splash, 'Предупреждение', "Пожалуйста выберите смену для расчёта")

    # расчитываем выплаты и долг
    def calculate_dept(self):
        calculation_debt(self.label_debt, self.label_salary, self.label_payOut, self.comboBox_selectedMonth)

    #  сохраняет даные таблицы за открытый в ней месяц
    def save_month(self):
        index = QtCore.QModelIndex()  # просто индекс
        date_shifts = []   # лист для данных по сменам
        shift_name_list = []  # лист для названий смен

        for j in range(self.StIM_shiftsTable.columnCount(index)):  # цикл для перебора по сменам
            shift_name_list.append(self.StIM_shiftsTable.horizontalHeaderItem(j).text())  # заполняем список именами
            # смен
            date_shift = []  # список для данных по смене
            for i in range(self.StIM_shiftsTable.rowCount(index)):  # цикл для перебора по смене
                date_shift.append(self.StIM_shiftsTable.index(i, j).data())  # заполняем данные за смену
            date_shifts.append(date_shift)  # добавляем данные за смену в список данных за месяц
        self.dateMonth = dict(zip(shift_name_list, date_shifts))  # собираем словарь с данными за месяц

        save_data_files(self.dateEdit_shifts.text()[3:] + '.txt', self.dateMonth)  # сохраняем в файл словарь смен

        name_file = name_month_list('save_dates')  # создаём свежий список файлов месяцев
        self.comboBox_selectedMonth.clear()  # очищаем comboBox
        self.comboBox_selectedMonth.addItems(name_file)  # добавляем новый список


if __name__ == "__main__":
    import sys  # импорт модуля

    app = QtWidgets.QApplication(sys.argv)  # создаём экземпляр QApplication
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("data/yandex_taxi.png"))  # экземпляр загрузочного экрана
    font = QtGui.QFont()  # экземпляр QFont для загрузочного экрана
    font.setFamily("C059 [UKWN]")  # название шрифта
    font.setPointSize(24)  # размер точек
    font.setBold(True)  # толщира шрифта
    font.setItalic(True)  # наклон шрифта
    font.setWeight(75)  # размер шрифта
    splash.setFont(font)  # добавляем шрифт в загрузочный экран
    splash.showMessage("Загрузка данных... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.yellow)
    splash.show()  # Отображаем заставку
    QtWidgets.qApp.processEvents()  # Запускаем оборот цикла
    window = MyWindow()  # Создаем экземпляр класса
    window.setStyleSheet(open("data/taxi_salary_1.qss", "r").read())  # добавляем .qss
    window.setAutoFillBackground(True)  # настраиваем заполнение
    desktop = QtWidgets.QApplication.desktop()  # экземпляр рабочего стола
    window.move(desktop.availableGeometry().center() - window.rect().center())  # помещаем окно программы в центр
    ico = QtGui.QIcon('data/taxi_icon_48.png')  # настраиваем иконку
    window.setWindowIcon(ico)  # добавляем иконку
    load_data(splash)  # Загружаем данные
    window.show()  # Отображаем окно
    splash.finish(window)  # Скрываем заставку
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
