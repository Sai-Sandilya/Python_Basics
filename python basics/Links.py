import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,'Digital downloads').click()
time.sleep(10)

# find number of links in page
link=driver.find_elements(By.TAG_NAME,'a')
print(len(link))

# print all the links names
for l in link:
    print(l.text)


# handle broken links

