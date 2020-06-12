from dataclasses import dataclass, field
import datetime
import itertools
from typing import List, Mapping


@dataclass(frozen=True)
class MonthKey:
    year: int
    month: int

    @classmethod
    def from_date(cls, dt):
        return cls(dt.year, dt.month)

    @property
    def display(self):
        return datetime.datetime(year=self.year, month=self.month, day=1).strftime(
            self.month_format()
        )

    @classmethod
    def month_format(cls):
        return "%b %Y"

    @property
    def prev(self):
        if self.month > 1:
            return MonthKey(self.year, self.month - 1)
        return MonthKey(self.year - 1, 12)


@dataclass
class LineItem:
    name: str
    amount: float = 0


@dataclass
class StaticLineItem(LineItem):
    paid: bool = False


@dataclass
class VariableLineItem(LineItem):
    pass


@dataclass
class MonthBudget:
    static: List[StaticLineItem] = field(default_factory=list)
    variable: List[VariableLineItem] = field(default_factory=list)


@dataclass
class Ledger:
    months: Mapping[MonthKey, MonthBudget] = field(default_factory=dict)


@dataclass
class Data:
    ledger: Ledger

    def add_month(self, month: MonthKey):
        static, variable = self.static_and_variable(month.prev)
        self.ledger.months.setdefault(
            month,
            MonthBudget(
                [StaticLineItem(s.name, s.amount) for s in static],
                [VariableLineItem(v.name) for v in variable]
            ),
        )

    def assets_and_liabilities(self, month: MonthKey):
        budget = self.ledger.months.get(month)
        if budget:
            assets = liabilities = 0
            for i in itertools.chain(budget.static, budget.variable):
                if i.amount > 0:
                    assets += i.amount
                if i.amount < 0:
                    liabilities -= i.amount
            return assets, liabilities
        return None

    def static_and_variable(self, month: MonthKey):
        budget = self.ledger.months.get(month)
        if budget:
            variable = budget.variable
            static = budget.static
        else:
            static = variable = []
        return static, variable

    @property
    def months_available(self):
        months = list(self.ledger.months.keys())
        if months:
            months.sort(key=lambda x: (-x.year, -x.month))
            return months
        return []

    def add_static_to_month(self, month, static):
        static_list, _ = self.static_and_variable(month)
        if static.name in static_list:
            raise ValueError("%s already exists" % static.name)
        static_list.append(static)

    def add_variable_to_month(self, month, variable):
        _, variable_list = self.static_and_variable(month)
        if variable.name in variable_list:
            raise ValueError("%s already exists" % variable.name)
        variable_list.append(variable)

    def update_variable(self, month, name, amount=None):
        if amount:
            variable = self.ledger.months[month].variable
            for var in variable:
                if var.name == name:
                    var.amount = amount

    def get_variable(self, month, name):
        variable = self.ledger.months[month].variable
        for var in variable:
            if var.name == name:
                return var
        return None

    def update_static(self, month, name, amount=None, paid=None):
        static = self.ledger.months[month].static
        for stat in static:
            if stat.name == name:
                stat.amount = amount or stat.amount
                stat.paid = paid if paid is not None else stat.paid

    def get_static(self, month, name):
        static = self.ledger.months[month].static
        for stat in static:
            if stat.name == name:
                return stat
        return None
