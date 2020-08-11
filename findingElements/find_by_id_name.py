from selenium import webdriver


class FindByIdName():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(executable_path = r"C:\Users\Federico Barderi\workspace_python\drivers\geckodriver.exe")
        driver.get(baseURL)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found an element by name")

        base2URL = "https://espanol.yahoo.com/?p=us"
        driver.get(base2URL)
        elementById = driver.find_element_by_id("applet_p_50000314")
         #yahoo.com   //*[@id="applet_p_50000314"]
        if elementById is not None:
            print("We found an element by IDname")

ff = FindByIdName()
ff.test()