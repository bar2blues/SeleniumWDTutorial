from selenium import webdriver


class RunFFTests():
    def testMethod(self):
        # Instantiate the FF Browser Command
        driver = webdriver.Firefox(executable_path = r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        #  Open the provided URL
        driver.get("http://www.google.com")

ff = RunFFTests()
ff.testMethod()