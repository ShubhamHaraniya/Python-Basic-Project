from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from colorama import Fore,Back
driver = webdriver.Chrome()
def Find_Social_Account(Number):
    # FaceBook Searching


    print(Fore.RED+'---------------------------------------------------------------------------------------')
    print(Fore.LIGHTGREEN_EX+"Facebook Searching......")
    driver.get("https://www.facebook.com/")
    Forgot_Pass = driver.find_element(by=By.CSS_SELECTOR,value='._6ltj a')
    Forgot_Pass.click()
    Email_Web = driver.find_element(by=By.XPATH,value='//*[@id="identify_email"]')
    Email_Web.send_keys('+91'+str(Number))
    Search = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div/form/div/div[3]/div/div[1]/button')
    Search.click()
    time.sleep(5)
    try:
        Found_Or_Not= driver.find_element(by=By.XPATH,value='//*[@id="identify_yourself_flow"]/div/div[2]/div[1]/div[1]')
        if Found_Or_Not.text == ('No search results'):
            print(Fore.CYAN+"There Is No Acoount From This Email")
            print(Fore.RED+'---------------------------------------------------------------------------------------')    
    except:
        print(Fore.CYAN+"Acoount Found From Facebook....")
        Account = driver.find_elements(By.CLASS_NAME,"_9o4d")
        time.sleep(2)
        for name in Account:
            print(Fore.CYAN+'->'+name.text)
        print(Fore.RED+'---------------------------------------------------------------------------------------')


    # Instagram Searching    


    print(Fore.LIGHTGREEN_EX+"Instgram Searching......")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    Forgot_Pass = driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/a')
    Forgot_Pass.click()
    time.sleep(5)
    Email_Web = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[4]/form/label/input')
    Email_Web.send_keys('+91'+str(Number))
    Search = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[5]/div')
    Search.click()
    time.sleep(3)
    try:
        Found_or_Not = driver.find_element(by=By.CLASS_NAME,value='_abmp')
        if Found_or_Not.text == 'No users found':
            print(Fore.CYAN+"There Is No Acoount From This Email")
            print(Fore.RED+'---------------------------------------------------------------------------------------')
    except:
        print(Fore.CYAN+"Acoount Found From Instagram")
        print(Fore.RED+'---------------------------------------------------------------------------------------')

    # X(Twitter) Searching

    print(Fore.LIGHTGREEN_EX+"X(Twitter) Searching......")
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(5)
    Input_X = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    Input_X.send_keys('+91'+str(Number))
    time.sleep(3)
    Next_but = driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    Next_but.click()
    try:
        text = driver.find_element(by=By.XPATH,value='//*[@id="modal-header"]/span/span')
        if text.text == 'Enter your password':
            print(Fore.CYAN+"Acoount Found From X")
            print(Fore.RED+'---------------------------------------------------------------------------------------')
    except:
        print(Fore.CYAN+"There Is No Acoount From This Email")
        print(Fore.RED+'---------------------------------------------------------------------------------------')
Find_Social_Account(123456788899)