# -*- coding=utf-8 -*-
# ! /usr/bin/env python3

"""
活动公告用例-H5
"""

import time
from libs.selenium_libs.common import loc
from libs.selenium_libs.common.base import Base


class ActivityNotice(Base):

    def join_activity_notice(self, activity_name):
        # 进入活动页面，等待
        self.go_activity()
        time.sleep(2)
        # 点击搜索框
        loc_search1 = self.driver.find_elements_by_xpath(loc.Activity.loc_search1)[-1]
        loc_search1.click()
        # 在搜索框中输入活动名称
        self.send_text(loc.Activity.loc_search2, activity_name)
        time.sleep(2)
        # 点击活动搜索后的第一个活动
        if self.find_ele(loc.Activity.loc_activity_name):
            self.click_ele(loc.Activity.loc_activity_name)
            # 当前页面活动名称
            time.sleep(1)
            name = self.driver.find_elements_by_xpath('//div[contains(@class,"shop_detail_wrap")]/div[1]')[-1].text
        else:
            name = None
        return name

