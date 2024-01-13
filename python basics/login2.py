import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

# Find the element that contains the email and password
details_element = driver.find_element(By.XPATH, "//p[1]")

# Get the text of the element
details_text = details_element.text

# Split the text into two parts at the newline character
details_parts = details_text.split("\n")
print(details_parts)

# Get the email and password and store them in separate variables
email = details_parts[0].split(":")[1].strip()
password = details_parts[1].split(":")[1].strip()

# Print the email and password
print("Email:", email)
print("Password:", password)

driver.find_element(By.CSS_SELECTOR,"#Email").clear()
time.sleep(30)
driver.find_element(By.CSS_SELECTOR,"#Email").send_keys(email)
