from memory.profile import bilgi_kaydet, bilgi_getir
from core.personality import AresPersonality
from memory.memory import yukle, kaydet
from modules.system import sistem_komutu

from commands.time import saat, tarih
from commands.system_info import sistem


ares = AresPersonality()


def cevap_ver(komut):
    komut = komut.lower().strip()
    hafiza = yukle()

    # Sistem komutları
    cevap = sistem_komutu(komut)
    if cevap:
        return cevap


    # ARES kimlik
    if "sen kimsin" in komut or "kendini tanıt" in komut:
        return ares.tanit()


    # İsim kaydetme
    if komut.startswith("adım "):
        isim = komut.replace("adım ", "")
        hafiza["isim"] = isim
        kaydet(hafiza)

        return f"Memnun oldum {isim}. Seni hafızama kaydettim."


    # Kullanıcı kim
    if "ben kimim" in komut:
        isim = hafiza.get("isim")

        if isim:
            return f"Sen {isim}. Benim geliştiricimsin."

        return "Henüz seni tanımıyorum."

    # Yeni bilgi kaydetme
    if komut.startswith("hatırla "):
        veri = komut.replace("hatırla ", "")

        if " " in veri:
            konu, bilgi = veri.split(" ", 1)

            bilgi_kaydet(konu, bilgi)

            return f"{konu} bilgisini hafızama aldım."


    # Hafızadan bilgi çağırma
    if komut.startswith("neydi "):
        konu = komut.replace("neydi ", "")

        bilgi = bilgi_getir(konu)

        if bilgi:
            return f"{konu}: {bilgi}"

        return "Bu bilgiyi hafızamda bulamadım."



















    # Selamlaşma
    if komut == "merhaba" or komut == "selam":
        isim = hafiza.get("isim")

        if isim:
            return f"Merhaba {isim}. Sistemler hazır."

        return "Merhaba. Ben ARES."


    # Saat
    if "saat" in komut:
        return f"Saat şu anda {saat()}."


    # Tarih
    if "tarih" in komut:
        return f"Bugünün tarihi {tarih()}."


    # Sistem bilgisi
    if "bilgisayar" in komut or "sistem" in komut:
        return sistem()


    return "Bu komutu henüz öğrenmedim."
