import time 
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")

#buttons = driver.find_elements(By.TAG_NAME, "button")
#print(buttons)
#print(type(buttons))
#for button in buttons:
 #     print(f"{button.text} = {button.is_displayed()}")
#      print(button.is_enabled())
      #print(button.text)
#driver.find_elements(By.ID, "john")  
#input[type='checkbox'][value='project-3']
#//input[@type='checkbox' and @value='project-3']
#checkBox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='project-3']")
#print(checkBox.is_selected())
#checkBox.click()
#print(checkBox.is_selected())  
radioButton = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='project-4']")
print(radioButton.is_selected())
radioButton.click()
print(radioButton.is_selected())  
time.sleep(5)
driver.quit()



