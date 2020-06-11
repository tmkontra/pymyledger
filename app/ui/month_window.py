from datetime import datetime

from PyQt5 import QtWidgets, QtCore

from .gen.ui_add_month import Ui_AddMonth

class MonthWindow(QtWidgets.QDialog):
    def __init__(self, cb, instruction=None):
        super(MonthWindow, self).__init__()

        self.ui = Ui_AddMonth()
        self.ui.setupUi(self)
    
        now = datetime.now()
        self.ui.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(0, 0, 0)))

        self.instruction: str = instruction
        self.ui.instruction.setText(instruction or "")

        self.callback = cb
        self.ui.buttonBox.clicked.connect(self._on_new_month_select)

    def open(self):
        self.exec()

    def _on_new_month_select(self, *args, **kwargs):
        d = date_from_qdatetime(self.ui.dateEdit.dateTime())
        print("Date selected:", d)
        self.callback(d)