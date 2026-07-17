import subprocess


def program_ac(komut):

    komut = komut.lower()


    if "hesap" in komut:
        subprocess.Popen(["gnome-calculator"])
        return "Hesap makinesi açılıyor."


    if "terminal" in komut:
        subprocess.Popen(["gnome-terminal"])
        return "Terminal açılıyor."


    if "dosya" in komut:
        subprocess.Popen(["nautilus"])
        return "Dosya yöneticisi açılıyor."


    if "firefox" in komut:
        subprocess.Popen(["firefox"])
        return "Firefox açılıyor."


    return None
