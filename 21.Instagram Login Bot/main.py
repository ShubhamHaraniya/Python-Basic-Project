from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
Insta_User = "Enter Your Email"
Insta_Pass = "Enter Yout Password"
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(5.0)
User_input = driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
User_input.send_keys(Insta_User)
driver.implicitly_wait(5.0)
Pass_Input = driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
Pass_Input.send_keys(Insta_Pass)
Pass_Input.send_keys(Keys.ENTER)
time.sleep(5)
Not_Now = driver.find_element(by=By.CSS_SELECTOR,value='._ac8f button')
Not_Now.click()
time.sleep(5)
Not_Now_Noti = driver.find_element(by=By.CSS_SELECTOR,value='._a9-z ._a9_1')
Not_Now_Noti.click()
