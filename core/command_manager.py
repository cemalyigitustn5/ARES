from modules.system_info import sistem_bilgisi
from modules.system import sistem_komutu
from datetime import datetime


def komut_kontrol(komut, hafiza):

    cevap = sistem_komutu(komut)

    if cevap:
        return cevap


    if komut == "sen kimsin":
        return (
            "Ben ARES. "
            "0.6 çekirdek sürümüyle çalışıyorum. "
            "Geliştiricim Cemal Yiğit Üstün."
        )


    if komut.startswith("adım "):
        isim = komut.replace("adım ", "")
        hafiza["isim"] = isim
        return f"Memnun oldum {isim}."


    if komut == "ben kimim":
        return hafiza.get(
            "isim",
            "Henüz adını bilmiyorum."
        )


    if komut == "saat kaç":
        saat = datetime.now().strftime("%H:%M")
        return f"Saat şu anda {saat}."


    if komut == "tarih ne":
        tarih = datetime.now().strftime("%d.%m.%Y")
        return f"Bugünün tarihi {tarih}."


    if komut == "merhaba":
        return "Merhaba Cemal."



    if komut == "sistem durumu":
        return sistem_bilgisi()

    return None
