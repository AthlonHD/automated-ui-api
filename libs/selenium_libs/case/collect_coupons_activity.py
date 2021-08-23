# -*- coding=utf-8 -*-
# ! /usr/bin/env python3

"""
领券活动
"""

import time
from libs.selenium_libs.common import loc
from libs.selenium_libs.common.base import Base


class CollectCouponsActivity(Base):

    def join_activity(self, activity_name):
        # 获取当前积分
        self.go_user_center()
        time.sleep(3)
        start_integral = self.driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_integral)[-2].text
        time.sleep(2)
        # 进入活动页面，等待
        self.go_activity()
        time.sleep(2)
        # 点击搜索框
        loc_search1 = self.driver.find_elements_by_xpath(loc.Activity.loc_search1)[1]
        loc_search1.click()
        # 在搜索框中输入活动名称
        self.send_text(loc.Activity.loc_search2, activity_name)
        time.sleep(2)
        # 点击活动搜索后的第一个活动
        self.click_ele(loc.Activity.loc_activity_name)
        # 检查参与活动方式
        way = self.find_ele(loc.Activity.loc_join_way).text
        if way == '免费':
            print('走免费领券流程')
            deduct_integral = 0
            # 点击我要领券
            self.click_ele(loc.Activity.loc_collect_coupons)
            time.sleep(2)
            # 获取个人中心页面
            self.go_user_center()
            time.sleep(3)
            # 再次获取个人积分
            end_integral = self.driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_integral)[-2].text
            time.sleep(3)
            # 点击我的卡包
            self.click_ele(loc.PersonalCenter.loc_my_card_bag)
            time.sleep(1.5)
            # 获取卡券名称
            text = self.find_ele(loc.MyCardBag.loc_first_coupon).text
        else:
            print('走领券扣积分')
            deduct_integral = way[:-3]
            print('抵扣积分:' + str(deduct_integral))
            # 点击我要领券
            self.click_ele(loc.Activity.loc_collect_coupons)
            time.sleep(2)
            # 点击确定按钮
            self.driver.switch_to.default_content()
            self.click_ele(loc.Activity.loc_define)
            time.sleep(2)
            # 获取个人中心页面
            self.go_user_center()
            # 再次获取个人积分
            time.sleep(3)
            end_integral = self.driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_integral)[-2].text
            time.sleep(1)
            # 点击我的卡包
            self.click_ele(loc.PersonalCenter.loc_my_card_bag)
            time.sleep(2)
            # 获取卡券名称
            text = self.find_ele(loc.MyCardBag.loc_first_coupon).text
        return text, start_integral, deduct_integral, end_integral
