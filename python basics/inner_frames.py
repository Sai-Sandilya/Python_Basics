import time

from pycparser.c_ast import Switch
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe= driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")

driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")

driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")

time.sleep(5)

driver.switch_to.parent_frame()  # direct switch to parent frame (outer iframe)

