from pathlib import Path

from PyQt5 import QtWidgets

from ..serialize import Serializer


class SaveLoad(QtWidgets.QWidget):
    def __init__(self, app, save_func, parent=None):
        super(SaveLoad, self).__init__(parent)
        self.app = app
        self.save_func = save_func
        self.app.ui.save_button.clicked.connect(self._on_save_press)
        self.app.ui.load_button.clicked.connect(self._on_load_press)
        self.last_opened = None

    def _on_save_press(self):
        print("opening save dialog")
        homedir = str(Path.home())
        (path, _) = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save to file", homedir, "PyMyLedger files (*.pml)"
        )
        if path:
            try:
                print("got path", path)
                self.save_func(path, self.app.data)
                self.last_opened = path
            except Exception as e:
                print("Unable to save data!")
                raise

    def _on_load_press(self):
        print("opening load dialog")
        homedir = str(Path.home())
        (path, _) = QtWidgets.QFileDialog.getOpenFileName(
            self, "Save to file", homedir, "PyMyLedger files (*.pml)"
        )
        if path:
            try:
                data = Serializer(path).load()
                print("loaded data:", data)
                self.last_opened = path
            except Exception as e:
                print("Unable to load data!")
                raise
                data = None
            self.app.set_data(data)
