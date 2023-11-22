import time 
from selenium import webdriver
from selenium.webdriver import Edge 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
Driver = webdriver.Edge()
Driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
#Webelement = webdriver.find_element (BY.NAME, 'MOTOROLA g13').click()
time.sleep(5)
driver.quit()
print ("db closed")
