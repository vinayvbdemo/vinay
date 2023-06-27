import time 
from selenium import webdriver
from selenium.webdriver import chrome 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
chromeDriver = webdriver.Chrome()
chromeDriver.get("https://www.flipkart.com/mobiles/~cs-tt5wilg3vt/pr?sid=tyy%2C4io&collection-tab-name=Moto+g13&param=37454634&otracker=clp_bannerads_1_25.bannerAdCard.BANNERADS_fdgvdc_mobile-phones-store_F2CQ4ABRSGAO")
Webelement = webdriver.find_element (BY.NAME, 'MOTOROLA g13').click()
time.sleep(5)
driver.quit()
