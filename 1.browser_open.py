#pip install selenium

# Selenium doesn't talk to browser directly, you need to use specific browser drivers
from selenium import webdriver
import time

driver = webdriver.Firefox()
#drive = webdriver.Chrome()
time.sleep(10)
# driver.close()
