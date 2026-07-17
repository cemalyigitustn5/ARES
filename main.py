import time

from ui.window import baslat
from core.system_check import modul_kontrol


def ares_boot():

    print("""
===============================
        ARES CORE v0.4
===============================

Initializing system...
""")

    time.sleep(1)

    durumlar = modul_kontrol()

    for isim, durum in durumlar.items():

        if durum:
            print(f"[✓] {isim:<12} ONLINE")
        else:
            print(f"[!] {isim:<12} OFFLINE")

        time.sleep(0.3)


    print("""
-------------------------------

Identity:
Cemal

ARES hazır.

Launching interface...

-------------------------------
""")

    time.sleep(2)



if __name__ == "__main__":
    ares_boot()
    baslat()
