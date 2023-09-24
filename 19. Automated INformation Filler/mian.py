from selenium import webdriver   
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "chromedriver_Path"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
search_First = driver.find_element(by= By.NAME,value="fName")
search_Last = driver.find_element(by= By.NAME,value="lName")
search_Mail = driver.find_element(by= By.NAME,value="email")
search_First.send_keys("Shubham")
search_Last.send_keys("Haraniya")
search_Mail.send_keys("spharaniya18@gmail.com")
enter = driver.find_element(by=By.CSS_SELECTOR,value="form button")
enter.click()
