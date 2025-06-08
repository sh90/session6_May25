from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Firefox()
browser.get('https://www.amazon.in')

browser.maximize_window()
# get the input elements
input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
search_button = browser.find_element(By.XPATH, "(//input[@type='submit'])[1]")

input_search.send_keys("Smartphones under 10000")
sleep(1)
search_button.click()
#
