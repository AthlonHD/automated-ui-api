# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import json
import time
import pytest
import allure
from apis.uat30 import Uat30
from libs.api_libs.case.directional_issuance_acivity import DirectionalIssuanceActivity as DI
from libs.selenium_libs.common import loc
from libs.selenium_libs.common.activity_audit import ActivityAudit
from libs.selenium_libs.common.base import Base


@allure.feature('定向发券')
class TestDirectionalIssuanceActivity:

    @allure.title('14335-定向发券-单张卡券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14335/')
    def test_directional_issuance_activity_01(self, driver):
        """
        测试定向发券活动，单张卡券
        """
        # 接口创建定向发券活动
        r = DI().add_coupons_activity()
        response = json.loads(r[0])  # 接口响应值
        activity_name = r[1]  # 活动名称
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('定向发券', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '26')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'
        # 发放卡券前验证卡券数量
        Base(driver).go_user_center()
        time.sleep(2)
        card_amount_start = int(driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_card_bag_amount)[-1].text)
        # 发放卡券
        DI().send_coupons(activity_id, '860000000129331')
        # 发放卡券后验证卡券数量
        Base(driver).go_user_center()
        time.sleep(2)
        card_amount_end = int(driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_card_bag_amount)[-1].text)
        assert card_amount_end - card_amount_start == 1
        # 获取的卡券名称
        driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_card_bag)[-1].click()
        coupons_name = Base(driver).find_ele(loc.MyCardBag.loc_first_coupon).text
        assert coupons_name == '商业代金券领取2天有用持续1天'
        # 撤回活动
        r = json.loads(Uat30().withdraw(activity_id, '26').text)
        assert r['message'] == "操作成功"

    @allure.title('14336-定向发券-券包')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14336/')
    def test_directional_issuance_activity_02(self, driver):
        """
        测试定向发券活动，使用券包
        """
        # 接口创建定向发券活动
        r = DI().add_coupons_bag_activity()
        response = json.loads(r[0])  # 接口响应值
        activity_name = r[1]  # 活动名称
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('定向发券', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '26')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'
        # 发放卡券前验证卡券数量
        Base(driver).go_user_center()
        time.sleep(2)
        card_amount_start = int(driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_card_bag_amount)[-1].text)
        # 发放卡券
        DI().send_coupons(activity_id, '860000000129331')
        # 发放卡券后验证卡券数量
        Base(driver).go_user_center()
        time.sleep(2)
        card_amount_end = int(driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_card_bag_amount)[-1].text)
        assert card_amount_end - card_amount_start == 5
        # 获取的卡券名称
        driver.find_elements_by_xpath(loc.PersonalCenter.loc_my_card_bag)[-1].click()
        time.sleep(2)
        coupons_name = driver.find_elements_by_xpath(loc.MyCardBag.loc_first_coupon)
        name = list()
        # 循环获取前5张卡券名称
        for i in coupons_name[:5]:
            name.append(i.text)
        assert '商业代金券领取2天有用持续1天' in name
        assert '礼品券-iPhone99一台' in name
        assert '1小时停车券' in name
        assert '一折优惠券' in name
        assert 'VR体验券' in name
        # 撤回活动
        r = json.loads(Uat30().withdraw(activity_id, '26').text)
        assert r['message'] == "操作成功"


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_directional_issuance_activity.py', '--alluredir', './report'])
