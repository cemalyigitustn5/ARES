import os


def modul_kontrol():

    moduller = {
        "Brain": "core/brain.py",
        "Memory": "memory",
        "Voice": "voice",
        "Vision": "vision",
        "Interface": "ui"
    }

    sonuc = {}

    for isim, yol in moduller.items():

        if os.path.exists(yol):
            sonuc[isim] = True
        else:
            sonuc[isim] = False

    return sonuc


def rapor():

    print("\nModule Scan:\n")

    durumlar = modul_kontrol()

    for isim, durum in durumlar.items():

        if durum:
            print(f"[✓] {isim:<12} detected")
        else:
            print(f"[!] {isim:<12} missing")
