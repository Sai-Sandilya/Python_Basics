from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
links= driver.find_elements(By.TAG_NAME,'a')
print(len(links))
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()