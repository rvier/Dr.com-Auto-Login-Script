import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #FireFox Quantum https://www.mozilla.org/en-US/firefox/
    def test_login_in_w17216(self):
        driver = self.driver
        driver.get("http://172.16.2.101:8080/Self/login/")
        elem = driver.find_element_by_name("account")
        elem.send_keys("2015************")
        elem = driver.find_element_by_name("password")
        elem.send_keys("***")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text('Offline').click()
        sleep(2)
        driver.get("http://172.16.2.100/")
        sleep(1)
        driver.refresh()
        driver.implicitly_wait(30)
        elem2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/form/input[2]")
        elem2.send_keys("2015************")
        elem2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/form/input[3]")
        elem2.send_keys("***")
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/select/option[2]').click()
        driver.implicitly_wait(30)
        elem2.send_keys(Keys.ENTER)
        driver.implicitly_wait(30)
        sleep(2)
        driver.get("http://172.16.2.100/")
        sleep(2)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
