from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pytest
from TestData import Data
from TestLocators import Locators

class TestArun:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_title(self, booting_function):
        self.driver.get(Data.Arun_Data().url)
        sleep(3)
        assert self.driver.title == 'OrangeHRM'
        print('Success title is correct')
    
    def test_login(self, booting_function):
        self.driver.get(Data.Arun_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=Locators.Arun_Locator().Username_Locator).send_keys(Data.Arun_Data().Username)
        self.driver.find_element(by=By.NAME, value=Locators.Arun_Locator().Password_Locator).send_keys(Data.Arun_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Locators.Arun_Locator().LoginButtonLocator).click()
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Logged in with Username {a} and Password {b}". format(a=Data.Arun_Data().Username,b=Data.Arun_Data().Password))
