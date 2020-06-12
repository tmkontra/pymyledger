# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'variable.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewVariable(object):
    def setupUi(self, NewVariable):
        NewVariable.setObjectName("NewVariable")
        NewVariable.resize(398, 93)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewVariable)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(NewVariable)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 221, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_text.setObjectName("name_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_text)

        self.retranslateUi(NewVariable)
        self.buttonBox.accepted.connect(NewVariable.accept)
        self.buttonBox.rejected.connect(NewVariable.reject)
        QtCore.QMetaObject.connectSlotsByName(NewVariable)

    def retranslateUi(self, NewVariable):
        _translate = QtCore.QCoreApplication.translate
        NewVariable.setWindowTitle(_translate("NewVariable", "Dialog"))
        self.name_label.setText(_translate("NewVariable", "Name"))
