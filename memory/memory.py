import json
import os

DOSYA = "data/memory.json"

def yukle():
    if not os.path.exists(DOSYA):
        return {}

    try:
        with open(DOSYA, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def kaydet(veri):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veri, f, indent=4, ensure_ascii=False)