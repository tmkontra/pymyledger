def date_from_qdatetime(qdt):
    return qdt.toPyDateTime().date()


def month_key_from_date(dt):
    return (dt.year, dt.month)
