from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

#get()- to open the application URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#title- to captutre the title of the current paghe
print(driver.title)


#current_url---- to capture the current url of the webpage

print(driver.current_url)

#page-source---to capture source code of the page
source=driver.page_source
print(source)

