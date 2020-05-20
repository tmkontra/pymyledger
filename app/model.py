from dataclasses import dataclass, field
import datetime
import itertools
import pickle
from typing import List

from copy import deepcopy


@dataclass(frozen=True)
class MonthKey:
    year: int
    month: int

    @classmethod
    def from_date(cls, dt):
        return cls(dt.year, dt.month)

    @property
    def display(self):
        return datetime.datetime(year=self.year, month=self.month, day=1).strftime(self.month_format())

    @classmethod
    def month_format(cls):
        return "%b %Y"

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
class Profile:
    name: str
    static: List[StaticLineItem] = field(default_factory=list)
    variable: List[VariableLineItem] = field(default_factory=list)
    
    @property
    def static_names(self):
        return [s.name for s in self.static]

    @property
    def variable_names(self):
        return [v.name for v in self.variable]

@dataclass
class MonthBudget:
    static: List[StaticLineItem] = field(default_factory=list)
    variable: List[VariableLineItem] = field(default_factory=list)


@dataclass
class Ledger:
    months: dict = field(default_factory=dict)


@dataclass
class Data:
    profile: Profile
    ledger: Ledger

    def add_month(self, month: MonthKey):
        self.ledger.months.setdefault(month, MonthBudget(deepcopy(self.profile.static), deepcopy(self.profile.variable)))
    
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
        else:
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
        if static.name in self.profile.static_names:
            raise ValueError
        else:
            self.profile.static.append(static)
            self.ledger.months[month].static.append(static)

    def add_variable_to_month(self, month, variable):
        if variable.name in self.profile.variable_names:
            raise ValueError
        else:
            self.profile.variable.append(variable)
            self.ledger.months[month].variable.append(variable)

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

    def save(self, fp):
        with open(fp, 'wb') as f:
            pickle.dump(self, f)
    
    @classmethod
    def load(cls, fp):
        with open(fp, 'rb') as f:
            data = pickle.load(f)
        return data
