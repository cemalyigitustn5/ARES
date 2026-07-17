from memory.memory import yukle, kaydet


def bilgi_kaydet(konu, bilgi):
    hafiza = yukle()

    if "bilgiler" not in hafiza:
        hafiza["bilgiler"] = {}

    hafiza["bilgiler"][konu] = bilgi

    kaydet(hafiza)

    return True


def bilgi_getir(konu):
    hafiza = yukle()

    bilgiler = hafiza.get("bilgiler", {})

    return bilgiler.get(konu)
