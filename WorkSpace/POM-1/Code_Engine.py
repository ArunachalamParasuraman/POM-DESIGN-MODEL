from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData import Data
from TestLocators import Locators

class Run_Engine:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(Data.Arun_Data().url)
    
    def Login(self):
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.Arun_Locator().Username_Locator))).send_keys(Data.Arun_Data().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.Arun_Locator().Password_Locator))).send_keys(Data.Arun_Data().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Arun_Locator().LoginButtonLocator))).click()

Run_Engine().Login()
