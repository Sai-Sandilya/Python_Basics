# we need to install "REQUESTS" package to find the broken links


from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests


driver=webdriver.Edge()

driver.get("http://www.deadlinkcity.com/")

alllink=driver.find_elements(By.TAG_NAME,'a')
count=0
print(len(alllink))
for link in alllink:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"    is broken link")
        count+=1
    else:
        print(url, "     is valid link")






