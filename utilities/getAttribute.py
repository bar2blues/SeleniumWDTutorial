from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetAttribute():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")

        print("Value of attribute is: " + result)
        time.sleep(1)
        driver.quit()


ff = GetAttribute()
ff.test()