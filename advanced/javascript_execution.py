from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        driver = webdriver.Firefox(executable_path=r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        driver.maximize_window()
        # driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(3)
        time.sleep(6)

        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

ff = JavaScriptExecution()
ff.test()