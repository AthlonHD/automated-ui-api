# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import time
import allure
from libs.selenium_libs.common import loc
from libs.selenium_libs.common.base import Base


class PagePersonalCenter(Base):

    @allure.step("获取个人积分")
    def get_my_integral(self):
        time.sleep(2)
        return self.driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_integral)[-2].text

    @allure.step('获取卡包数量')
    def get_my_coupon_amount(self):
        time.sleep(2)
        return self.driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_card_bag_amount)[-1].text


