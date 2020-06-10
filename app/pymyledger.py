from datetime import datetime
import signal
from PyQt5 import QtWidgets, QtCore

from ui import ApplicationWindow, MonthWindow

from cache import Cache
from model import Data, Ledger, MonthKey

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
            try:
                data = Data.load(last_open)
            except:
                data = None
        else:
            data = None

        self._window: ApplicationWindow = ApplicationWindow()
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
            self._window._on_new_month_press("Please Select A Month To Start:")

    def on_shutdown(self):
        lo = self._window.save_load.last_opened
        if lo:
            print("caching last file location")
            self.cache.update("last_opened", lo)
            self.cache.flush()

    @property
    def default_data(self):
        print("initializing data...")
        data = Data(Ledger())
        return data

    def _register_signal_handlers(self):
        signal.signal(signal.SIGINT, self.sigint_handler)
        signal.signal(signal.SIGQUIT, self.sigquit_handler)

    @staticmethod
    def sigint_handler(*args):
        """Handler for the SIGINT signal."""
        print("Goodbye!")
        QtWidgets.QApplication.quit()

    def sigquit_handler(self, *args):
        print("\n")
        print("Profile")
        print(self._window.data.profile.__dict__)
        print("Ledger")
        for m, v in self._window.data.ledger.months.items():
            print(m)
            print(v)
        print("\n")

    def _start_timer(self):
        timer = QtCore.QTimer()
        timer.start(500)  # You may change this if you wish.
        timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.
        self.timer = timer
