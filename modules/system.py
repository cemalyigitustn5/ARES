import subprocess
import platform

def sistem_komutu(komut):
    sistem = platform.system()

    if sistem == "Linux":

        if komut == "terminal aç":
            subprocess.Popen(["gnome-terminal"])
            return "Terminal açılıyor."

        elif komut == "dosyalar":
            subprocess.Popen(["nautilus"])
            return "Dosyalar açılıyor."

    return None