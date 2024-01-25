############Wait Commands

#1) implicit wait
#2) explict wait
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

mywait=WebDriverWait(driver,10,ignored_exceptions=[Exception])  #explicit wait declaration

driver.get("https://www.google.com")
driver.maximize_window()
search=driver.find_element(By.NAME,"q")
search.send_keys("Selenium")
search.submit()

#explicit wait --until(EC.presence_of_element_located)  --it is a condition
searchbox=mywait.until(EC.presence_of_element_located(By.XPATH,"//h3[text()='Selenium']"))
searchbox.click()






#explicit wait()
