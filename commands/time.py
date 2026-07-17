import datetime


def saat():
    return datetime.datetime.now().strftime("%H:%M")


def tarih():
    return datetime.datetime.now().strftime("%d.%m.%Y")

