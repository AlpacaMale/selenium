from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleKeywordScreenshooter:

    def __init__(self, keyword, screenshots_dir, max_page):
        self.driver = webdriver.Chrome()
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir
        self.max_page = max_page
        self.picture_count = 0

    def start(self):
        self.driver.get("https://google.com")
        search_bar = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        for _ in range(self.max_page):
            search_results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "N54PNb"))
            )
            for search_result in search_results:
                search_result.screenshot(
                    f"{self.screenshots_dir}/{self.keyword}-{self.picture_count}.png"
                )
                self.picture_count += 1
            next_button = self.driver.find_element(By.CLASS_NAME, "oeN89d")
            if next_button:
                next_button.click()
            else:
                break

    def finish(self):
        self.driver.quit()


domain_competitors = GoogleKeywordScreenshooter("buy domain", "screenshots", 20)
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenshooter("python book", "screenshots", 20)
python_competitors.start()
python_competitors.finish()
