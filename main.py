from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_SPEED = YOUR_PROMISED_INTERNET_SPEED

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://fast.com/")

sleep(10)
speed = driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/div[2]/div/div[1]')

if int(speed.text) < PROMISED_SPEED:
    print("Speed is lower than advertised")
