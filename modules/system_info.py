import platform
import psutil


def sistem_bilgisi():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory()
    ram_yuzde = ram.percent

    disk = psutil.disk_usage("/")
    disk_yuzde = disk.percent

    sistem = platform.system()

    return f"""
ARES Sistem Raporu:

İşletim Sistemi: {sistem}

CPU Kullanımı: %{cpu}

RAM Kullanımı: %{ram_yuzde}

Disk Kullanımı: %{disk_yuzde}

Durum: Stabil
"""
