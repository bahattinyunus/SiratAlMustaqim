from dataclasses import dataclass
from enum import Enum, auto

class DeedType(Enum):
    SAWAB = auto()  # Good Deed (Reward)
    GUNAH = auto()  # Sin (Punishment)
    NEUTRAL = auto()

@dataclass
class SoulStats:
    iman: int = 50        # Faith: 0-100
    nafs: int = 50        # Ego/Desire: 0-100 (Lower is better)
    peace: int = 50       # Inner Peace: 0-100
    book_of_deeds: int = 0 # Net score

    def to_dict(self):
        return {
            "iman": self.iman,
            "nafs": self.nafs,
            "peace": self.peace,
            "book_of_deeds": self.book_of_deeds
        }

    @staticmethod
    def from_dict(data):
        return SoulStats(
            iman=data.get("iman", 50),
            nafs=data.get("nafs", 50),
            peace=data.get("peace", 50),
            book_of_deeds=data.get("book_of_deeds", 0)
        )

class MoralityEngine:
    def __init__(self):
        self.stats = SoulStats()

    def process_deed(self, name: str, deed_type: DeedType, magnitude: int):
        """
        Calculates the impact of a deed on the soul.
        """
        if deed_type == DeedType.SAWAB:
            self.stats.book_of_deeds += magnitude
            self.stats.iman = min(100, self.stats.iman + (magnitude // 2))
            self.stats.nafs = max(0, self.stats.nafs - (magnitude // 3))
            self.stats.peace = min(100, self.stats.peace + (magnitude // 4))
            return f"🌟 Elhamdülillah! Güzel bir amel işlendi: {name} (+{magnitude})"
        
        elif deed_type == DeedType.GUNAH:
            self.stats.book_of_deeds -= magnitude
            self.stats.iman = max(0, self.stats.iman - (magnitude // 2))
            self.stats.nafs = min(100, self.stats.nafs + (magnitude // 2))
            self.stats.peace = max(0, self.stats.peace - (magnitude // 2))
            return f"🌑 Estağfirullah. Bir günah işlendi: {name} (-{magnitude})"
        
        return "Nötr eylem gerçekleşti."

    def get_status_report(self):
        status = "SAĞLIKLI" if self.stats.iman > 70 else "ZAYIF" if self.stats.iman > 30 else "KRİTİK"
        return f"""
        === RUH DURUMU ===
        İman (İnanç):  {self._bar(self.stats.iman)} ({self.stats.iman}%) [{status}]
        Nefs (Ego):    {self._bar(self.stats.nafs, inverse=True)} ({self.stats.nafs}%)
        Huzur:         {self._bar(self.stats.peace)} ({self.stats.peace}%)
        Amel Defteri:  {self.stats.book_of_deeds}
        ==================
        """

    def _bar(self, value, length=10, inverse=False):
        filled = int(value / 100 * length)
        if inverse:
            # For Nafts (lower is better), empty holds the value
            return "▓" * filled + "░" * (length - filled) 
        return "▓" * filled + "░" * (length - filled)
