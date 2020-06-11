from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from datetime import datetime
import pprint

from ..model import (
    StaticLineItem,
    VariableLineItem,
    Ledger,
    Data,
    MonthBudget,
    MonthKey,
)
from .gen.ui_pyledger import Ui_PyLedger
from .month_window import MonthWindow
from .save_load import SaveLoad
from .static_window import StaticWindow
from .variable_window import VariableWindow


class ApplicationWindow(QtWidgets.QMainWindow):
    _window_title = "PyMyLedger"

    def __init__(self, save_func):
        super(ApplicationWindow, self).__init__()

        self.data: Data = None

        self.ui = Ui_PyLedger()
        self.ui.setupUi(self)
        self._set_window_title()

        self.save_load = SaveLoad(self, save_func)

        self.ui.new_month.clicked.connect(self._on_new_month_press)
        self.ui.add_static.clicked.connect(self._on_new_static_press)
        self.ui.add_variable.clicked.connect(self._on_new_variable_press)

        self.static_table = StaticTableManager(
            self.ui.static_table, self._on_static_check_state_change
        )
        self.variable_table = VariableTableManager(self.ui.variable_table)

        self.ui.month_select.currentTextChanged.connect(self._load_month)

        self.ui.static_table.cellChanged.connect(self._on_static_cell_change)
        self.ui.variable_table.cellChanged.connect(self._on_variable_cell_change)

    def set_data(self, data=None):
        self.data: Data = data or self.data
        self._populate_month_select()
        self._set_window_title()
        self._load_month()

    def _set_window_title(self):
        if self.data:
            title = self._window_title + " | " + "PROFILE"
        else:
            title = self._window_title
        self.setWindowTitle(title)

    @property
    def _current_month(self):
        current_month_display = self.ui.month_select.currentText()
        if current_month_display:
            key = MonthKey.from_date(self._month_display_as_date(current_month_display))
            return key
        return None

    def _month_display_as_date(self, month_display):
        return datetime.strptime(month_display, MonthKey.month_format()).date()

    def _load_month(self, *args):
        month_key = self._current_month
        if month_key:
            static, variable = self.data.static_and_variable(month_key)
            self.variable_table.add_items(variable)
            self.static_table.add_items(static)
            self._balance_calculations(month_key)

    def _balance_calculations(self, month):
        assets, liabilities = self.data.assets_and_liabilities(month)
        balance = assets - liabilities
        self.ui.assets_text.setText(str(assets))
        self.ui.liabilities_text.setText(str(liabilities))
        self.ui.balance_text.setText(str(balance))

    def _on_new_month_press(self, instruction=None):
        dialog = MonthWindow(self._add_month, instruction)
        dialog.open()

    def _add_month(self, date):
        month_key = MonthKey.from_date(date)
        print("adding month:", month_key)
        self.data.add_month(month_key)
        self.set_data()

    def _populate_month_select(self):
        print("populating month select")
        index = (
            self.ui.month_select.currentIndex()
            if self.ui.month_select.currentText()
            else None
        )
        print("index", index)
        print("clearing month select")
        self.ui.month_select.clear()
        print("adding months")
        for key in self.data.months_available:
            print("got key", key)
            month_str = key.display
            print("adding month to select:", month_str)
            self.ui.month_select.addItem(month_str)
        if index is None:
            index = 0
        print("setting month index", index)
        self.ui.month_select.setCurrentIndex(index)

    def _on_new_static_press(self):
        dialog = StaticWindow(self._add_static)
        dialog.open()

    def _add_static(self, dialog: QtWidgets.QDialog):
        c = lambda: self._current_month

        def try_add_variable(static):
            try:
                self.data.add_static_to_month(c(), static)
            except ValueError:
                dialog.close()
                self._error_message("Cannot add duplicate item name!")
            self._load_month()

        return try_add_variable

    def _error_message(self, message):
        err = QtWidgets.QErrorMessage()
        err.showMessage(message)
        err.exec()

    def _on_new_variable_press(self):
        dialog = VariableWindow(self._add_variable)
        dialog.setFocus()
        dialog.open()

    def _add_variable(self, dialog: QtWidgets.QDialog):
        c = lambda: self._current_month

        def try_add_variable(variable):
            try:
                self.data.add_variable_to_month(c(), variable)
            except ValueError:
                dialog.close()
                self._error_message("Cannot add duplicate item name!")
            self._load_month()

        return try_add_variable

    def _on_static_cell_change(self, row, column):
        if column == 1:
            item_name = self.ui.static_table.item(row, 0).text()
            updatedValue = self.ui.static_table.item(row, column).text()
            self.data.update_static(
                self._current_month, item_name, amount=int(updatedValue)
            )

    def _on_static_check_state_change(self, item_name):
        c = lambda: self._current_month

        def change_state(check_state):
            new_state = bool(check_state)
            print(f"changing paid {item_name} to", new_state)
            self.data.update_static(c(), item_name, paid=new_state)

        return change_state

    def _on_variable_cell_change(self, row, column):
        if column == 1:
            item_name = self.ui.variable_table.item(row, 0).text()
            updated_value = self.ui.variable_table.item(row, column).text()
            if updated_value:
                try:
                    new_val = int(updated_value)
                    self.data.update_variable(
                        self._current_month, item_name, amount=new_val
                    )
                except ValueError as e:
                    item = self.data.get_variable(self._current_month, item_name)
                    self.ui.variable_table.item(row, column).setText(str(item.amount))
                    self._error_message("Amount must be an integer!")


class StaticTableManager:
    def __init__(self, static_table, check_callback):
        self.table = static_table
        self.check_callback = check_callback
        self._setup()

    def _setup(self):
        self.table.setColumnCount(3)
        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )
        self.table.setHorizontalHeaderLabels(["Name", "Amount", "Paid"])

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
        paid.stateChanged.connect(self.check_callback(item.name))
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
        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )
        self.table.setHorizontalHeaderLabels(["Name", "Amount"])

    def add_items(self, items: list):
        self.table.setRowCount(len(items))
        for i, s in enumerate(items):
            name = QtWidgets.QTableWidgetItem(s.name)
            name.setFlags(name.flags() ^ Qt.ItemIsEditable)
            amt = QtWidgets.QTableWidgetItem(str(s.amount))
            amt.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(i, 0, name)
            self.table.setItem(i, 1, amt)
