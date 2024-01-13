import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)

# Find the element that contains the username
username_element = driver.find_element(By.XPATH, "//p[normalize-space()='Username : Admin']")
password_element = driver.find_element(By.XPATH,"//p[normalize-space()='Password : admin123']")

# Get the text of the element
username_text = username_element.text
password_text = password_element.text

# Split the text into two parts at the colon character
username_parts = username_text.split(":")
password_parts = password_text.split(":")

# Get the second part (which is the username) and store it in a variable
username = username_parts[1].strip()
password = password_parts[1].strip()

# Print the username
print(username)
print(password)

# Enter the username and password into the login form
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(30)

act_title= driver.title
expe_title="OrangeHRM"

if act_title==expe_title:
    print("login page passed")
    driver.save_screenshot("E:\python_basics\pyhton basics"+"login_page.png")
else:
    print("Login failed")

driver.close()