import json
import os
from src.morality import SoulStats

SAVE_FILE = "savegame.json"

def save_game(stats: SoulStats):
    """Saves the current SoulStats to a JSON file."""
    try:
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(stats.to_dict(), f, indent=4)
        return True
    except Exception as e:
        print(f"Kayıt hatası: {e}")
        return False

def load_game() -> SoulStats:
    """Loads SoulStats from the JSON file if it exists."""
    if not os.path.exists(SAVE_FILE):
        return None
    
    try:
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return SoulStats.from_dict(data)
    except Exception as e:
        print(f"Yükleme hatası: {e}")
        return None

def has_save_file() -> bool:
    return os.path.exists(SAVE_FILE)
