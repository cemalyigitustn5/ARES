class AresPersonality:

    def __init__(self):
        self.name = "ARES"
        self.creator = "Cemal Yiğit Üstün"
        self.version = "0.5"


    def tanit(self):
        return (
            f"Ben {self.name}. "
            f"{self.version} çekirdek sürümüyle çalışıyorum. "
            f"Geliştiricim {self.creator}."
        )


    def durum(self):
        return (
            "Tüm ana sistemler kontrol altında. "
            "Göreve hazırım."
        )


    def selam(self):
        return (
            f"Merhaba {self.creator}. "
            "ARES aktif."
        )
