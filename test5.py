import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
textArea = driver.find_element(By.ID, "description")
print(f"Text Area Vaule: {textArea.get_attribute('value')}")
textArea.send_keys("hello world!")
print(f"Text Area Vaule: {textArea.get_attribute('value')}")
time.sleep(5)
driver.quit()
