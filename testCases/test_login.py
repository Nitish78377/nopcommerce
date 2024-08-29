import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title = self.driver.title
        if (act_title == "Your store. Login"):

            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('..\\ScreenShots\\' + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if (act_title == 'Dashboard / nopCommerce administration'):
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('..\\ScreenShots\\' + "test_Login.png")
            self.driver.close()
            assert False
