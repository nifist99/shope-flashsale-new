from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement

# Added for FireFox support
from webdriver_manager.firefox import GeckoDriverManager
import chromedriver_autoinstaller
import undetected_chromedriver.v2 as uc
import os
import time

import pyautogui

def retry(func):
    """
    Adds retry functionality to functions
    """
    # wrapper function
    def wrapper(*args, **kwargs):
        max_tries = 5
        attempt = 1
        status = False
        while not status and attempt < max_tries:
            print(f'[{func.__name__}]: Attempt - {attempt}')
            status = func(*args, **kwargs)
            if status == 'skip_retry':
                status = False
                break                    
            attempt +=  1
        return status
    return wrapper


class Shopee:
    def __init__(self, username, password, timeout=30, browser='chrome', headless=False):
        # current working directory/driver

        self.browser = 'chrome'
        self.driver_baseloc = os.path.join(os.getcwd(), 'driver')
        self.comment_disabled = False

        # Firefox
        if browser.lower() == 'firefox':
            self.browser = 'firefox'
            # Firefox Options
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            options.set_preference("dom.webnotifications.enabled", False)
            options.log.level = 'fatal'

            # current working directory/driver/firefox
            self.driver = webdriver.Firefox(
                executable_path=GeckoDriverManager(path=os.path.join(self.driver_baseloc, 'firefox')).install(),
                options=options)
        # Chrome
        else:
            # Chrome Options
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--disable-notifications")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument("--log-level=3")
            options.add_argument("--start-maximized")

            # current working directory/driver/chrome
            # self.driver = webdriver.Chrome(options=options)
            self.driver = uc.Chrome()

        self.wait = WebDriverWait(self.driver, timeout)
        self.baseurl = "https://shopee.co.id/buyer/login"
        self.targeturl = self.baseurl
        self.username = username
        self.password = password
        self.tag = None
        self.account = None

        self.flash = WebDriverWait(self.driver, 2)

    def login(self):
        """
        Initiates login with username and password
        """
        try:
            self.driver.get(self.baseurl)
            # self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Log In"]'))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input'))).send_keys(self.username)
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input'))).send_keys(self.password)
            time.sleep(4)
            pyautogui.hotkey('enter')
        except:
            return False
        return True

    def validate_login(self):
        """
        Validates login
        """
        try:
            # look for user avatar
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shopee-avatar__img')))
            return True
        except:
            return False

    def is_page_loaded(self):
        """
        Checks if page is loaded successfully
        """
        try:
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            return True
        except:
            return False

    def open_url(self,url):
        try:
            self.driver.get(url)
            return True
        
        except:
            return False


    def fetch_userAgent(self,url):

        try:
            self.driver.get(url)
            user_agent= self.driver.execute_script("return navigator.userAgent")
            return user_agent
        except:
            return False

    def cookie(self,url):
        try:
            self.driver.get(url)
            cookie = self.driver.get_cookies()

            return cookie
        except:
            return False

    #FUNCTION FLASH SALE

    def varian(self):

        try:
            beli = self.flash.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[1]')))
            beli.click()
            return True
        except:
            return False

    
    def close_web(self):

        self.driver.close()

        print("SELAMAT KAWAN")

    
    def flash_sale(self,url,pin):
        """
        Initiates login with username and password
        """
        try:
            #VARIAN BARANG

            self.varian()

            beli = self.flash.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div/div[1]/div[3]/div/div[5]/div/div/button[2]')))
            beli.click()

            checkout = self.flash.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[3]/div[2]/div[7]/button[4]')))
            checkout.click()

            pay      = self.flash.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[4]/div[2]/div[9]/button')))
            pay.click()

            #PEMBAYARAN 
            button_pay      = self.flash.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pay-button"]')))
            button_pay.click()

            pyautogui.write(pin)

            konfrim         =  self.flash.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[4]/div[2]')))

            konfrim.click()

            time.sleep(2)

            print("success get barangnya brooo")

        except:
            return False
        return True
