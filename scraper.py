import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GameScraper:
    def __init__(self, url):
        self.url = url
        # Setup dial Chrome options bach n-banou bhal bnadem mashi bot
        options = uc.ChromeOptions()
        # options.add_argument('--headless') # Khlliha m-commentya f l-lowel bach t-logga
        self.driver = uc.Chrome(options=options)
        self.last_multiplier = 0.0

    def open_game(self):
        print(f"Opening: {self.url}")
        self.driver.get(self.url)
        print("S'il vous plaît, connectez-vous à votre compte 1xbet...")
        # Ghadi n-khlliw 20 tanya bach t-logga o dkhel l-game "Crash"
        time.sleep(20)

    def get_current_multiplier(self):
        try:
            # Had l-selector howa li kiban f l-Inspecteur dial 1xbet Crash
            # Kanshoufou div li fih l-multiplier real-time
            element = self.driver.find_element(By.CLASS_NAME, "crash-game__multiplier-text")
            
            if element:
                txt = element.text.replace('x', '').strip()
                if txt:
                    return float(txt)
            return None
        except Exception:
            # Ila malqach l-element (momkin l-game habsat aw mazal mabdat)
            return None

    def is_game_crashed(self, current_val):
        """
        Hadi logic bach n-detectiw imta tfarqa3at l-tiyara.
        Ila l-multiplier hbas aw rje3 l 'Waiting', ya3ni crashat.
        """
        if current_val is None and self.last_multiplier > 1.0:
            final_val = self.last_multiplier
            self.last_multiplier = 0.0
            return final_val
        
        if current_val:
            self.last_multiplier = current_val
        return None

    def close(self):
        self.driver.quit()
