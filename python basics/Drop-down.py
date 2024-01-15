import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Edge()



driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

Drp_Countryelem=driver.find_element(By.XPATH,"//select[@id='country']")
Drpcountry=Select(Drp_Countryelem)

#select option from drop-down
# Drpcountry.select_by_visible_text("India")
#
# time.sleep(5)

# capture all the option and print them
alloptions=Drpcountry.options
print(len(alloptions))
# for all in alloptions:
#     print(all.text)


# Select option without using Built-in  method

for all in alloptions:
    if all.text=='India':
        all.click()
        break
time.sleep(10)