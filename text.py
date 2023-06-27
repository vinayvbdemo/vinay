import time 
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Chrome()
driver.maximize_window() 
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
webpageTitle = driver.title
print(webpageTitle)
time.sleep(5)
driver.quit()


