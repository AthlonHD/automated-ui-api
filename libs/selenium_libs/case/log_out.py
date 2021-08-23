# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import time
from libs.selenium_libs.common.base import Base


class Logout(Base):

    def log_out(self):
        self.go_user_center()
        time.sleep(1)
        ele = self.driver.find_element_by_link_text('其他')
        self.focus_ele(ele)
        time.sleep(1)
        ele.click()
        time.sleep(1)
        self.click_ele('//div[contains(@class,"user_signout")]')