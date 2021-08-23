# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import time
import pytest
from selenium import webdriver
from libs.env_conf import config as env_conf
from libs.selenium_libs.case import login


@pytest.fixture(scope='session')
def driver():
    path = env_conf.path
    mobile_emulation = {'deviceName': 'Galaxy S5'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    options.add_argument('disable-infobars')
    executable_path = path + r'drivers/chromedriver.exe'
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, executable_path=executable_path)
    driver.maximize_window()
    time.sleep(3)
    login.Login(driver).login('15738995325')
    # yield
    # time.sleep(1)
    # self.driver.quit()
    return driver


