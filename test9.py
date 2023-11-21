import time 
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
time.sleep(20)
driver.quit()
