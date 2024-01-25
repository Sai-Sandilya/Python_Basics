import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

#close()--close single browser windows (where driver focused)
#quit()--it will close the entire browser

#get()- to open the application URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"a[href='http://www.orangehrm.com']").click()

# Wait for the page to load
time.sleep(20)

# Close the second tab
driver.close()

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
