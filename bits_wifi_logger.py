import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

class BitsWifiLogger:
    def __init__(self):
        driver_path = "/home/samaygandhi/Documents/chromedriver"
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/brave-browser"
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        self.DRIVER = webdriver.Chrome(service=Service(executable_path=driver_path), options=options)

    def get_keys(self):
        #Extract the Credentials
        exists = os.path.isfile("/home/samaygandhi/Documents/.env")
        if exists:
            load_dotenv()
            self.USERNAME = os.environ.get('USERNAME')
            self.PASSWORD = os.environ.get('PASSWORD') 
        else: 
            raise Exception('Credentials not found')


    def run(self):
        #Get the website
        self.DRIVER.get("https://fw.bits-pilani.ac.in:8090")

        self.get_keys()

        #Send the keys to the appropriate the input fields
        
        username = self.DRIVER.find_element(By.ID,'username')
        password = self.DRIVER.find_element(By.ID,'password')

        username.send_keys(self.USERNAME)
        password.send_keys(self.PASSWORD)

        #Connect
        self.DRIVER.find_element(By.ID, 'loginbtn').click()
        self.DRIVER.implicitly_wait(time_to_wait=1)

        connectionStatusMessage = self.DRIVER.find_element(By.ID, 'statusmessage').text

        if connectionStatusMessage: print('Failed to connect')
        else:print('Connected Successfully')

        self.DRIVER.close()


if __name__ == "__main__":
    logger = BitsWifiLogger()
    logger.run()
