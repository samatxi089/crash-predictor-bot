import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

class GameScraper:
    def __init__(self, url):
        self.url = url
        self.options = uc.ChromeOptions()
        # self.options.add_argument('--headless') # Ila bghiti l-browser may-ban-sh
        self.driver = uc.Chrome(options=self.options)

    def open_game(self):
        self.driver.get(self.url)
        print("Game opened. Please log in if necessary.")
        time.sleep(10) # Waqt bach t-scani l-page

    def get_current_multiplier(self):
        try:
            # HNA KHASSNA L-SELECTOR DIAL L-SITE (CSS_SELECTOR)
            # Ghadi n-khlliha variable hta t-at-tini l-site li khddam fih
            element = self.driver.find_element(By.CSS_SELECTOR, ".multiplier-value") 
            return float(element.text.replace('x', '').strip())
        except Exception as e:
            return None

    def close(self):
        self.driver.quit()
