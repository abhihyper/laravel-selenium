from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Start Chrome
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000")

wait = WebDriverWait(driver, 15)

# Random values
email_value = f"user{random.randint(100,999)}@test.com"
password_value = f"pass{random.randint(1000,9999)}"

# WAIT and FIND email input (try id first)
email_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='email' or @type='text']"))
)
email_input.send_keys(email_value)

# WAIT and FIND password input
password_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
)
password_input.send_keys(password_value)

# Wait and exit
time.sleep(3)
driver.quit()
