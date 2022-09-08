from selenium import webdriver
import time
import os

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")


driver.get("https://tr-tr.facebook.com/")

username= driver.find_element(By.NAME, "email").send_keys("E-mail girilecek")
password=driver.find_element(By.CLASS_NAME, "pass").send_keys("Şifre girilecek")
login=driver.find_element(By.NAME, "login").click()
time.sleep(5)
print(driver.title)
driver.quit()
