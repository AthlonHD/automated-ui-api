# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import json
from libs.selenium_libs.case import collect_coupons_activity
from libs.selenium_libs.common import activity_audit
from test_cases.case_modifymemberbanknoteInfo import ModifyMemberBankNoteInfo
from apis.uat30 import Uat30
from libs.env_conf import config as env_conf
import pytest
import allure

path = env_conf.path


@allure.feature('领券活动')
class TestCollectCouponsActivity:

    @allure.title('14399——免费领取代金券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14339/')
    def test_collect_coupons_activity_01(self, driver):
        """
        免费领取代金券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_memberbanknoteinfo())
        print(response)
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
                print(activity_name)
            coupons_name = '卡券每满10元减5元'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            with allure.step('发布活动'):
                pass
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            with allure.step('验证获取卡券'):
                pass
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            with allure.step('验证参与活动前后积分正确'):
                pass
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 查看卡券管理获取卡券id
            coupons_mange = Uat30().card_manage(activity_id).json()
            coupons_id = coupons_mange['body']['list'][0]['id']
            # 验证会员
            coupons = Uat30().card_collection_details(coupons_id).json()
            member_card_no = str(coupons['body']['list'][0]['memberCardNo'])
            with allure.step('验证会员'):
                pass
            assert member_card_no == '860000000129331'
            # 卡券管理
            card_manage = Uat30().card_manage(activity_id).json()
            # 剩余卡券数
            surplus_coupons = int(card_manage['body']['list'][0]['stockCount'])
            # 卡券总数
            total_coupons = int(card_manage['body']['list'][0]['totalNum'])
            # 领券数
            collect_coupons = int(card_manage['body']['list'][0]['totalReward'])
            with allure.step('领券数'):
                pass
            assert total_coupons == surplus_coupons + collect_coupons

            # 退还卡券
            tui = json.loads(Uat30().tuihuan(activity_id).text)
            tuihuan = tui['message']
            with allure.step('退还卡券'):
                pass
            assert tuihuan == '操作成功'

            # 卡券管理
            card_manage = Uat30().card_manage(activity_id).json()
            # 剩余卡券数
            surplus_coupons = int(card_manage['body']['list'][0]['stockCount'])
            # 卡券总数
            total_coupons = int(card_manage['body']['list'][0]['totalNum'])
            # 领券数
            collect_coupons = int(card_manage['body']['list'][0]['totalReward'])
            with allure.step('领券数'):
                pass
            assert surplus_coupons == 0
            assert total_coupons == surplus_coupons + collect_coupons
            # 撤回活动
            Uat30().withdraw(activity_id, '8')

        else:
            print('—————————— 测试用例 lqhd_001接口失败，跳过UI验证 ——————————')

    @allure.title('14399——免费领取礼品券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14339/')
    def test_collect_coupons_activity_02(self, driver):
        """
        免费领取礼品券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_free_lipin())
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '卡券核销复测券'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            with allure.step('发布活动'):
                pass
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            with allure.step('验证获取卡券'):
                pass
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            with allure.step('验证参与活动前后积分正确'):
                pass
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_002接口失败，跳过UI验证 ——————————')

    @allure.title('14399——免费领取停车券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14339/')
    def test_collect_coupons_activity_03(self, driver):
        """
        免费领取停车券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_free_tingche())
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '0507停车券可抵扣5元'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            with allure.step('发布活动'):
                pass
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            with allure.step('验证获取卡券'):
                pass
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            with allure.step('验证参与活动前后积分正确'):
                pass
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_003接口失败，跳过UI验证 ——————————')

    @allure.title('14399——免费领取体验券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14339/')
    def test_collect_coupons_activity_04(self, driver):
        """
        免费领取体验券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_free_tiyan())
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '体验券名1234'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            with allure.step('发布活动'):
                pass
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            with allure.step('验证获取卡券'):
                pass
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            with allure.step('验证参与活动前后积分正确'):
                pass
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_004接口失败，跳过UI验证 ——————————')

    @allure.title('14399——免费领取折扣券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14339/')
    def test_collect_coupons_activity_05(self, driver):
        """
        免费领取折扣券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_free_zhekou())
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '0615平台折扣券'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_005接口失败，跳过UI验证 ——————————')

    @allure.title('14334——1积分领取代金券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14334/')
    def test_collect_coupons_activity_06(self, driver):
        """
        1积分领取代金券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_point_daijin())
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '卡券每满10元减5元'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_006接口失败，跳过UI验证 ——————————')

    @allure.title('14334——1积分领取礼品券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14334/')
    def test_collect_coupons_activity_07(self, driver):
        """
        1积分领取礼品券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_point_lipin())
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '卡券核销复测券'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_007接口失败，跳过UI验证 ——————————')

    @allure.title('14334——1积分领取停车券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14334/')
    def test_collect_coupons_activity_08(self, driver):
        """
        1积分领取停车券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_point_tingche())
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '0507停车券可抵扣5元'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_008接口失败，跳过UI验证 ——————————')

    @allure.title('14334——1积分领取体验券')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14334/')
    def test_collect_coupons_activity_09(self, driver):
        """
        1积分领取体验券
        """
        response = json.loads(ModifyMemberBankNoteInfo().modify_point_tiyan())
        response_assert = response['message']
        if response_assert == '操作成功':
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '体验券名1234'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_009接口失败，跳过UI验证 ——————————')

    @allure.title('14334——消耗积分领取券包')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/14334/')
    def test_collect_coupons_activity_10(self, driver):
        """
        1积分领取折扣券
        """
        # 调用接口创建，编辑活动
        response = json.loads(ModifyMemberBankNoteInfo().modify_point_zhekou())
        response_assert = response['message']
        if response_assert == '操作成功':
            # 读取活动名称
            with open(path + r'test_cases/activity_name.txt', encoding='utf-8') as f:
                activity_name = f.read()
            coupons_name = '自动化礼品券'
            # iwf审核
            activity_audit.ActivityAudit(driver).activity_notice_uat('领券', activity_name)
            # 活动详情
            activity_details = Uat30().activity_details(activity_name).json()
            # 获取活动对应id
            activity_id = activity_details['body']['list'][0]['id']
            # 发布活动
            response_fabu = Uat30().fabu(activity_id, '8')
            test_json = json.loads(response_fabu.text)
            assert test_json['message'] == '操作成功'
            # H5页面参与活动
            r = collect_coupons_activity.CollectCouponsActivity(driver).join_activity(activity_name)
            # 验证获取卡券
            assert coupons_name == r[0]
            # 验证参与活动前后积分正确
            # r[1]为初始积分，r[2]为抵扣积分，r[3]为活动结束积分
            assert int(r[1]) - int(r[2]) == int(r[3])
            # 撤回活动
            Uat30().withdraw(activity_id, '8')
        else:
            print('—————————— 测试用例 lqhd_010接口失败，跳过UI验证 ——————————')

    # def test_collect_coupons_activity_11(self, driver): """ 新增窗口，测试未登录与会员积分为零情况 """ # 新建窗口 js = 'window.open(
    # "https://mall30uat.capitaland.com.cn/#/activity_list?mallId=88&portalId=74&__key=url_1624865966602_34")'
    # driver.execute_script(js) # 获取所有句柄 handles = driver.window_handles print(handles) # 进入新窗口
    # driver.switch_to.window(handles[1]) print(driver.current_url) with open(r'activity_name.txt') as f:
    # activity_name = f.read() ele1 = driver.find_element_by_xpath('//div[contains(@class,"shop_search")]')[]
    # ele1.click() ele2 = driver.find_element_by_xpath('//input[contains(@class,"shop_search")]') ele2.send_keys(
    # activity_name) ele3 = driver.find_element_by_xpath('//div[contains(@class,"search_list_list--1Dvrj")]')
    # ele3.click() ele4 = driver.find_element_by_xpath('//div/div[2]/div/div/div[3]/div/a[2]') ele4.click()
    # login.Login(driver).login('18399999999') # 点击我要领券 ele5 = driver.find_element_by_xpath('//span[contains(text(),
    # "我要领券")]') ele5.click() # 点击确定 ele6 = driver.find_element_by_xpath('//div[contains(@class,
    # "am-modal-button")]/a[2]') ele6.click() # 弹窗信息 ele7 = driver.find_element_by_xpath('//span/div/div/div') print(
    # ele7.text)


if __name__ == '__main__':
    pytest.main(['test_collect_coupons_activity.py'])
