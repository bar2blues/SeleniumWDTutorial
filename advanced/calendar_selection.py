from selenium import webdriver
import time

class CalendarSelection():
    def test1(self):
        baseURL  ="https://www.expedia.com"
        driver = webdriver.Firefox(executable_path=r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Click flights tabs
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing-wrapper-hp-flight")
        # Click departing field
        departingField.click()
        # Find the date to be selected
        dateToSelect = driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/fieldset[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr[5]/td[6]/button")
        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()

    def test2(self):
        baseURL  ="https://www.expedia.com"
        driver = webdriver.Firefox(executable_path=r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Click flights tabs
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing-wrapper-hp-flight")
        # Click departing field
        departingField.click()
       # calMonths = driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/fieldset[2]/div/div[2]/div/div/div/div[2]")
        #allValidDates = calMonths.find_element_by_tag_name("td")

        time.sleep(2)

        #for date in allValidDates:
         #   if date.text == "31":
          #      date.click()
           #     break




ff = CalendarSelection()
ff.test1()