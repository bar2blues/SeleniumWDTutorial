from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers
import time

class UsingWrappers():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        textField = hw.getElement("name")
        textField.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType= "xpath")
        textField2.clear()


ff = UsingWrappers()
ff.test()