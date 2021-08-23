# -*- coding=utf-8 -*-
# ! /usr/bin/env python3

"""
抽奖活动-摇一摇活动
"""

import time
import allure
from libs.selenium_libs.common.base import Base
from libs.selenium_libs.page_object.page_activity import PageActivity
from libs.selenium_libs.page_object.page_personal_center import PagePersonalCenter


class LuckDrawActivity(Base):
    @allure.step('参加抽奖活动')
    def join_luck_draw_activity(self, driver,activity_name):
        # 进入个人中心页面
        self.go_user_center()
        time.sleep(2)
        # 获取当前积分
        integral_start = PagePersonalCenter(driver).get_my_integral()
        # 获取当前卡券数
        coupon_amount_start = PagePersonalCenter(driver).get_my_coupon_amount()
        # 进入活动页面，等待
        self.go_activity()
        time.sleep(2)
        # 点击搜索框
        PageActivity(driver).click_search()
        # 在搜索框中输入活动名称
        PageActivity(driver).input_activity_name(activity_name)
        time.sleep(2)
        # 点击活动搜索后的第一个活动
        PageActivity(driver).click_activity()
        time.sleep(2)
        return integral_start, coupon_amount_start
        # # 检查参与活动方式
        # time.sleep(1)
        # way = self.driver.find_elements_by_xpath(loc.Activity.loc_luck_draw_rule)[-1].text
        # # 判断抽奖形式
        # if '凯德星会员即可参与抽奖' in way:
        #     print('免费抽奖')
        #     self.click_ele(loc.Activity.loc_draw_immediately)
        #     # 判断奖励类型
        #     # if self.driver.find_element_by_xpath('//div[@class="result_txt"]').text =="恭喜您抽中奖品是积分，立即兑换你想要的礼品吧！":
        #     # 进入个人中心页面
        #     self.go_user_center()
        #     time.sleep(2)
        #     # 获取当前积分
        #     integral_end = PagePersonalCenter.get_my_integral()
        #     # 获取当前卡券数
        #     coupon_amount_end = PagePersonalCenter.get_my_coupon_amount()
        # elif '每次抽奖消耗' in way:
        #     print('消耗积分抽奖')
        #     integral_end = 0
        #     coupon_amount_end = 0
        # else:
        #     print('验证积分抽奖')
        #     integral_end = 0
        #     coupon_amount_end = 0
        # return integral_start, coupon_amount_start, integral_end, coupon_amount_end

        # integral = filter(way.isdigit, way)
