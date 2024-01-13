import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# 1) select specfic check box of the list


driver.find_element(By.XPATH,"//input[@id='sunday']").click()


# 2) selecvt all the checkbox
allboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(allboxes))

# for box in allboxes:
#     box.click()
#     print(box)
#
# time.sleep(10)

for i in range(len(allboxes)):
    allboxes[i].click()

time.sleep(10)


#slect multuples checkboxes by choice

# for box in allboxes:
#     weekname=box.get_attribute('id')
#     print(weekname)
#     if weekname=='monday'or weekname=='saturday':
#         box.click()

#4) select last two checkboxes

# for i in range(len(allboxes)-2,len(allboxes)):   #range(5,7)--->6 and 7
#     allboxes[i].click()
#
# time.sleep(10)


#5) sleect 1st two check boxes
# for i in range(len(allboxes)):#range(5,7)--->6 and 7
#     if i<2:
#         allboxes[i].click()
#
# time.sleep(10)

#6) clearing all the checkboxes
for box in (allboxes):
    if box.is_selected():
        box.click()
time.sleep(10)


