# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resource/month.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddMonth(object):
    def setupUi(self, AddMonth):
        AddMonth.setObjectName("AddMonth")
        AddMonth.resize(444, 110)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddMonth)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dateEdit = QtWidgets.QDateEdit(AddMonth)
        self.dateEdit.setGeometry(QtCore.QRect(90, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.dateEdit.setFont(font)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.instruction = QtWidgets.QLabel(AddMonth)
        self.instruction.setGeometry(QtCore.QRect(60, 10, 191, 21))
        self.instruction.setObjectName("instruction")

        self.retranslateUi(AddMonth)
        self.buttonBox.accepted.connect(AddMonth.accept)
        self.buttonBox.rejected.connect(AddMonth.reject)
        QtCore.QMetaObject.connectSlotsByName(AddMonth)

    def retranslateUi(self, AddMonth):
        _translate = QtCore.QCoreApplication.translate
        AddMonth.setWindowTitle(_translate("AddMonth", "Dialog"))
        self.dateEdit.setDisplayFormat(_translate("AddMonth", "MMM yyyy"))
        self.instruction.setText(_translate("AddMonth", "Please Select A Month To Start:"))
