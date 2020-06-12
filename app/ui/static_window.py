from PyQt5 import QtWidgets

from ..model import StaticLineItem
from .gen.ui_new_static import Ui_NewStatic


class StaticWindow(QtWidgets.QDialog):
    def __init__(self, cb):
        super(StaticWindow, self).__init__()

        self.ui = Ui_NewStatic()
        self.ui.setupUi(self)

        self.callback = cb(self)
        self.ui.buttonBox.clicked.connect(self._on_submit)

    def open(self):
        self.exec()

    def _on_submit(self, *args, **kwargs):
        name = self.ui.name_text.text()
        try:
            amount = int(self.ui.amount_text.text())
        except ValueError:
            return
        new = StaticLineItem(name, amount)
        self.callback(new)
