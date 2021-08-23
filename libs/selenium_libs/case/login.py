# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import time
from libs.selenium_libs.common import loc
from libs.selenium_libs.common.base import Base


class Login(Base):

    def login(self, phone):
        # 打开网页后点击个人中心
        self.go_user_center()
        self.driver.refresh()
        time.sleep(2)
        # 点击登录\注册
        self.click_ele(loc.PersonalCenter.loc_login)
        # 输入手机号码
        self.send_text(loc.Login.loc_phone, phone)
        # 点击获取验证码
        # self.click_ele(loc.Login.loc_get_verification_code)
        time.sleep(1)
        # 输入验证码
        code = '1111'
        time.sleep(1)
        self.send_text(loc.Login.loc_input_verification_code, code)
        # 勾选按钮
        self.click_ele(loc.Login.loc_check)
        # 点击立即登录
        self.click_ele(loc.Login.loc_login)
        time.sleep(2)
