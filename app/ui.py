from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from datetime import datetime
import itertools
import signal
import pprint

from ui_pyledger import Ui_PyLedger
from ui_add_month import Ui_AddMonth
from ui_new_static import Ui_NewStatic
from ui_new_variable import Ui_NewVariable
from model import Profile, StaticLineItem, VariableLineItem, Ledger, Data, MonthBudget, MonthKey


def date_from_qdatetime(qdt):
    return qdt.toPyDateTime().date()

def month_key_from_date(dt):
    return (dt.year, dt.month)


class ApplicationWindow(QtWidgets.QMainWindow):
    _window_title = "PyMyLedger"

    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.data: Data = None

        self.ui = Ui_PyLedger()
        self.ui.setupUi(self)
        self._set_window_title()

        self.ui.new_month.clicked.connect(self._on_new_month_press)
        self.ui.add_static.clicked.connect(self._on_new_static_press)
        self.ui.add_variable.clicked.connect(self._on_new_variable_press)

        self.static_table = StaticTableManager(self.ui.static_table)
        self.variable_table = VariableTableManager(self.ui.variable_table)

        self.ui.month_select.currentTextChanged.connect(self._on_moth_select)

    def set_data(self, data=None):
        self.data = data or self.data
        self._populate_month_select()
        self._set_window_title()
        self.render()

    def _set_window_title(self):
        if self.data:
            title = self._window_title + " | " + self.data.profile.name
        else:
            title = self._window_title
        self.setWindowTitle(title)        
    
    @property
    def _current_month(self):
        current_month_display = self.ui.month_select.currentText()
        return MonthKey.from_date(self._month_display_as_date(current_month_display))

    def _month_display_as_date(self, month_display):
        return datetime.strptime(month_display, MonthKey.month_format()).date()

    def render(self, month_display=None):
        if month_display:
            print("Got month to render:", month_display)
            month_dt = self._month_display_as_date(month_display)
            month_key = MonthKey.from_date(month_dt)
            static, variable = self.data.static_and_variable(month_key)
            self.variable_table.add_items(variable)
            self.static_table.add_items(static)
            self._balance_calculations()

    def _balance_calculations(self):
        assets, liabilities = self.data.assets_and_liabilities(self._current_month)
        balance = assets - liabilities
        self.ui.assets_text.setText(str(assets))
        self.ui.liabilities_text.setText(str(liabilities))
        self.ui.balance_text.setText(str(balance))

    def _on_new_month_press(self):
        dialog = MonthWindow(self._add_month)
        dialog.open()

    def _add_month(self, date):
        month_key = (date.year, date.month)
        print("adding month:", month_key)
        self.data.add_month(month_key)
        self.set_data()

    def _populate_month_select(self):
        index = self.ui.month_select.currentIndex() if self.ui.month_select.currentText() else None
        self.ui.month_select.clear()
        for key in self.data.months_available:
            month_str = key.display
            print("adding month to select:", month_str)
            self.ui.month_select.addItem(month_str)
        if index:
            self.ui.month_select.setCurrentIndex(index)

    def _on_moth_select(self, month_str):
        self.render(month_str)

    def _on_new_static_press(self):
        dialog = StaticWindow(self._add_static)
        dialog.open()

    def _add_static(self, static):
        self.data.add_static_to_month(self._current_month, static)
        self.set_data()
    
    def _on_new_variable_press(self):
        dialog = VariableWindow(self._add_variable)
        dialog.open()
    
    def _add_variable(self, variable):
        self.data.add_variable_to_month(self._current_month, variable)
        self.set_data()


class MonthWindow(QtWidgets.QDialog):
    def __init__(self, cb):
        super(MonthWindow, self).__init__()

        self.ui = Ui_AddMonth()
        self.ui.setupUi(self)
        now = datetime.now()
        self.ui.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(0, 0, 0)))

        self.callback = cb
        self.ui.buttonBox.clicked.connect(self._on_new_month_select)

    def open(self):
        self.exec()

    def _on_new_month_select(self, *args, **kwargs):
        d = date_from_qdatetime(self.ui.dateEdit.dateTime())
        print("Date selected:", d)
        self.callback(d)

class StaticWindow(QtWidgets.QDialog):
    def __init__(self, cb):
        super(StaticWindow, self).__init__()

        self.ui = Ui_NewStatic()
        self.ui.setupUi(self)

        self.callback = cb
        self.ui.buttonBox.clicked.connect(self._on_submit)

    def open(self):
        self.exec()

    def _on_submit(self, *args, **kwargs):
        name = self.ui.name_text.text()
        amount = int(self.ui.amount_text.text())
        new = StaticLineItem(name, amount)
        self.callback(new)

class VariableWindow(QtWidgets.QDialog):
    def __init__(self, cb):
        super(VariableWindow, self).__init__()

        self.ui = Ui_NewVariable()
        self.ui.setupUi(self)

        self.callback = cb
        self.ui.buttonBox.clicked.connect(self._on_submit)
    
    def open(self):
        self.exec()
    
    def _on_submit(self, *args, **kwargs):
        name = self.ui.name_text.text()
        new = VariableLineItem(name)
        self.callback(new)

class StaticTableManager:
    def __init__(self, static_table):
        self.table = static_table
        self._setup()

    def _setup(self):
        self.table.setColumnCount(3)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(['Name', 'Amount', 'Paid'])
    
    def add_items(self, items: list):
        self.table.setRowCount(len(items))
        for i, s in enumerate(items):
            self._add_item(i, s)

    def _add_item(self, r, item):
        name = QtWidgets.QTableWidgetItem(item.name)
        name.setFlags(name.flags() ^ Qt.ItemIsEditable)

        amt = QtWidgets.QTableWidgetItem(str(item.amount))
        amt.setTextAlignment(Qt.AlignCenter)

        paid = QtWidgets.QCheckBox()
        paid.setCheckState(item.paid)
        paid = self.create_row_widget(paid)
    
        self.table.setItem(r, 0, name)
        self.table.setItem(r, 1, amt)
        self.table.setCellWidget(r, 2, paid)

    @staticmethod
    def create_row_widget(inner_widget):
        w = QtWidgets.QWidget()
        l = QtWidgets.QHBoxLayout(w)
        l.addWidget(inner_widget)
        l.setAlignment(Qt.AlignCenter)
        w.setLayout(l)
        return w


class VariableTableManager:
    def __init__(self, variable_table):
        self.table = variable_table
        self._setup()

    def _setup(self):
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(['Name', 'Amount'])
    
    def add_items(self, items: list):
        self.table.setRowCount(len(items))
        for i, s in enumerate(items):
            name = QtWidgets.QTableWidgetItem(s.name)
            amt = QtWidgets.QTableWidgetItem(str(s.amount))
            amt.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(i, 0, name)
            self.table.setItem(i, 1, amt)