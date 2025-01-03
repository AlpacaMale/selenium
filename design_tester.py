from math import ceil
import time
from selenium import webdriver
import os


class ResponsiveTester:
    def __init__(self, urls):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.urls = urls
        self.sizes = [480, 960, 1366, 1920]

    def screenshot(self, url):
        BROWSER_HEIGHT = 1048
        dir_name = url.replace("https://", "").split(".")[0]
        os.mkdir(f"screenshots/{dir_name}")
        self.driver.get(url)
        for size in self.sizes:
            self.driver.set_window_size(size, BROWSER_HEIGHT)
            time.sleep(3)
            scroll_size = self.driver.execute_script(
                "return document.body.scrollHeight"
            )
            total_sectoins = ceil(scroll_size / BROWSER_HEIGHT)
            for section in range(total_sectoins):
                self.driver.execute_script(
                    f"window.scrollTo(0,{(section)*BROWSER_HEIGHT})"
                )
                self.driver.save_screenshot(
                    f"screenshots/{dir_name}/{size}-{section+1}.png"
                )
                time.sleep(2)

    def start(self):
        for url in self.urls:
            self.screenshot(url)

    def finish(self):
        self.driver.quit()


urls = ["https://nomadcoders.co", "https://wikidocs.net/book/1"]
responsive_tester = ResponsiveTester(urls)
responsive_tester.start()
