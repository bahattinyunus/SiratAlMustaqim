import sys
import time
import os
from src.morality import MoralityEngine
from src.world import WorldGenerator

from src.persistence import save_game, load_game, has_save_file

# Try to import colorama, handle if missing
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class MockColor:
        def __getattr__(self, name): return ""
    Fore = MockColor()
    Style = MockColor()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + "=== SIRAT-I MÜSTAKİM: ETİK YAŞAM SİMÜLASYONU ===")
    print("1. Yeni Hayat Başlat")
    if has_save_file():
        print("2. Önceki Hayata Devam Et")
    print("3. Çıkış")
    return input(Fore.CYAN + "\nSeçiminiz: ")

def main():
    while True:
        choice = main_menu()
        
        engine = None
        
        if choice == "1":
            engine = MoralityEngine()
            print(Fore.YELLOW + "Yeni bir sayfa açılıyor...")
            time.sleep(1)
        elif choice == "2" and has_save_file():
            stats = load_game()
            if stats:
                engine = MoralityEngine()
                engine.stats = stats
                print(Fore.GREEN + "Geçmiş hatırlandı. Hayat kaldığı yerden devam ediyor...")
                time.sleep(1)
            else:
                print(Fore.RED + "Kayıt dosyası okunamadı!")
                continue
        elif choice == "3":
            print("Allah'a emanet olun.")
            break
        else:
            continue
            
        # Game Loop
        game_loop(engine)

def game_loop(engine):
    world = WorldGenerator()
    turn = 1
    max_turns = 10 

    while turn <= max_turns and engine.stats.iman > 0:
        print(Fore.YELLOW + f"\n--- Oruç/Gün {turn} ---")
        print(engine.get_status_report())
        
        scenario = world.generate_event()
        print(Fore.WHITE + Style.BRIGHT + f"\nSENARYO: {scenario.description}")
        
        for i, choice in enumerate(scenario.choices):
            print(f"{i + 1}. {choice}")
        print(f"{len(scenario.choices) + 1} . Kaydet ve Çık")
            
        try:
            user_input = input(Fore.CYAN + "\nSeçiminiz: ")
            
            # Save & Exit Check
            if user_input == str(len(scenario.choices) + 1):
                if save_game(engine.stats):
                    print(Fore.GREEN + "İlerlemeniz kaydedildi. Görüşmek üzere...")
                else:
                    print(Fore.RED + "Kayıt başarısız!")
                return # Exit to main menu

            idx = int(user_input) - 1
            
            if 0 <= idx < len(scenario.choices):
                choice_text = scenario.choices[idx]
                impact_type, magnitude = scenario.impacts[idx]
                
                print(Fore.MAGENTA + "Sonuçlar işleniyor...")
                time.sleep(1)
                
                result_msg = engine.process_deed(choice_text, impact_type, magnitude)
                print(result_msg)
            else:
                print(Fore.RED + "Geçersiz seçim!")
        except ValueError:
            print(Fore.RED + "Geçersiz giriş!")
            
        turn += 1
        time.sleep(1.5)

    if engine.stats.iman <= 0:
        print(Fore.RED + "\nİman tükendi. Oyun Bitti.")
    else:
        print(Fore.GREEN + "\n\n=== EBEDİ HESAP VAKTİ ===")
        print(engine.get_status_report())
    
    input(Fore.WHITE + "Ana menüye dönmek için Enter'a bas...")


if __name__ == "__main__":
    main()
