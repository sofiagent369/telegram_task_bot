import datetime

def format_date(date: datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M")