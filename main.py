from selenium import webdriver
import time
import undetected_chromedriver as uc

driver = uc.Chrome(use_subprocess=True)

driver.get("https://chat.openai.com/auth/login")
time.sleep(100)
