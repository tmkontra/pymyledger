from PyQt5 import QtWidgets

from .gen.ui_new_variable import Ui_NewVariable


class VariableWindow(QtWidgets.QDialog):
    def __init__(self, cb):
        super(VariableWindow, self).__init__()

        self.ui = Ui_NewVariable()
        self.ui.setupUi(self)
        self.setFocusProxy(self.ui.name_text)

        self.callback = cb(self)
        self.ui.buttonBox.clicked.connect(self._on_submit)

    def open(self):
        self.show()
        self.activateWindow()
        self.raise_()
        self.setFocus()
        self.exec_()

    def _on_submit(self, *args, **kwargs):
        name = self.ui.name_text.text()
        if name == "":
            return
        new = VariableLineItem(name)
        self.callback(new)
