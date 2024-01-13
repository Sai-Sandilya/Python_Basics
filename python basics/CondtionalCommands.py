#conditional comands
# 1) is_displayed()
# 2) is_enabled()
# 3) is_selected()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

#get()- to open the application URL
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# 1) is_displayed()  2) is_enabled()

searchbox=driver.find_element(By.ID,"small-searchterms")
print(searchbox.is_displayed())

print("enable status:  ",searchbox.is_enabled())

# 3) is_selected() -- for radio buttons and check boxes
male_rd=driver.find_element(By.XPATH,"//input[@id='gender-male']")
female_rd=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(male_rd.is_selected())
print(female_rd.is_selected())

male_rd.click()
print(male_rd.is_selected())


