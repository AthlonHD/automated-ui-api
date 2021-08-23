# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import allure
from libs.selenium_libs.common.base import Base
from selenium.webdriver.support.select import Select
from libs.env_conf import config as env_conf


class ActivityAudit(Base):
    @allure.step('活动审核')
    def activity_notice_uat(self, text, activity_name):
        path = env_conf.path
        self.driver.get(path + r'activity_audit/AuditActivity.html')
        self.driver.maximize_window()
        activity_type = self.driver.find_element_by_id('ActivityTableName')
        Select(activity_type).select_by_visible_text(text)
        activity_name1 = self.driver.find_element_by_id('ActivityName')
        activity_name1.send_keys(activity_name)
        shenhe = self.driver.find_element_by_id('But_ShenHe')
        shenhe.click()