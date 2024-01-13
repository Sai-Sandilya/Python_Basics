from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")


    #xpath with self
# company=driver.find_element(By.XPATH,"//a[contains(text(),'Electrosteel Cas')]/self::a").text
# print(company)

  #xpath with parent
# company=driver.find_element(By.XPATH,"//a[contains(text(),'Electrosteel Cas')]/parent::td").text
# print(company)

    #xpath with child and ancestor
# companys=driver.find_elements(By.XPATH,"//a[contains(text(),'Electrosteel Cas')]/ancestor::tr/child::td")
# print(len(companys))

    #xpath with ancestor
# company=driver.find_element(By.XPATH,"//a[contains(text(),'Electrosteel Cas')]/ancestor::tr").text
# print(company)


    #Xpath with decendant
# companys=driver.find_elements(By.XPATH,"//a[contains(text(),'Electrosteel Cas')]/ancestor::tr/descendant::*")
# print(len(companys))

    #xpath with following nodes
sel = driver.find_elements(By.XPATH,"//a[contains(text(),'Electrosteel Cas')]/ancestor::tr/following::*")
print(len(sel)) #2926

    #xapth with following:sibiling
followingSiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Electrosteel Cas')]/ancestor::tr/following-sibling::tr")
print(len(followingSiblings)) #345

    #xapth with precdings
precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'Electrosteel Cas')]/ancestor::tr/preceding::*")
print(len(precedings))


