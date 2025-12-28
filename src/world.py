import random
from dataclasses import dataclass
from src.morality import DeedType

@dataclass
class Scenario:
    description: str
    choices: list
    impacts: list  # List of tuples (DeedType, magnitude) corresponding to choices

class WorldGenerator:
    def __init__(self):
        self.scenarios = [
            Scenario(
                "Yolda içinde 500 TL olan bir cüzdan buldun.",
                ["Polise teslim et", "Sessizce cebe indir", "Öylece bırak"],
                [
                    (DeedType.SAWAB, 20),
                    (DeedType.GUNAH, 50),
                    (DeedType.NEUTRAL, 0)
                ]
            ),
            Scenario(
                "Bir arkadaşın, ortak bir tanıdığınız hakkında gıybet yapmaya başladı.",
                ["Konuyu nazikçe değiştir", "Katıl ve detay ekle", "Sessizce dinle"],
                [
                    (DeedType.SAWAB, 15),
                    (DeedType.GUNAH, 30),
                    (DeedType.GUNAH, 10) # Gıybeti dinlemek de sıkıntılıdır
                ]
            ),
            Scenario(
                "Bakkalda kasiyer sana yanlışlıkla 100 TL fazla para üstü verdi.",
                ["Kasiyeri uyar ve parayı iade et", "Mutlu bir şekilde uzaklaş"],
                [
                    (DeedType.SAWAB, 25),
                    (DeedType.GUNAH, 25)
                ]
            ),
             Scenario(
                "Vakit namazı girdi ama eğlenceli bir oyunun tam ortasındasın.",
                ["Oyunu durdur ve hemen kıl", "Son dakikaya kadar ertele", "Kazaya bırak (Kılma)"],
                [
                    (DeedType.SAWAB, 50),
                    (DeedType.GUNAH, 10),
                    (DeedType.GUNAH, 100)
                ]
            ),
            Scenario(
                "İş yerinde yöneticin, sevmediğin bir çalışma arkadaşına mobbing (psikolojik baskı) uyguluyor.",
                ["Arkadaşını savun ve yöneticiye karşı çık", "Sessiz kalıp işine bak", "Yöneticiye katılıp gözüne girmeye çalış"],
                [
                    (DeedType.SAWAB, 40),      # Cesurca hakkı savunmak
                    (DeedType.GUNAH, 20),      # Haksızlık karşısında susmak (Dilsiz Şeytan)
                    (DeedType.GUNAH, 60)       # Zulme ortak olmak
                ]
            ),
            Scenario(
                "Soğuk bir kış günü sokakta titreyen bir kedi gördün.",
                ["Montunu çıkarıp ona sar ve mama al", "Başını okşayıp geç", "Görmezden gel"],
                [
                    (DeedType.SAWAB, 30),
                    (DeedType.SAWAB, 5),
                    (DeedType.NEUTRAL, 0)
                ]
            ),
            Scenario(
                "Borsada çok hızlı kazandıracağı söylenen bir 'Coin' var, ama projesi belirsiz (kumar şüphesi var).",
                ["Asla bulaşma, helal ve sağlam yatırım yap", "Az bir miktar yatırıp dene", "Varını yoğunu bas"],
                [
                    (DeedType.SAWAB, 20),      # Şüpheli şeylerden kaçınmak
                    (DeedType.GUNAH, 15),      # Şüpheye dalmak
                    (DeedType.GUNAH, 50)       # Kumara girmek
                ]
            ),
            Scenario(
                "Uzun zamandır aramadığın yaşlı bir akraban aklına geldi (Sıla-i Rahim).",
                ["Hemen ara ve halini hatırını sor", "Müsait bir zamanda ararım de (ertele)", "Aramaya gerek yok"],
                [
                    (DeedType.SAWAB, 35),
                    (DeedType.GUNAH, 10),      # Ertelemek çoğu zaman terk etmektir
                    (DeedType.GUNAH, 40)       # Akrabalık bağını kesmek
                ]
            ),
            Scenario(
                "Sosyal medyada bir kişi haksız yere linç ediliyor, herkes ona hakaret ediyor.",
                ["'Zan ile hareket etmeyin' diye uyar", "Sen de bir hakaret yazıp beğenilme kas", "Sadece izle"],
                [
                    (DeedType.SAWAB, 45),
                    (DeedType.GUNAH, 70),      # Kul hakkı ve iftira
                    (DeedType.GUNAH, 10)       # Kötülüğe seyirci kalmak
                ]
            )
        ]

    def generate_event(self):
        return random.choice(self.scenarios)
