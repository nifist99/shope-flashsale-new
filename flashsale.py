from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from setting import Config
import random
import requests
from module.scraper import Shopee

import time

USERNAME = '082238982100'
PASSWORD = 'Maret1099'
PIN      = '100399'
URL_FLASH_SALE = 'https://shopee.co.id/UBS-1-Gram-i.104204972.7670453756'

def main():

        #PROSES LOGIN SHOPE 
        shope = Shopee(USERNAME,PASSWORD,timeout=30, browser='chrome', headless=False)

        shope.is_page_loaded()

        shope.login()

        is_login = ''
        try:
                shope.validate_login()

                is_login = 'success login'
        
        except:
                is_login = 'failed'
        
        print(is_login)
        #DONE LOGIN

        shope.open_url(URL_FLASH_SALE)

        jam_device = time.strftime("%H:%M:%S", time.localtime())
        jam = int(input("\033[32m[+] Masukan Jam untuk memulai beli : "))
        menit = int(input("\033[32m[+] Masukan Menit untuk memulai beli : "))
        detik = int(input("\033[32m[+] Masukan Detik untuk memulai beli : "))
        waktu = '{:02d}:{:02d}:{:02d}'.format(jam, menit, detik)

        while jam_device != waktu :
            jam_device_INT = int(time.strftime("%H%M%S", time.localtime()))
            waktu_int='{:02d}{:02d}{:02d}'.format(jam, menit, detik)
            nilai = int(waktu_int)

            if jam_device_INT <= nilai:
                shope.open_url(URL_FLASH_SALE)
                print("\033[32m[+] INFO:\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mWAKTU BELUM MULAI.!")
            else:
                break

        shope.flash_sale(URL_FLASH_SALE,PIN)
        shope.close_web()


    


if __name__ == "__main__":
    main()
