import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    testbox_username_id = 'Email'
    testbox_password_id = 'Password'
    login_btn_xpath = "//*[text()='Log in']"
    logout_btn_xpath = "//*[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.testbox_username_id).clear()
        self.driver.find_element(By.ID, self.testbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.testbox_password_id).clear()
        self.driver.find_element(By.ID, self.testbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_btn_xpath).click()


