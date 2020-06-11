# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'static.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewStatic(object):
    def setupUi(self, NewStatic):
        NewStatic.setObjectName("NewStatic")
        NewStatic.resize(395, 110)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewStatic)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(NewStatic)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 20, 221, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_text.setObjectName("name_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_text)
        self.amount_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.amount_label.setObjectName("amount_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.amount_label)
        self.amount_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.amount_text.setObjectName("amount_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.amount_text)

        self.retranslateUi(NewStatic)
        self.buttonBox.accepted.connect(NewStatic.accept)
        self.buttonBox.rejected.connect(NewStatic.reject)
        QtCore.QMetaObject.connectSlotsByName(NewStatic)

    def retranslateUi(self, NewStatic):
        _translate = QtCore.QCoreApplication.translate
        NewStatic.setWindowTitle(_translate("NewStatic", "Dialog"))
        self.name_label.setText(_translate("NewStatic", "Name"))
        self.amount_label.setText(_translate("NewStatic", "Amount"))
