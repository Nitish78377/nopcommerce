from time import sleep

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup():
    driver = uc.Chrome(services=ChromeService(ChromeDriverManager().install()))
    return driver
