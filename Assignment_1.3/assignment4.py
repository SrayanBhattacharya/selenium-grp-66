from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")

try:
    driver.maximize_window()
    #Child Nodes using CSS
    email = driver.find_element(By.CSS_SELECTOR,"div.form-group > input#email")
    email.send_keys("Example@gmail.com") #Email 
    address = driver.find_element(By.CSS_SELECTOR,"div.form-group > textarea#textarea")
    address.send_keys("Kolkata, West Bengal, India") #Address
    time.sleep(8)
finally:
    driver.quit()