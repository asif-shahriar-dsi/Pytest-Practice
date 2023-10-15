from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options

import pytest


class Setup:

    def __init__(self):
        self.driver = webdriver

    def setup(self):
        # ---------------------------------Chrome----------------------------------
        ops = Options()
        ops.add_argument("headless")
        ops.add_argument('window-size=1920x1080')
        driver = self.driver.Chrome(service=Service(ChromeDriverManager().install(), options=ops))

        # ---------------------------------Chrome----------------------------------
        # edge_ops = EdgeOptions()
        # edge_ops.add_argument("headed")
        # edge_ops.add_argument('window-size=1920x1080')
        # driver = self.driver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_ops)
        # ---------------------------------Edge----------------------------------
        driver.implicitly_wait(10)
        driver.maximize_window()
        print("Driver launched successfully!!")
        return driver

