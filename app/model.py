from dataclasses import dataclass, field
import datetime
import itertools
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

@dataclass
class MonthBudget:
    static: List[StaticLineItem] = field(default_factory=list)
    variable: List[VariableLineItem] = field(default_factory=list)


my_static = [
    StaticLineItem("Rent", -1975),
    StaticLineItem("Student Loan", -450),
    StaticLineItem("VW Lease", -360),
    StaticLineItem("Utilities", -120),
    StaticLineItem("Paycheck", 6000)
]

my_variable = [
    VariableLineItem("Freedom Unlimited"),
    VariableLineItem("Sapphire"),
    VariableLineItem("United"),
    VariableLineItem("Amazon"),
    VariableLineItem("Citi AA"),
]

my_profile = Profile("Tyler", my_static, my_variable)


@dataclass
class Ledger:
    months: dict = field(default_factory=dict)


my_ledger = Ledger(
    {
        (2020, 1): MonthBudget(
            deepcopy(my_static), 
            [VariableLineItem(v.name, -120) for v in my_variable]
        )
    }
)

@dataclass
class Data:
    profile: Profile
    ledger: Ledger

    def add_month(self, month: MonthKey):
        self.ledger.months.setdefault(month, MonthBudget(self.profile.static, self.profile.variable))
    
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
        print("sorting months:", months)
        if months:
            months.sort(key=lambda x: (-x.year, -x.month))
            return months
        return []

    def add_static_to_month(month, static):
        self.ledger.months[month].static.append(static)

    def add_variable_to_month(month, variable):
        self.ledger.months[month].variable.append(variable)




my_data = Data(deepcopy(my_profile), deepcopy(my_ledger))