from scraper import GameScraper
from logic import GameLogic
import time

def run_bot():
    url = "URL_DIAL_SITE_HNA"
    scraper = GameScraper(url)
    logic = GameLogic()
    
    scraper.open_game()
    
    print("Bot is running...")
    while True:
        val = scraper.get_current_multiplier()
        if val:
            # Fach l-game t-crash (multiplier i-hbas), n-diroh f l-logic
            # (Hna khass n-detectiw imta l-round tsallat)
            print(f"Live Multiplier: {val}x")
            
            # Mital: Chnu hiya l-ihtimaliya dial round t-wsal l 2.0x?
            prob = logic.calculate_probability(2.0)
            print(f"Probability of 2.0x: {prob}%")
            
        time.sleep(0.5)

if __name__ == "__main__":
    run_bot()
