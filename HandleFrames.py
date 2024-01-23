import time

from pycparser.c_ast import Switch
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()
driver.get("https://ui.vision/demo/webtest/frames/")

#
# ##FRAMES /IFRAMES
# driver.switch_to.frame("NAme of thr frame")
# driver.switch_to.frame("id of thr frame")
# driver.switch_to.frame("webelement of thr frame")
# driver.switch_to.frame(0)
#
# Taganmes:frame,iframe,form
# driver.switch_to.default_content()

driver.switch_to.frame(0)
driver.find_element(By.NAME,"mytext1").send_keys("sdhg")
driver.switch_to.default_content()   #go back to main page

driver.switch_to.frame(1)
driver.find_element(By.NAME,"mytext2").send_keys("xyx")

driver.switch_to.default_content()   #go back to main page
time.sleep(5)


