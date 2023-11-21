import time 
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
#textArea = driver.find_element(By.NAME, "emp_name")
#print(f"Text Area Value: {textArea.get_attribute('value')}")
#textArea.send_keys("Vinay B")
#print(f"Text Area Value: {textArea.get_attribute('value')}")
dropdown = driver.find_element(By.CSS_SELECTOR, "#mul-projectName > option[value='Project-4']")
dropdown.click()
print(f"Text Area Value: {dropdown.get_attribute('value')}")
time.sleep(5)
driver.quit()
