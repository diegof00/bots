from selenium import webdriver
from time import sleep

class OneBot:
    def __init__(self, search):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com")
        self.driver.switch_to.frame('gsft_main')
        sleep(2)
        searchBox = self.driver.find_element_by_xpath("//*[@id=\"search\"]").send_keys(search)
        sleep(2)
        searchBox.send_keys(search)


OneBot('cats')