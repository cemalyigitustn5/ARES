from memory.memory import yukle, kaydet
from modules.system import sistem_komutu

def cevap_ver(komut):
    komut = komut.lower()
    hafiza = yukle()

    cevap = sistem_komutu(komut)
    if cevap:
        return cevap

    if komut.startswith("adım "):
        isim = komut.replace("adım ", "")
        hafiza["isim"] = isim
        kaydet(hafiza)
        return f"Memnun oldum {isim}."

    if komut == "ben kimim":
        return hafiza.get("isim", "Henüz adını bilmiyorum.")

    if komut == "merhaba":
        return "Merhaba!"

    return "Bu komutu henüz bilmiyorum."