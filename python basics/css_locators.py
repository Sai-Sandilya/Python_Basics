import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()

driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag & id-- tag is optional
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("sai123@gmail.com")

#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("sai123@gmail.com")
time.sleep(5)

# tag & class

#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("shsd")
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("shsd")


#tag & attribute

#driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal_email']").send_keys("shsg")
driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal_email']").send_keys("shsg")
#time.sleep(20)

#tag & class & attribute 
driver.find_element(By.CSS_SELECTOR,"input.inputtext[name='pass']").send_keys("shsd")
time.sleep(20)
