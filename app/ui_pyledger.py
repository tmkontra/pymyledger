# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resource/acc.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyLedger(object):
    def setupUi(self, PyLedger):
        PyLedger.setObjectName("PyLedger")
        PyLedger.resize(777, 616)
        PyLedger.setMaximumSize(QtCore.QSize(777, 616))
        self.main_widget = QtWidgets.QWidget(PyLedger)
        self.main_widget.setObjectName("main_widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.main_widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 8, 761, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setObjectName("grid")
        self.static_table = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.static_table.setObjectName("static_table")
        self.static_table.setColumnCount(0)
        self.static_table.setRowCount(0)
        self.grid.addWidget(self.static_table, 6, 0, 1, 1)
        self.add_static = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_static.setObjectName("add_static")
        self.grid.addWidget(self.add_static, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.variable_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.variable_label.setObjectName("variable_label")
        self.grid.addWidget(self.variable_label, 5, 2, 1, 1)
        self.static_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.static_label.setObjectName("static_label")
        self.grid.addWidget(self.static_label, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.grid.addItem(spacerItem, 6, 1, 1, 1)
        self.new_month = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.new_month.setObjectName("new_month")
        self.grid.addWidget(self.new_month, 0, 2, 1, 1)
        self.month_button_layout = QtWidgets.QHBoxLayout()
        self.month_button_layout.setObjectName("month_button_layout")
        self.month_select = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.month_select.setObjectName("month_select")
        self.month_button_layout.addWidget(self.month_select)
        self.grid.addLayout(self.month_button_layout, 0, 0, 1, 2)
        self.add_variable = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_variable.setObjectName("add_variable")
        self.grid.addWidget(self.add_variable, 7, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.variable_table = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.variable_table.setObjectName("variable_table")
        self.variable_table.setColumnCount(0)
        self.variable_table.setRowCount(0)
        self.grid.addWidget(self.variable_table, 6, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.main_widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(310, 470, 151, 85))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.liabilities_text = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.liabilities_text.setObjectName("liabilities_text")
        self.gridLayout.addWidget(self.liabilities_text, 1, 1, 1, 1)
        self.assets_text = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.assets_text.setObjectName("assets_text")
        self.gridLayout.addWidget(self.assets_text, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.liabilities_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.liabilities_label.setObjectName("liabilities_label")
        self.gridLayout.addWidget(self.liabilities_label, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.assets_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.assets_label.setObjectName("assets_label")
        self.gridLayout.addWidget(self.assets_label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)
        self.balance_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.balance_label.setObjectName("balance_label")
        self.gridLayout.addWidget(self.balance_label, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.balance_text = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.balance_text.setObjectName("balance_text")
        self.gridLayout.addWidget(self.balance_text, 3, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(520, 480, 171, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.save_load_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.save_load_layout.setContentsMargins(0, 0, 0, 0)
        self.save_load_layout.setObjectName("save_load_layout")
        self.load_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_button.setObjectName("load_button")
        self.save_load_layout.addWidget(self.load_button, 0, QtCore.Qt.AlignHCenter)
        self.save_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setKerning(True)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(77, 125, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.save_button.setCheckable(False)
        self.save_button.setObjectName("save_button")
        self.save_load_layout.addWidget(self.save_button, 0, QtCore.Qt.AlignHCenter)
        PyLedger.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(PyLedger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 22))
        self.menubar.setObjectName("menubar")
        self.menuLedger = QtWidgets.QMenu(self.menubar)
        self.menuLedger.setObjectName("menuLedger")
        PyLedger.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyLedger)
        self.statusbar.setObjectName("statusbar")
        PyLedger.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLedger.menuAction())

        self.retranslateUi(PyLedger)
        QtCore.QMetaObject.connectSlotsByName(PyLedger)

    def retranslateUi(self, PyLedger):
        _translate = QtCore.QCoreApplication.translate
        PyLedger.setWindowTitle(_translate("PyLedger", "MainWindow"))
        self.add_static.setText(_translate("PyLedger", "Add Static Line Item"))
        self.variable_label.setText(_translate("PyLedger", "Variable"))
        self.static_label.setText(_translate("PyLedger", "Static"))
        self.new_month.setText(_translate("PyLedger", "New Month"))
        self.add_variable.setText(_translate("PyLedger", "Add Variable Line Item"))
        self.liabilities_text.setText(_translate("PyLedger", "0"))
        self.assets_text.setText(_translate("PyLedger", "0"))
        self.liabilities_label.setText(_translate("PyLedger", "Liabilities"))
        self.assets_label.setText(_translate("PyLedger", "Assets"))
        self.balance_label.setText(_translate("PyLedger", "Balance"))
        self.balance_text.setText(_translate("PyLedger", "0"))
        self.load_button.setText(_translate("PyLedger", "Load..."))
        self.save_button.setText(_translate("PyLedger", "Save..."))
        self.menuLedger.setTitle(_translate("PyLedger", "Ledger"))
