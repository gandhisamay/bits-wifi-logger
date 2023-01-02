import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import subprocess

class BitsWifiLogger:
    def __init__(self):
        driver_path = "/home/samaygandhi/Documents/chromedriver"
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/brave-browser"
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        self.DRIVER = webdriver.Chrome(service=Service(executable_path=driver_path), options=options)

    def get_current_connection(self):
        self.BITS_WIFI = "BITS STUDENT"
        ssid = str(subprocess.run(["iwgetid", "-r"],capture_output=True).stdout)
        if self.BITS_WIFI in ssid:
            self.WIFI_NAME = self.BITS_WIFI
        else: self.WIFI_NAME = "OTHERS"
       
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
        try:
            self.get_current_connection()

            if self.WIFI_NAME != self.BITS_WIFI: 
               os.execlp("echo", "echo", "Bits wifi not connected")

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
            self.DRIVER.close()

            if connectionStatusMessage: os.execlp("notify-send", "notify-send", "-u", "low", "bits_wifi_logger: Login Failed!")
            else:os.execlp("notify-send", "notify-send", "-u", "low", "bits_wifi_logger: Login Successfull")
        except:
           self.DRIVER.close()
           os.execlp("notify-send", "notify-send", "-u", "low", "bits_wifi_logger: Login Failed!")

if __name__ == "__main__":
    logger = BitsWifiLogger()
    logger.run()
