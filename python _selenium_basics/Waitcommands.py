############Wait Commands

#1) implicit wait
#2) explict wait
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
#implicit wait--# it will applicale for all the statements
#perfoemnce will not be reduced .(if the element is avaiable within the time it proceed to excute further)
#if the element is not loaded with in the time , there will be a change of getting exception
driver.implicitly_wait(10)

driver.get("https://www.google.com")
driver.maximize_window()
search=driver.find_element(By.NAME,"q")
search.send_keys("Selenium")
search.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

time.sleep(10)


#explicit wait()
