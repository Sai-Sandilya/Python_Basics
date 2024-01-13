from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

#get()- to open the application URL
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
##################find_element()--returns single webelement


#1) locator matching with single webelement
# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
# #1) locator matching with Multiple  webelements
#
# links=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(links.text)

##################find_elements()--returns multiple webelement{list}
#1) locator matching with single webelement
# eles=driver.find_elements(By.ID,"small-searchterms")
# print(len(eles))
# print(eles[0].send_keys("trg"))

#2) locator matching with multiple webelement
links=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(links))
for link in links:
    print(link.text)