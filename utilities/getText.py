from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetText():

    def testGetText(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        openTabElement = driver.find_element(By.ID, "opentab" )
        elementText = openTabElement.text
        print("Text on element is: " + elementText)
        time.sleep(1)
        driver.quit()


ff = GetText()
ff.testGetText()