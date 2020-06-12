import logging
import signal

from PyQt5 import QtWidgets, QtCore

from .cache import Cache
from .model import Data, Ledger
from .serialize import Serializer
from .ui import ApplicationWindow


logger = logging.getLogger(__name__)


class PyMyLedger:
    _default_profile_name = "My Profile"
    _appname = "PyMyLedger"

    def __init__(self, args=None, **kwargs):
        args = args or []
        self._qt: QtWidgets.QApplication = QtWidgets.QApplication(args)
        self._qt.setApplicationDisplayName(self._appname)

        self.cache = Cache(self._appname)

        last_open = self.cache.get("last_opened")
        if last_open:
            data = self._load(last_open)
        else:
            data = None

        save_func = lambda fp, d: Serializer(fp).save(d)
        self._window: ApplicationWindow = ApplicationWindow(save_func)
        self._set_data(data)
        self._register_signal_handlers()
        self._start_timer()
        self._window.show()
        self._qt.exec()
        self.on_shutdown()

    def _set_data(self, data=None):
        if data is None:
            data = self.default_data
            needs_month = True
        else:
            needs_month = False
        self._window.set_data(data)
        if needs_month:
            self._window.month_select("Please Select A Month To Start:")

    def on_shutdown(self):
        lo = self._window.save_load.last_opened
        if lo:
            logger.info("Caching last file location %s", lo)
            self.cache.update("last_opened", lo)
            self.cache.flush()

    @property
    def default_data(self):
        logger.debug("Initializing default data")
        data = Data(Ledger())
        return data

    @staticmethod
    def _load(fp):
        try:
            logger.info("Loading data from %s", fp)
            return Serializer(fp).load()
        except Exception:
            logger.exception("Error loading file %s", fp)
            return None

    def _register_signal_handlers(self):
        signal.signal(signal.SIGINT, self.sigint_handler)
        signal.signal(signal.SIGQUIT, self.sigquit_handler)

    @staticmethod
    def sigint_handler(*args):
        """Handler for the SIGINT signal."""
        logger.debug("Goodbye!")
        QtWidgets.QApplication.quit()

    def sigquit_handler(self, *args):
        logger.debug("\n")
        logger.debug("Profile")
        logger.debug(self._window.data.profile.__dict__)
        logger.debug("Ledger")
        for m, v in self._window.data.ledger.months.items():
            logger.debug(m)
            logger.debug(v)
        logger.debug("\n")

    def _start_timer(self):
        timer = QtCore.QTimer()
        timer.start(500)  # You may change this if you wish.
        timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.
        self.timer = timer
