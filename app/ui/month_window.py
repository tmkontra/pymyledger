from datetime import datetime
import logging

from PyQt5 import QtWidgets, QtCore

from .gen.ui_add_month import Ui_AddMonth
from .utils import date_from_qdatetime

logger = logging.getLogger(__name__)


class MonthWindow(QtWidgets.QDialog):
    def __init__(self, cb, instruction=None):
        super(MonthWindow, self).__init__()

        self.ui = Ui_AddMonth()
        self.ui.setupUi(self)

        now = datetime.now()
        self.ui.dateEdit.setDateTime(
            QtCore.QDateTime(
                QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(0, 0, 0)
            )
        )

        self.instruction: str = instruction
        self.ui.instruction.setText(instruction or "")

        self.callback = cb
        self.ui.buttonBox.accepted.connect(self._on_new_month_select)
        self.ui.buttonBox.rejected.connect(self._on_cancel)

    def open(self):
        self.exec()

    def _on_cancel(self, *args, **kwargs):
        logger.debug("Canceled month select")

    def _on_new_month_select(self, *args, **kwargs):
        d = date_from_qdatetime(self.ui.dateEdit.dateTime())
        logger.debug("Date selected: %s", d)
        self.callback(d)
