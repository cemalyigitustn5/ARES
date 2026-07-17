from memory.memory import yukle, kaydet
from core.personality import AresPersonality

from commands.time import saat, tarih
from commands.system_info import sistem


ares = AresPersonality()


def cevap_ver(komut):

    komut = komut.lower()
    hafiza = yukle()


    # Sistem komutları
    if "saat" in komut:
        return f"Saat {saat()}"

    if "tarih" in komut:
        return f"Bugünün tarihi {tarih()}"


    if "bilgisayar" in komut or "sistem" in komut:
        return sistem()


    # Hafıza
    if komut.startswith("adım "):
        isim = komut.replace("adım ", "")
        hafiza["isim"] = isim
        kaydet(hafiza)

        return f"Memnun oldum {isim}."


    if komut == "ben kimim":
        return hafiza.get(
            "isim",
            "Henüz adını bilmiyorum."
        )


    # Kişilik
    if komut == "sen kimsin":
        return ares.tanit()


    if komut == "merhaba":
        return "Merhaba Cemal."


    return "Bu komutu henüz bilmiyorum."
