from selenium import webdriver   
from selenium.webdriver.common.by import By
chrome_driver_path = "\\Users\\sphar\\Desktop\\Python 101\\Driver\\chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://www.python.org/")
dates = driver.find_elements(by= By.CSS_SELECTOR,value=".event-widget time")
names = driver.find_elements(by=By.CSS_SELECTOR,value=".event-widget li a")
date_list = []
name_list = []
for date in dates:
    date_list.append(date.text)
for name in names:
    name_list.append(name.text)
event_dict = {}

for n in range(len(date_list)):
    event_dict[n] = {
        "date" : date_list[n],
        "name" : name_list[n],
    }
print(event_dict)    
driver.quit()