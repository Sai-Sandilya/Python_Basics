from selenium import webdriver

driver= webdriver.Edge()

#sysntax: http://username:password@URL
#username and password should be injected with the URL

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.maximize_window()
