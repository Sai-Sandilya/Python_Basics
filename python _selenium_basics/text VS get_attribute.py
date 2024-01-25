import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

#get()- to open the application URL
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

emailtext=driver.find_element(By.CSS_SELECTOR,"#Email")
emailtext.clear()
emailtext.send_keys("jshgjhs@gmail.com")
time.sleep(30)

#text----returns inner text of the element
print(emailtext.text)

#get_attribute('value')-----
print(emailtext.get_attribute('value'))