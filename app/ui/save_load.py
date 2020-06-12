import logging
from pathlib import Path

from PyQt5 import QtWidgets

from ..serialize import Serializer


logger = logging.getLogger(__name__)


class SaveLoad(QtWidgets.QWidget):
    def __init__(self, app, save_func, parent=None):
        super(SaveLoad, self).__init__(parent)
        self.app = app
        self.save_func = save_func
        self.app.ui.save_button.clicked.connect(self._on_save_press)
        self.app.ui.load_button.clicked.connect(self._on_load_press)
        self.last_opened = None

    def _on_save_press(self):
        logger.debug("Opening save dialog")
        homedir = str(Path.home())
        (path, _) = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save to file", homedir, "PyMyLedger files (*.pml)"
        )
        if path:
            try:
                logger.info("Got save path %s", path)
                self.save_func(path, self.app.data)
                self.last_opened = path
            except Exception as e:
                logger.exception("Unable to save data!")
                raise

    def _on_load_press(self):
        logger.debug("Opening load dialog")
        homedir = str(Path.home())
        (path, _) = QtWidgets.QFileDialog.getOpenFileName(
            self, "Save to file", homedir, "PyMyLedger files (*.pml)"
        )
        if path:
            try:
                logger.info("Got load path %s", path)
                data = Serializer(path).load()
                logger.debug("Loaded data: %s", data)
                self.last_opened = path
            except Exception as e:
                logger.exception("Unable to load data!")
                raise
            self.app.set_data(data)
