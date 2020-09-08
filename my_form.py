# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 505)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 300))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 505))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.centralWidget.setFont(font)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 400))
        self.tabWidget.setBaseSize(QtCore.QSize(300, 500))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 6)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.comboBox_selectTariff = QtWidgets.QComboBox(self.tab)
        self.comboBox_selectTariff.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_selectTariff.setEditable(False)
        self.comboBox_selectTariff.setMaxVisibleItems(5)
        self.comboBox_selectTariff.setMaxCount(10)
        self.comboBox_selectTariff.setObjectName("comboBox_selectTariff")
        self.verticalLayout_2.addWidget(self.comboBox_selectTariff)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableView_settingTariff = QtWidgets.QTableView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_settingTariff.sizePolicy().hasHeightForWidth())
        self.tableView_settingTariff.setSizePolicy(sizePolicy)
        self.tableView_settingTariff.setMinimumSize(QtCore.QSize(200, 200))
        self.tableView_settingTariff.setMaximumSize(QtCore.QSize(200, 400))
        self.tableView_settingTariff.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableView_settingTariff.setAlternatingRowColors(True)
        self.tableView_settingTariff.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView_settingTariff.setObjectName("tableView_settingTariff")
        self.tableView_settingTariff.horizontalHeader().setDefaultSectionSize(70)
        self.tableView_settingTariff.horizontalHeader().setMinimumSectionSize(30)
        self.verticalLayout_2.addWidget(self.tableView_settingTariff)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_salary = QtWidgets.QLabel(self.tab_2)
        self.label_salary.setEnabled(True)
        self.label_salary.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_salary.setText("")
        self.label_salary.setAlignment(QtCore.Qt.AlignCenter)
        self.label_salary.setObjectName("label_salary")
        self.verticalLayout_3.addWidget(self.label_salary)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_payOut = QtWidgets.QLabel(self.tab_2)
        self.label_payOut.setEnabled(True)
        self.label_payOut.setText("")
        self.label_payOut.setAlignment(QtCore.Qt.AlignCenter)
        self.label_payOut.setObjectName("label_payOut")
        self.verticalLayout_3.addWidget(self.label_payOut)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_dept = QtWidgets.QLabel(self.tab_2)
        self.label_dept.setEnabled(True)
        self.label_dept.setText("")
        self.label_dept.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dept.setObjectName("label_dept")
        self.verticalLayout_3.addWidget(self.label_dept)
        self.pushButton_calculation = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_calculation.setObjectName("pushButton_calculation")
        self.verticalLayout_3.addWidget(self.pushButton_calculation)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setMinimumSize(QtCore.QSize(400, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.dateEdit_shifts = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_shifts.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_shifts.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_shifts.setCalendarPopup(True)
        self.dateEdit_shifts.setObjectName("dateEdit_shifts")
        self.horizontalLayout_3.addWidget(self.dateEdit_shifts)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_selectedMonth = QtWidgets.QComboBox(self.widget)
        self.comboBox_selectedMonth.setMaxCount(24)
        self.comboBox_selectedMonth.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_selectedMonth.setObjectName("comboBox_selectedMonth")
        self.horizontalLayout_3.addWidget(self.comboBox_selectedMonth)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView_shifts = QtWidgets.QTableView(self.widget)
        self.tableView_shifts.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableView_shifts.setAlternatingRowColors(True)
        self.tableView_shifts.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView_shifts.setObjectName("tableView_shifts")
        self.tableView_shifts.horizontalHeader().setDefaultSectionSize(70)
        self.tableView_shifts.verticalHeader().setDefaultSectionSize(70)
        self.verticalLayout.addWidget(self.tableView_shifts)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 864, 25))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menu_Tariffs = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menu_Tariffs.setFont(font)
        self.menu_Tariffs.setObjectName("menu_Tariffs")
        self.menu_settingTariffs = QtWidgets.QMenu(self.menu_Tariffs)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menu_settingTariffs.setFont(font)
        self.menu_settingTariffs.setObjectName("menu_settingTariffs")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_addTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_addTariff.setFont(font)
        self.action_addTariff.setObjectName("action_addTariff")
        self.action_removeTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_removeTariff.setFont(font)
        self.action_removeTariff.setObjectName("action_removeTariff")
        self.action_addRow = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_addRow.setFont(font)
        self.action_addRow.setObjectName("action_addRow")
        self.action_removeRow = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_removeRow.setFont(font)
        self.action_removeRow.setObjectName("action_removeRow")
        self.action_saveTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_saveTariff.setFont(font)
        self.action_saveTariff.setObjectName("action_saveTariff")
        self.action_saveSettings = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_saveSettings.setFont(font)
        self.action_saveSettings.setObjectName("action_saveSettings")
        self.menu_settingTariffs.addAction(self.action_addRow)
        self.menu_settingTariffs.addAction(self.action_removeRow)
        self.menu_settingTariffs.addSeparator()
        self.menu_settingTariffs.addAction(self.action_saveTariff)
        self.menu_settingTariffs.addAction(self.action_saveSettings)
        self.menu_Tariffs.addAction(self.action_addTariff)
        self.menu_Tariffs.addAction(self.action_removeTariff)
        self.menu_Tariffs.addSeparator()
        self.menu_Tariffs.addAction(self.menu_settingTariffs.menuAction())
        self.menuBar.addAction(self.menu_Tariffs.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моя зарплата в такси"))
        self.label_2.setText(_translate("MainWindow", "Выбор тарифа"))
        self.label_3.setText(_translate("MainWindow", "Настройки тарифа"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Настройки тарифа"))
        self.label_6.setText(_translate("MainWindow", "Доход"))
        self.label_7.setText(_translate("MainWindow", "Выплаты"))
        self.label_9.setText(_translate("MainWindow", "Долг"))
        self.pushButton_calculation.setText(_translate("MainWindow", "Расчитать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Зарплата"))
        self.label.setText(_translate("MainWindow", "Дата смены"))
        self.label_4.setText(_translate("MainWindow", "Выбор месяца"))
        self.menu_Tariffs.setTitle(_translate("MainWindow", "Тарифы"))
        self.menu_settingTariffs.setTitle(_translate("MainWindow", "Настроить тарифы"))
        self.action_addTariff.setText(_translate("MainWindow", "Добавить тариф"))
        self.action_removeTariff.setText(_translate("MainWindow", "Удалить тариф"))
        self.action_addRow.setText(_translate("MainWindow", "Добвить строку"))
        self.action_removeRow.setText(_translate("MainWindow", "Удалить строку"))
        self.action_saveTariff.setText(_translate("MainWindow", "Сохранить тариф"))
        self.action_saveSettings.setText(_translate("MainWindow", "Сохранить настройки"))