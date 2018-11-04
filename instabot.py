from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def run():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")

    # driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    email_field = driver.find_element_by_name('username')
    email_field.send_keys('nachwon@hotmail.com')

    password_field = driver.find_element_by_name('password')
    password_field.send_keys('mgame132')

    login_button = driver.find_element_by_class_name('L3NKy')
    login_button.click()

    driver.implicitly_wait(10)

    mobile_button = driver.find_element_by_xpath("//label[@for='choice_0']")
    mobile_button.click()

    send_code = driver.find_element_by_xpath("//button[text()='보안 코드 보내기']")
    send_code.click()

    driver.implicitly_wait(2)

    security_code_field = driver.find_element_by_xpath(("//input[@id='security_code']"))

    code = input('Security code: ')

    security_code_field.send_keys(code)
    verify_button = driver.find_element_by_xpath("//button[text()='제출']")
    verify_button.click()

    later_button = driver.find_element_by_xpath("//button[text()='나중에 하기']")
    later_button.click()

    heart_button = driver.find_element_by_class_name('coreSpriteDesktopNavActivity')
    heart_button.click()

    driver.implicitly_wait(5)

    feeds = driver.find_element_by_class_name('YFq-A')

    print(feeds)

    driver.get_screenshot_as_file('insta.png')



if __name__ == '__main__':
    run()