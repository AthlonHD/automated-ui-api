# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotSelectableException
from selenium.common.exceptions import NoSuchElementException
import time


def get_time_stamp():
    """
    获取时间戳
    :return:
    """
    time_stamp = time.strftime("%m%d%H%M%S", time.localtime(time.time()))
    return time_stamp


class Base:
    def __init__(self, driver: WebDriver):
        """
        :param driver:
        """
        self.driver = driver

    def implicitly_wait(self):
        self.driver.implicitly_wait(10)

    def find_ele(self, loc):
        """
        找元素
        :param loc: 定位器，字符串形式
        :return:
        """
        try:
            WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.XPATH, loc)))
            ele = self.driver.find_element(By.XPATH, loc)
        except TimeoutException as e:
            print(e, f"{loc}" + "元素未出现")
            ele = None
        return ele

    def click_ele(self, loc):
        """
        点击元素
        :param loc:
        :return:
        """
        try:
            self.find_ele(loc).click()
        except NoSuchElementException:
            print(NoSuchElementException, f"{loc}" + "元素未点击")

    def send_text(self, loc, text):
        """
        输入值
        :param loc: 定位器
        :param text: 发送内容
        :return:
        """
        try:
            self.find_ele(loc).send_keys(text)
        except ElementNotSelectableException:
            print(ElementNotSelectableException, f"{text}" + "输入失败")
            print(text)
            print(type(text))

    def handling_popup_window(self):
        """
        处理浏览器自带弹窗
        :return:
        """
        alert = self.driver.switch_to.alert
        alert.accept()

    # 获取首页地址
    def go_home(self):
        self.driver.get(
            'https://mall30uat.capitaland.com.cn/#/index?mallId=88&portalId=74&__key=url_1623204663655_1')

    # 获取活动地址
    def go_activity(self):
        self.driver.get('https://mall30uat.capitaland.com.cn/#/activity_list?mallId=88&portalId=74&__key'
                        '=url_1623204971557_50')

    # 获取消息地址
    def go_message(self):
        self.driver.get('https://mall30uat.capitaland.com.cn/#/message_list?mallId=88&portalId=74&__key'
                        '=url_1623205666216_1')

    # 获取个人中心地址
    def go_user_center(self):
        self.driver.get('https://mall30uat.capitaland.com.cn/#/user_center?mallId=88&portalId=74&__key'
                        '=url_1623205793763_34')

    # 聚焦元素
    def focus_ele(self, loc):
        self.driver.execute_script("arguments[0].scrollIntoView();", loc)

    def remove_read_only(self):
        js1 = "document.getElementsByClassName('ant-calendar-picker-input ant-input')[0].removeAttribute('readonly')"
        self.driver.execute_script(js1)
