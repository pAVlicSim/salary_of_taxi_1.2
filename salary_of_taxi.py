import os
import pickle
import time
import re

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


def save_data_files(a, b):
    f = open('save_dates/' + a, 'wb')
    pickle.dump(b, f)
    f.close()


def create_dialog_message(a, b, c):
    QtWidgets.QMessageBox.information(a, b, c, defaultButton=QtWidgets.QMessageBox.Ok)


def name_file_comboBox(a: str):
    names_files_list = os.listdir(a)
    name_file = []
    for i in range(len(names_files_list)):
        if re.search('\d+', names_files_list[i]) is not None:
            name_file.append(names_files_list[i][:-4])
    name_file.sort()
    return name_file


class MyWindow(QtWidgets.QMainWindow, my_form.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.action_addShift = QtWidgets.QAction('Добавить смену')
        self.actionRemoveShift = QtWidgets.QAction('Удалить смену')
        self.action_AddMonth = QtWidgets.QAction('Добавить месяц')
        self.action_removeMonth = QtWidgets.QAction('Удалить месяц')
        self.action_saveData = QtWidgets.QAction('Сохранить данные')

        self.tableView_shifts.addAction(self.action_addShift)
        self.tableView_shifts.addAction(self.actionRemoveShift)
        self.tableView_shifts.addAction(self.action_AddMonth)
        self.tableView_shifts.addAction(self.action_removeMonth)
        self.tableView_shifts.addAction(self.action_saveData)


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
    desktop = QtWidgets.QApplication.desktop()
    window.move(desktop.availableGeometry().center() - window.rect().center())
    ico = QtGui.QIcon('data/taxi_icon_48.png')
    window.setWindowIcon(ico)
    load_data(splash)  # Загружаем данные
    window.show()  # Отображаем окно
    splash.finish(window)  # Скрываем заставку
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
