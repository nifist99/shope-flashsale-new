from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from setting import Config
import random
import requests
from module.scraper import Shopee

USERNAME = '082238982100'
PASSWORD = 'Maret1099'
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

        #DONE LOGIN

        shope.open_url(URL_FLASH_SALE)

        cookie     = shope.cookie(URL_FLASH_SALE)

        cok = ''
        for key in cookie:
                cok += f"{key['name']} = {key['value']};" 



        url = "https://shopee.co.id/api/v4/item/get?itemid=1709344843&shopid=35772189"

        print(cok)

        payload={}
        headers = {
              'Cookie': f'{cok}',
              'Accept':'application/json',
              'Content-Type':'application/json',
              'sz-token': 'fhVRFExXTfZqc3MrRNyI3Q==|rV/2CBr3Fm1EJ434qkj4xyThebKqXvB0ZHfy7J4WX8rFB/wWwOClxLsIw2Eb37SQTEtt0Ji8EAl25d8ftE8f3y22gapPJkifof0=|bWvEAkb9mnXux7bA|06|3',
              'X-CSRFToken': 'iz1nh54Qch6BlSN3SxzwbzuEMtCo5gDS',
              'af-ac-enc-dat': 'AAcyLjQuMS0zAAABhJ7ZhHkAAAWFAW0AAAAAAAAAAAvjwIoQbhtY57gvQCDyqwF9rx8N6OU9EDJx2xm1/GTr1RPlUgQdcrJvh/NUQaxk4ZVG8CLalNNUvG1UJlKHfKD+y+ECTwa0Jv1IJ5zvy9KbIroNipppTEPiWEzBxepBevIkQ/NPkaWRyHFXn87XNjW5orgzkWOzjLDykZY2dhCO2aemlpFjs4yw8pGWNnYQjtmnppb7K2uBsnKOjb+4qJgUQ63JurWZnSKvBtk/5lc8+aXC6ZppTEPiWEzBxepBevIkQ/PlrUOo3cLVhcuMMtQ3vr33W+FiR3V2f8UmfHL+NpoWdu7yMO45B4ONFL+qGotNgRwm8k+iu/bl9gygdeslzSsITlEnjGaCoXSlA02AlYjkjFz5dew8THJlxHqfp9DzL2qULbMzRT7tgNKEc0t8kV4bkWOzjLDykZY2dhCO2aemltaYSNH3qpLos1wCO0s3ieVrgO1pORNqMJOWO5sx2uxOdO5bIn0cJCDhTB76tewBrw==',
              'X-API-SOURCE': 'rweb'
        }

        

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json())




if __name__ == "__main__":
    main()
