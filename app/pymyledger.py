from datetime import datetime
import signal
from PyQt5 import QtWidgets, QtCore

from ui import ApplicationWindow

from model import Data, Profile, Ledger, MonthKey

class PyMyLedger:
    _default_profile_name = "My Profile"

    def __init__(self, args=None, **kwargs):
        args = args or []
        self._qt: QtWidgets.QApplication = QtWidgets.QApplication(args)
        self._qt.setApplicationDisplayName("PyMyLedger")
        self._window: ApplicationWindow = ApplicationWindow()
        data = kwargs.get("data")
        self._set_data(data)
        self._register_signal_handlers()
        self._start_timer()
        self._window.show()
        self._qt.exec()

    def _set_data(self, data=None):
        if data is None:
            data = self.default_data
        self._window.set_data(data)

    @property
    def default_data(self):
        print("initializing data...")
        data = Data(Profile(self._default_profile_name), Ledger())
        data.add_month(MonthKey.from_date(datetime.now()))
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
