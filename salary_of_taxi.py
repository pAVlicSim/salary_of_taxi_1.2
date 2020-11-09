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


def load_data_file(a):
    f = open('save_dates/' + a, 'rb')  # открываем файл
    b = pickle.load(f)  # загружаем файл в словарь
    f.close()  # закрываем файл
    return b


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
        if re.search(r'\d+', names_files_list[i]) is not None:  # если в названии файла есть цифры
            name_file.append(names_files_list[i][:-4])  # имя файла добавляется в список
    name_file.sort()  # сортируем список
    return name_file


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

        self.current_index_comboBox = None  # для хранения выбранного индекса comboBox
        self.settingTariffDict = {}  # для хранения настроек тарифов
        self.dateMonth = {}  # словарь для хранения данных по сменам за месяц

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

        self.stackedWidget.setCurrentIndex(0)  #

        # если файлы, с сохранёнными настройками, существуют то они загружаются для дальнейшего использования
        try:
            self.settingTariffDict = load_data_file('settingTariffDict.txt')  # открываем файл с настройками тарифа
            self.current_index_comboBox = load_data_file('comboBox_currentIndex.txt')  # открываем файл с настройкой
            # выбранного тарифа
        # если  файлов с настпройками тарифов нет, то выполняется этот код
        except (FileNotFoundError, EOFError):
            # диалоговое окно с информацией о отсутствии настроеных тарифов
            create_dialog_message(splash, 'Тарифы не настроены!', 'Вам нужно настроить тарифы для расчёта зарплаты.')
        # если тарифы настроены то выполняется этот код
        else:
            self.comboBox_selectTariff.addItems(self.settingTariffDict.keys())  # заполнение comboBox названиями тарифов
            self.comboBox_selectTariff.setCurrentIndex(self.current_index_comboBox)  # настойка ранее выбраного тарифа
            tariff_dict = self.settingTariffDict[self.comboBox_selectTariff.currentText()]  # выбор соответствующих
            # данных

            # по выбраному тарифу заполняется таблица настроек тарифов
            tariff_keys = list(tariff_dict.keys())  # список для ключей
            tariff_list: List[Any] = list(tariff_dict.values())  # список для настроек тарифов
            for row in range(len(tariff_dict)):  # цикл для заполнения таблицы
                if type(tariff_list[row]) == list:
                    percent_list = ''  #
                    percent_list_final = ''  #
                    for j in range(len(tariff_list[row])):  #
                        percent = str(tariff_list[row][j] * 100)  #
                        percent_list += percent + ' / '  #
                        percent_list_final = percent_list[:-3]  #
                    item_l0 = QtGui.QStandardItem(str(tariff_keys[row]))  #
                    item_l1 = QtGui.QStandardItem(percent_list_final)  #
                    self.table_settingTariffsModel.setItem(row, 0, item_l0)  #
                    self.table_settingTariffsModel.setItem(row, 1, item_l1)  #
                else:
                    item_0 = QtGui.QStandardItem(str(tariff_keys[row]))  # модель для заполнения первой колонки
                    item_1 = QtGui.QStandardItem(str(tariff_list[row] * 100))  # модель для заполнения
                    # второй колонки
                    self.table_settingTariffsModel.setItem(row, 0, item_0)  # заполняем первую колонки
                    self.table_settingTariffsModel.setItem(row, 1, item_1)  # заполняем вторую колонку

        # загружаем данные смен из сохранённого файла dateMont
        try:
            self.dateMonth = load_data_file(self.dateEdit_shifts.text()[3:] + '.txt')  # открываем файл со сменами
            # текущего месяца
        # если файла не существует выполняется этот код
        except(FileNotFoundError, EOFError):
            # диалоговое окно с информацией о отсутствии смен в текущем месяце
            create_dialog_message(splash, 'Нет смен в текущем месяце.', 'Создайте смены или загрузите другой месяц.')
        except _pickle.UnpicklingError:
            create_dialog_message(splash, 'Файл повреждён!!!', 'Требуется восстановление файла')
        # если файл существует то заполняем таблицу смен
        else:
            shiftsNameList = list(self.dateMonth.keys())  # список названий смен
            self.StIM_shiftsTable.setHorizontalHeaderLabels(shiftsNameList)  # список горизонтальных заголовков
            index = QtCore.QModelIndex()  # просто индекс
            date_list = []  # список для временного хранения данных по сменам
            for key_dateMonth in self.dateMonth.keys():  # цикл для заполнения списка данных по сменам
                date_list.append(self.dateMonth[key_dateMonth])  # заполняем список с данными по сменам
            for j in range(self.StIM_shiftsTable.columnCount(index)):  # цикл по колонкам
                for row in range(self.StIM_shiftsTable.rowCount(index)):  # цикл по строкам
                    self.StIM_shiftsTable.setItem(row, j, QtGui.QStandardItem(date_list[j][row]))  # заполнение таблицы
                    # данными по сменам
            # расчитываем выплаты и долг
            name_month = name_month_list('save_dates')  # получаем названия файлов месяцев
            for i in range(len(name_month)):  #
                dateMonth = load_data_file(name_month[i] + '.txt')  #
                salary_list = []  #
                payOut_list = []  #
                key_dateMonth: str  #
                for key_dateMonth in dateMonth.keys():  #
                    salary_list.append(Decimal(dateMonth[key_dateMonth][8]))  #
                    payOut_list.append(Decimal(dateMonth[key_dateMonth][9]))  #
                f_salary = Decimal(sum(salary_list))  #
                payOut = Decimal(sum(payOut_list))  #
                self.label_debt.setText(str(f_salary - payOut))  #
                self.label_salary.setText(str(f_salary))  #
                self.label_payOut.setText(str(payOut))  #

            # заполняем comboBox названиями месяцев
            self.comboBox_selectedMonth.addItems(name_month)

        # действие при выборе тарифа
        self.comboBox_selectTariff.activated[str].connect(self.comboBox_setting_activated)  # смена тарифа в comboBox
        # действия меню
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
        self.action_calculationShift.triggered.connect(self.calculated_percentShift)  # расчитываем смену
        self.action_saveData.triggered.connect(self.save_dates)  # сохраняем данные по сменам
        self.action_removeShift.triggered.connect(self.removeShift_tableShifts)  # удаляем смену
        self.pushButton_calculation.clicked.connect(self.calculate_dept)  #
        self.action_addMonth.triggered.connect(self.add_month)  #
        self.action_removeMonth.triggered.connect(self.remove_month)  #
        self.action_salary.triggered.connect(self.show_widget_salary)
        self.action_tariff.triggered.connect(self.show_widget_settingTariff)
        self.action_rent.triggered.connect(self.show_widget_rent)
        self.action_easy_rental.triggered.connect(self.show_widget_easy_rental)

    def show_widget_salary(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_widget_settingTariff(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_widget_rent(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_widget_easy_rental(self):
        self.stackedWidget.setCurrentIndex(3)

    # метод добавляет новый тариф в comboBox
    def add_new_tariff(self):
        self.comboBox_selectTariff.blockSignals(True)  #
        self.comboBox_selectTariff.setEditable(True)  # разрешение на редактирование
        self.comboBox_selectTariff.setEditText('Новый тариф')  # добавляем "Новый тариф"
        index_clear = QtCore.QModelIndex()
        self.table_settingTariffsModel.removeRows(0, self.table_settingTariffsModel.rowCount(index_clear),
                                                  parent=index_clear)

    # метод удаляет тариф
    def remove_tariff(self):
        ind = self.comboBox_selectTariff.currentIndex()  # индекс выбранного тарифа
        if self.comboBox_selectTariff.currentText() in self.settingTariffDict:  # если название тарифа есть в списке то
            del self.settingTariffDict[self.comboBox_selectTariff.currentText()]  # удаляем тариф из списка
        self.comboBox_selectTariff.removeItem(ind)  # удаляем название тарифа из comboBox

    # метод добавляет строку в таблицу настроек тарифов
    def tableTariff_addRow(self):
        L = []  #
        for i in range(0, 2):  #
            L.append(QtGui.QStandardItem('0'))  #
        self.table_settingTariffsModel.appendRow(L)  #

    # метод удаляет выбранную строку из таблицы настроек тарифов
    def tableTariff_removeRow(self):
        ind_remove = self.tableViewSetting.currentIndex()  #
        if ind_remove.isValid():  #
            self.table_settingTariffsModel.removeRow(ind_remove.row())  #

    # метод сохраняет настройки тарифа в settingTariffDict
    def tableTariff_saveTariff(self):
        key_list = []  #
        date_list = []  #
        settingDateDict = {}  #
        ind = QtCore.QModelIndex()  #
        for i in range(0, self.table_settingTariffsModel.rowCount(ind)):  #
            if '/' in self.table_settingTariffsModel.index(i, 1).data():  #
                percent_list = str(self.table_settingTariffsModel.index(i, 1).data()).split(sep='/')  #
                percent_list[0] = Decimal(percent_list[0].replace(',', '.')) / Decimal(100)  #
                percent_list[1] = Decimal(percent_list[1].replace(',', '.')) / Decimal(100)  #
                settingDateDict[self.table_settingTariffsModel.index(i, 0).data()] = percent_list  #
            else:
                date_list.append(Decimal(str(self.table_settingTariffsModel.index(i, 1).data()).replace(',', '.')) /
                                 Decimal(100))  #
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
            tariff_keys = list(tariff_dict.keys())  #
            tariff_list = list(tariff_dict.values())  #
            for row in range(len(tariff_dict)):  #
                if type(tariff_list[row]) == list:  #
                    percent_list = ''  #
                    percent_list_final = ''  #
                    for j in range(len(tariff_list[row])):  #
                        percent = str(tariff_list[row][j] * 100)  #
                        percent_list += percent + ' / '  #
                        percent_list_final = percent_list[:-3].replace('.', ',')  #
                    item_l0 = QtGui.QStandardItem(str(tariff_keys[row]))  #
                    item_l1 = QtGui.QStandardItem(percent_list_final)  #
                    self.table_settingTariffsModel.setItem(row, 0, item_l0)  #
                    self.table_settingTariffsModel.setItem(row, 1, item_l1)  #
                else:
                    item_0 = QtGui.QStandardItem(str(tariff_keys[row]))  #
                    item_1 = QtGui.QStandardItem(str(tariff_list[row] * 100).replace('.', ','))  #
                    self.table_settingTariffsModel.setItem(row, 0, item_0)  #
                    self.table_settingTariffsModel.setItem(row, 1, item_1)  #

            ind = self.tableView_shifts.currentIndex()  #
            sel = self.tableView_shifts.selectionModel()  #
            if sel.isColumnSelected(ind.column(), QtCore.QModelIndex()):  #
                self.StIM_shiftsTable.setItem(6, ind.column(), QtGui.QStandardItem(self.comboBox_selectTariff.
                                                                                   currentText()))

    #
    def comboBox_selectedMonth_activated(self, v):
        try:
            self.dateMonth = load_data_file(v + '.txt')  #
        except(FileNotFoundError, EOFError):  #
            # диалоговое окно с информацией о отсутствии смен в текущем месяце
            create_dialog_message(splash, 'Нет смен в выбраном месяце.', 'Попробуйте выбрать другой месяц.')
            # если файл существует то заполняем таблицу смен
        except _pickle.UnpicklingError:  #
            create_dialog_message(splash, 'Файл повреждён!!!', 'Требуется восстановление файла')
        else:  #
            index = QtCore.QModelIndex()  # просто индекс
            self.StIM_shiftsTable.removeColumns(0, self.StIM_shiftsTable.columnCount(index), parent=index)  #
            shiftsNameList = list(self.dateMonth.keys())  # список названий смен
            self.StIM_shiftsTable.setHorizontalHeaderLabels(shiftsNameList)  # список горизонтальных заголовков
            date_list = []  # список для временного хранения данных по сменам
            for key_dateMonth in self.dateMonth.keys():  # цикл для заполнения списка данных по сменам
                date_list.append(self.dateMonth[key_dateMonth])  # заполняем список с данными по сменам
            for j in range(self.StIM_shiftsTable.columnCount(index)):  # цикл по колонкам
                for row in range(self.StIM_shiftsTable.rowCount(index)):  # цикл по строкам
                    self.StIM_shiftsTable.setItem(row, j, QtGui.QStandardItem(date_list[j][row]))  # заполнение таблицы
                    # данными по сменам
            self.dateEdit_shifts.setDate(self.date_shift.today().replace(month=int(self.comboBox_selectedMonth.
                                                                                   currentText()[:-3])))  #

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
    def calculated_percentShift(self):
        coefficient = 0  #
        key_reverse_dict = ''  #
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
            my_salary = (my_percent - Decimal(self.StIM_shiftsTable.index(3, ind.column()).data(role=0)) -
                         Decimal(self.StIM_shiftsTable.index(4, ind.column()).data(role=0)))  #
            self.StIM_shiftsTable.setItem(8, ind.column(), QtGui.QStandardItem(str(my_salary)))  #
            self.StIM_shiftsTable.setItem(6, ind.column(), QtGui.QStandardItem(self.comboBox_selectTariff.
                                                                               currentText()))  #
        #
        else:
            QtWidgets.QMessageBox.information(splash, "Предупреждение",
                                              "Пожалуйста выберите смену для расчёта",
                                              buttons=QtWidgets.QMessageBox.Close,
                                              defaultButton=QtWidgets.QMessageBox.Ok)

    def calculated_rentShift(self):
        ind = self.tableView_shifts.currentIndex()  #
        sel = self.tableView_shifts.selectionModel()  #

        if sel.isColumnSelected(ind.column(), QtCore.QModelIndex()):  #
            fullSalary = sum([Decimal(self.StIM_shiftsTable.index(0, ind.column()).data(role=0)),
                              Decimal(self.StIM_shiftsTable.index(1, ind.column()).data(role=0)),
                              Decimal(self.StIM_shiftsTable.index(2, ind.column()).data(role=0))])  #
            self.StIM_shiftsTable.setItem(5, ind.column(), QtGui.QStandardItem(str(fullSalary)))  #

    # расчитываем выплаты и долг
    def calculate_dept(self):
        salary_list = []  #
        payOut_list = []  #
        key_dateMonth: str  #
        name_month = name_month_list('save_dates')  # получаем названия файлов месяцев
        for i in range(len(name_month)):  #
            dateMonth = load_data_file(name_month[i] + '.txt')  #
            for key_dateMonth in dateMonth.keys():  #
                salary_list.append(Decimal(dateMonth[key_dateMonth][8]))  #
                payOut_list.append(Decimal(dateMonth[key_dateMonth][9]))  #
        f_salary = Decimal(sum(salary_list))  #
        payOut = Decimal(sum(payOut_list))  #
        self.label_debt.setText(str(f_salary - payOut))  #
        self.label_salary.setText(str(f_salary))  #
        self.label_payOut.setText(str(payOut))  #

    #
    def save_dates(self):
        index = QtCore.QModelIndex()  #
        date_shifts = []  #
        shift_name_list = []  #
        for j in range(self.StIM_shiftsTable.columnCount(index)):  #
            shift_name_list.append(self.StIM_shiftsTable.horizontalHeaderItem(j).text())  #

        for j in range(self.StIM_shiftsTable.columnCount(index)):  #
            date_shift = []  #
            for i in range(self.StIM_shiftsTable.rowCount(index)):  #
                date_shift.append(self.StIM_shiftsTable.index(i, j).data())  #
            date_shifts.append(date_shift)  #
        self.dateMonth = dict(zip(shift_name_list, date_shifts))  #

        save_data_files(self.dateEdit_shifts.text()[3:] + '.txt', self.dateMonth)  #

        name_file = name_month_list('save_dates')  #
        self.comboBox_selectedMonth.clear()  #
        self.comboBox_selectedMonth.addItems(name_file)  #


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("data/yandex_taxi.png"))
    font = QtGui.QFont()
    font.setFamily("C059 [UKWN]")
    font.setPointSize(24)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    splash.setFont(font)
    splash.showMessage("Загрузка данных... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.yellow)
    splash.show()  # Отображаем заставку
    QtWidgets.qApp.processEvents()  # Запускаем оборот цикла
    window = MyWindow()  # Создаем экземпляр класса
    window.setStyleSheet(open("data/taxi_salary_1.qss", "r").read())
    window.setAutoFillBackground(True)
    desktop = QtWidgets.QApplication.desktop()
    window.move(desktop.availableGeometry().center() - window.rect().center())
    ico = QtGui.QIcon('data/taxi_icon_48.png')
    window.setWindowIcon(ico)
    load_data(splash)  # Загружаем данные
    window.show()  # Отображаем окно
    splash.finish(window)  # Скрываем заставку
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
