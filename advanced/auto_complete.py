from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():

    def test(self):
        baseUrl = "https://www.southwest.com"
        driver = webdriver.Firefox(executable_path=r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Send Partial Data
        cityField = driver.find_element_by_id("air-city-departure")
        cityField.send_keys("New York")
        time.sleep(3)
        # Find the item and click
        itemToSelect = driver.find_element_by_xpath("//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        itemToSelect.click()

        # time.sleep(3)
        # driver.quit()

ff = AutoComplete()
ff.test()