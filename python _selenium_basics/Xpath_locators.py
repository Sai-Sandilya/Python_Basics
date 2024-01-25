import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()

driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

#Relative -xpath
#driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("T-shirts")
#driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

#Xpath with OR operator
#driver.find_element(By.XPATH,"//input[@id='search_query_top' or @placeholder='Organization']").send_keys("sdf")

#Xpath with AND operator---it should satify both conditions

#driver.find_element(By.XPATH,"//button[@name='submit_search' and @type='submit']").click()

#Xpath with CONTAINS operator  and Starts=with operator
# driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("sdf")
# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()

#text operator

driver.find_element(By.XPATH,"//a[text()='Women']").click()