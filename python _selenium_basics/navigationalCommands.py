import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

#Back()
#forward()
#refresh()

#get()- to open the application URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.get("https://amazon.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()