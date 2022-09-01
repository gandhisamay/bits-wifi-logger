import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service('/home/samaygandhi/Documents/chromedriver'))
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

driver.get("https://fw.bits-pilani.ac.in:8090")

exists = os.path.isfile("./.env")
if exists:
    # Extract the details
    f = open("./.env", "r")
    credentials = f.readlines()
    usnm = credentials[0]
    pswd = credentials[1]
else:
    raise Exception('Credentials not found')

username = driver.find_element(By.NAME,'username')
password = driver.find_element(By.NAME,'password')

username.send_keys(usnm)
password.send_keys(pswd)

driver.find_element(By.CLASS_NAME, 'buttonrow').click()

driver.implicitly_wait(time_to_wait=1)

connectionStatusMessage = driver.find_element(By.ID, 'statusmessage').text

if connectionStatusMessage:
    print('Failed to connect')
else:
    print('Connected Successfully')

driver.close()
