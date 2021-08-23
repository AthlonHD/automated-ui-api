# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import allure
from libs.selenium_libs.common import loc
from libs.selenium_libs.common.base import Base


class PageActivity(Base):
    @allure.step('点击搜索框')
    def click_search(self):
        self.driver.find_elements_by_xpath(loc.Activity.loc_search1)[-1].click()

    @allure.step('输入活动名称')
    def input_activity_name(self, activity_name):
        self.send_text(loc.Activity.loc_search2, activity_name)

    @allure.step('点击活动')
    def click_activity(self):
        self.click_ele(loc.Activity.loc_activity_name)
