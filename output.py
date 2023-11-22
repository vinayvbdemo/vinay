import time 
from selenium import webdriver
driver =webdriver.Edge()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
time.sleep(5)
driver.quit()

