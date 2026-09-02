from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")

try:
    driver.maximize_window()
    #CSS Selector Challenge
    driver.find_element(By.CSS_SELECTOR,"[id^='nam']").send_keys("Satadru") #Name
    driver.find_element(By.CSS_SELECTOR,"[id*='hon']").send_keys("1234567890") #Phone number
    driver.find_element(By.CSS_SELECTOR,"[class$='-check-input']").click() #Gender
    dropdown = Select(driver.find_element(By.CSS_SELECTOR,"[id='country']")).select_by_value("india") #Dropdown
    time.sleep(5)
finally:
    driver.quit()