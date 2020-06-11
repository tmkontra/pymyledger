from .base import BaseSerializer

from ..model import (
    Data,
    Ledger,
    MonthBudget,
    MonthKey,
    StaticLineItem,
    VariableLineItem,
)


class SerializerV0(BaseSerializer):
    _version = 0

    @classmethod
    def serialize_data(cls, data):
        return {
            "application": "PyMyLedger",
            "version": cls._version,
            "ledger": cls.serialize_ledger(data.ledger),
        }

    @classmethod
    def serialize_ledger(cls, ledger):
        return {
            "months": {
                cls.serialize_month_key(k): cls.serialize_month_budget(m)
                for (k, m) in ledger.months.items()
            }
        }

    @classmethod
    def serialize_month_key(cls, month_key):
        return f"{month_key.year}-{month_key.month}"

    @classmethod
    def serialize_month_budget(cls, month):
        return {
            "static": [cls.serialize_static(i) for i in month.static],
            "variable": [cls.serialize_variable(i) for i in month.variable],
        }

    @classmethod
    def serialize_variable(cls, variable):
        return {"name": variable.name, "amount": variable.amount}

    @classmethod
    def serialize_static(cls, static):
        return {"name": static.name, "amount": static.amount, "paid": static.paid}

    @classmethod
    def deserialize_data(cls, json):
        months = json["ledger"]["months"]
        return Data(
            Ledger(
                months={
                    cls.deserialize_month_key(k): cls.deserialize_month(m)
                    for (k, m) in months.items()
                }
            )
        )

    @classmethod
    def deserialize_month_key(cls, month_key):
        y, m = month_key.split("-")
        return MonthKey(int(y), int(m))

    @classmethod
    def deserialize_month(cls, month):
        st = month["static"]
        vr = month["variable"]
        return MonthBudget(
            [Static(s["name"], s["amount"], s["paid"]) for s in st],
            [VariableLineItem(s["name"], s["amount"]) for v in vr],
        )
