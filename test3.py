import time 
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Chrome()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
#submitButton = driver.find_element(By.NAME,"submit_button")
#submitButton.click()
#resetButton = driver.find_element(By.ID,"reset_button").click()
#saveButton = driver.find_element(By.CLASS_NAME,"qa_circle").click()
#driver.find_element(By.LINK_TEXT,"QA Circle").click()
driver.find_element(By.TAG_NAME,"a").click()

#print(submitButton)
time.sleep(5)
driver.quit()