


import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


with open("output.json", "r") as file:
    SID_data = json.load(file)

print(SID_data) 


driver = webdriver.Chrome()
driver.get("https://mybaps.uk.baps.org/")
    
time.sleep(3)




p1_sign_in = driver.find_element(By.XPATH, '//a[@href="/Account/SignUpSignIn"]')
p1_sign_in.click()

time.sleep(5)

email_type= driver.find_element(By.ID, 'logonIdentifier') 
email_type.send_keys("manislearning@gmail.com") # Change the text here to the karaykars email 

time.sleep(3)

password_type= driver.find_element(By.ID, 'password') 
password_type.send_keys("SonicBoom1") # Change the text here to the karaykars password
time.sleep(3)

move_on_sign_up = driver.find_element(By.ID, 'next')
move_on_sign_up.click()


time.sleep(30)


