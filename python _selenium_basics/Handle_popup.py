import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Alert window is not a webelement-there will be no locator for that
driver= webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

time.sleep(10)

alertwin=driver.switch_to.alert
print(alertwin.text)
time.sleep(2)
alertwin.send_keys("Welcome")
alertwin.accept()

time.sleep(10)