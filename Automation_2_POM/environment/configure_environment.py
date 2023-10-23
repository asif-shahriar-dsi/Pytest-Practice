from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Setup:

    def __init__(self):
        self.driver = webdriver

    def setup(self, browser: str):
        driver = None
        browser_name = browser.lower()

        if 'chrome' in browser_name:
            options = Options()
            options.add_experimental_option("detach", True)
            options.add_argument('window-size=1920x1080')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        elif 'edge' in browser_name:
            edge_options = EdgeOptions()
            edge_options.add_argument('window-size=1920x1080')
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

        driver.maximize_window()
        driver.implicitly_wait(60)
        driver.set_page_load_timeout(100)
        return driver
