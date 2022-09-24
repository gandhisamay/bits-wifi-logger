import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

driver = webdriver.Chrome(service=Service('/home/samaygandhi/Documents/chromedriver'))
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

driver.get("https://fw.bits-pilani.ac.in:8090")


exists = os.path.isfile("/home/samaygandhi/Documents/.env")
if exists:
    # Extract the details
    load_dotenv()
    usnm = os.environ.get('USERNAME')
    pswd = os.environ.get('PASSWORD') 
else: 
    raise Exception('Credentials not found')

username = driver.find_element(By.ID,'username')
password = driver.find_element(By.ID,'password')
username.send_keys(usnm)
password.send_keys(pswd)

driver.find_element(By.ID, 'loginbtn').click()

driver.implicitly_wait(time_to_wait=1)

connectionStatusMessage = driver.find_element(By.ID, 'statusmessage').text

if connectionStatusMessage:
    print('Failed to connect')
else:
    print('Connected Successfully')

driver.close()
