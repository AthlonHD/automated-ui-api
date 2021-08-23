# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import json
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apis.uat30 import Uat30
from libs.selenium_libs.case import login, log_out
from libs.api_libs.case.cj import Cj
from libs.selenium_libs.case.luck_draw_activity import LuckDrawActivity
from libs.selenium_libs.common import loc
from libs.selenium_libs.common.activity_audit import ActivityAudit
from libs.selenium_libs.common.base import Base
from libs.selenium_libs.page_object.page_personal_center import PagePersonalCenter


@allure.feature('抽奖摇一摇')
class Testcj:

    @allure.title('01——1.抽奖次数无限制 2.免费抽奖3.奖池为空时不可以继续抽奖（2个积分奖品')
    @allure.severity('critical')
    def test_cj01(self, driver):
        """
        活动-抽奖验证：1.抽奖次数无限制 2.免费抽奖3.奖池为空时不可以继续抽奖（2个积分奖品）
        """
        # 创建摇一摇抽奖活动
        r = Cj().add_cj01()
        response = json.loads(r[0])
        activity_name = r[1]
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('抽奖', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 添加奖品
        Cj().add_jinmgpin01(activity_id)
        # 查询奖品id
        jiangpin = Uat30().chxunjingpin(activity_id).text
        test_json = json.loads(jiangpin)
        jiangpinid = test_json['body']['list'][0]['id']
        jiangpinid01 = test_json['body']['list'][1]['id']
        strjingpinid = str(jiangpinid)
        jiangpinid01 = str(jiangpinid01)
        # 总奖品领取数
        total = test_json['body']['list'][0]['total'] + test_json['body']['list'][1]['total']
        # 上架奖品
        TEST = Uat30().shangjiajp(strjingpinid).text
        TESTs = Uat30().shangjiajp(jiangpinid01).text
        test_json = json.loads(TEST)
        test_jsons = json.loads(TESTs)
        jiangpinid = test_json['message']
        jiangpinids = test_jsons['message']
        assert jiangpinid == '操作成功'
        assert jiangpinids == '操作成功'
        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '6')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'

        flag = True
        i = 0
        while flag:
            start = LuckDrawActivity(driver).join_luck_draw_activity(driver, activity_name)
            # 开始积分
            integral_start = start[0]
            # 开始卡券数
            coupon_amount_start = start[1]
            # 切换到frame
            driver.switch_to.frame(0)
            time.sleep(1)
            # 点击立即抽奖
            driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
            # 判断奖品是否领完，False-领完
            try:
                WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@class="dialogue_content"]')))
                flag = False
            except:
                flag = True
            finally:
                i += 1
            # 进入个人中心页面
            Base(driver).go_user_center()
            time.sleep(2)
            # 获取当前积分
            integral_end = PagePersonalCenter(driver).get_my_integral()
            # 获取当前卡券数
            coupon_amount_end = PagePersonalCenter(driver).get_my_coupon_amount()
            if flag:
                assert int(coupon_amount_start) == int(coupon_amount_end)
                assert int(integral_start) + 5 == int(integral_end)
            else:
                pass
        assert i - int(total) == 1

    @allure.title('02——1.总抽奖次数为2次 2.消耗2积分抽奖 3.不可多次中奖4.奖池为空可继续抽奖（只有一个积分奖品）')
    @allure.severity('critical')
    def test_cj02(self, driver):
        """
        活动-抽奖验证：1.总抽奖次数为2次 2.消耗2积分抽奖 3.不可多次中奖4.奖池为空可继续抽奖（只有一个积分奖品）
        """
        r = Cj().add_cj02()
        response = json.loads(r[0])
        activity_name = r[1]
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('抽奖', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 查询奖品id
        jiangpin = Uat30().chxunjingpin(activity_id).text
        test_json = json.loads(jiangpin)
        jiangpinid = test_json['body']['list'][0]['id']
        strjingpinid = str(jiangpinid)
        # 上架奖品
        TEST = Uat30().shangjiajp(strjingpinid).text
        test_json = json.loads(TEST)
        jiangpinid = test_json['message']
        assert jiangpinid == '操作成功'

        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '6')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'

        flag = True
        total = 1  # 礼品数量
        i = 0
        while flag:
            # H5页面参加活动
            start = LuckDrawActivity(driver).join_luck_draw_activity(driver, activity_name)
            # 开始积分
            integral_start = start[0]
            # 开始卡券数
            coupon_amount_start = start[1]
            # 切换到frame
            driver.switch_to.frame(0)
            time.sleep(1)
            # 点击立即抽奖
            driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
            # 判断奖品是否领完，False-领完
            try:
                WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@class="dialogue_content"]')))
                flag = False
            except:
                flag = True
            finally:
                i += 1
            # 进入个人中心页面
            Base(driver).go_user_center()
            time.sleep(2)
            # 获取当前积分
            integral_end = PagePersonalCenter(driver).get_my_integral()
            # 获取当前卡券数
            coupon_amount_end = PagePersonalCenter(driver).get_my_coupon_amount()
            if flag:
                assert int(coupon_amount_start) == int(coupon_amount_end)
                assert int(integral_start) + 3 == int(integral_end)
            else:
                pass
        assert i - int(total) == 1

        # 退出当前账号
        log_out.Logout(driver).log_out()
        # 登录账号
        time.sleep(2)
        login.Login(driver).login('18305632668')
        # H5页面参加活动
        start = LuckDrawActivity(driver).join_luck_draw_activity(driver, activity_name)
        # 开始积分
        integral_start = start[0]
        # 开始卡券数
        coupon_amount_start = start[1]
        # 切换到frame
        driver.switch_to.frame(0)
        time.sleep(1)
        # 点击立即抽奖
        driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
        time.sleep(1)
        tips = driver.find_element_by_xpath('//div[@class="dialogue_content"]').text
        assert tips == '本活动太火爆了，已经没有参与机会了，请关注其它更多活动吧'
        # 进入个人中心页面
        Base(driver).go_user_center()
        time.sleep(2)
        # 获取当前积分
        integral_end = PagePersonalCenter(driver).get_my_integral()
        # 获取当前卡券数
        coupon_amount_end = PagePersonalCenter(driver).get_my_coupon_amount()
        assert int(coupon_amount_start) == int(coupon_amount_end)
        assert int(integral_start) == int(integral_end)

    @allure.title('03——1.单用户抽奖次数1次 2.验证2积分（5个卡券包）')
    @allure.severity('critical')
    def test_cj03(self, driver):
        """
        活动-抽奖验证：1.单用户抽奖次数1次 2.验证2积分（5个卡券包）
        """
        # 接口创建抽奖活动
        r = Cj().add_cj03()
        response = json.loads(r[0])
        activity_name = r[1]
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('抽奖', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']

        # 查询奖品id
        jiangpin = Uat30().chxunjingpin(activity_id).text
        test_json = json.loads(jiangpin)
        jiangpinid = test_json['body']['list'][0]['id']
        strjingpinid = str(jiangpinid)

        # 上架奖品
        TEST = Uat30().shangjiajp(strjingpinid).text
        test_json = json.loads(TEST)
        jiangpinid = test_json['message']
        assert jiangpinid == '操作成功'

        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '6')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'

        flag = True
        total = 1  # 用户可领取数量
        i = 0
        while flag:
            # H5页面参加活动
            start = LuckDrawActivity(driver).join_luck_draw_activity(driver, activity_name)
            # 开始积分
            integral_start = start[0]
            # 开始卡券数
            coupon_amount_start = start[1]
            # 切换到frame
            driver.switch_to.frame(0)
            time.sleep(1)
            if int(integral_start) > 2:
                # 点击立即抽奖
                driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
                # 判断奖品是否领完，False-领完
                try:
                    WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[@class="dialogue_content"]')))
                    flag = False
                except:
                    flag = True
                finally:
                    i += 1
                # 进入个人中心页面
                Base(driver).go_user_center()
                time.sleep(2)
                # 获取当前积分
                integral_end = PagePersonalCenter(driver).get_my_integral()
                # 获取当前卡券数
                coupon_amount_end = PagePersonalCenter(driver).get_my_coupon_amount()
                if flag:
                    assert int(coupon_amount_start) + 1 == int(coupon_amount_end)
                    assert int(integral_start) == int(integral_end)
                    # 进入卡包
                    driver.find_element_by_xpath(loc.PersonalCenter.loc_my_card_bag).click()
                    time.sleep(1)
                    coupon_name = Base(driver).find_ele(loc.MyCardBag.loc_first_coupon).text
                    assert coupon_name == '礼品券-iPhone99一台'
                else:
                    assert int(integral_start) == int(integral_end)
                    assert int(coupon_amount_start) == int(coupon_amount_end)
            else:
                # 点击立即抽奖
                driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
                tips = Base(driver).find_ele('//div[@class="dialogue_content"]').text
                assert tips == '您的积分余额不足,暂无法参与此活动!'
        assert i - int(total) == 1

        # # 账号退出再重新登录，验证积分不满足2积分
        # log_out.Logout(driver).log_out()
        # login.Login(driver).login('18399999999')
        # flag = True
        # total = 1  # 用户可领取数量
        # i = 0
        # while flag:
        #     # H5页面参加活动
        #     start = LuckDrawActivity(driver).join_luck_draw_activity(driver, activity_name)
        #     # 开始积分
        #     integral_start = start[0]
        #     # 开始卡券数
        #     coupon_amount_start = start[1]
        #     # 切换到frame
        #     driver.switch_to.frame(0)
        #     time.sleep(1)
        #     if int(integral_start) > 2:
        #         # 点击立即抽奖
        #         driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
        #         # 判断奖品是否领完，False-领完
        #         try:
        #             WebDriverWait(driver, 5).until(
        #                 EC.visibility_of_element_located((By.XPATH, '//div[@class="dialogue_content"]')))
        #             flag = False
        #         except:
        #             flag = True
        #         finally:
        #             i += 1
        #         # 进入个人中心页面
        #         Base(driver).go_user_center()
        #         time.sleep(2)
        #         # 获取当前积分
        #         integral_end = PagePersonalCenter(driver).get_my_integral()
        #         # 获取当前卡券数
        #         coupon_amount_end = PagePersonalCenter(driver).get_my_coupon_amount()
        #         if flag:
        #             assert int(coupon_amount_start) + 1 == int(coupon_amount_end)
        #             assert int(integral_start) == int(integral_end)
        #             # 进入卡包
        #             driver.find_element_by_xpath(loc.PersonalCenter.loc_my_card_bag).click()
        #             time.sleep(1)
        #             coupon_name = Base(driver).find_ele(loc.MyCardBag.loc_first_coupon).text
        #             assert coupon_name == '礼品券-iPhone99一台'
        #         else:
        #             assert int(integral_start) == int(integral_end)
        #             assert int(coupon_amount_start) == int(coupon_amount_end)
        #     else:
        #         # 点击立即抽奖
        #         time.sleep(1)
        #         driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
        #         tips = Base(driver).find_ele('//div[@class="dialogue_content"]').text
        #         assert tips == '您的积分余额不足,暂无法参与此活动!'
        # assert i - int(total) == 1

        # 账号退出再重新登录，验证可再次领券
        log_out.Logout(driver).log_out()
        login.Login(driver).login('15738995325')
        flag = True
        total = 1  # 用户可领取数量
        i = 0
        while flag:
            # H5页面参加活动
            start = LuckDrawActivity(driver).join_luck_draw_activity(driver, activity_name)
            # 开始积分
            integral_start = start[0]
            # 开始卡券数
            coupon_amount_start = start[1]
            # 切换到frame
            driver.switch_to.frame(0)
            time.sleep(2)
            if int(integral_start) > 2:
                # 点击立即抽奖
                driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
                # 判断奖品是否领完，False-领完
                try:
                    WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, '//div[@class="dialogue_content"]')))
                    flag = False
                except:
                    flag = True
                finally:
                    i += 1
                # 进入个人中心页面
                Base(driver).go_user_center()
                Base(driver).implicitly_wait()
                # 获取当前积分
                integral_end = PagePersonalCenter(driver).get_my_integral()
                # 获取当前卡券数
                coupon_amount_end = PagePersonalCenter(driver).get_my_coupon_amount()
                if flag:
                    assert int(coupon_amount_start) + 1 == int(coupon_amount_end)
                    assert int(integral_start) == int(integral_end)
                    # 进入卡包
                    driver.find_element_by_xpath(loc.PersonalCenter.loc_my_card_bag).click()
                    time.sleep(1)
                    coupon_name = Base(driver).find_ele(loc.MyCardBag.loc_first_coupon).text
                    assert coupon_name == '礼品券-iPhone99一台'
                else:
                    assert int(integral_start) == int(integral_end)
                    assert int(coupon_amount_start) == int(coupon_amount_end)
            else:
                # 点击立即抽奖
                driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
                tips = Base(driver).find_ele('//div[@class="dialogue_content"]').text
                assert tips == '您的积分余额不足,暂无法参与此活动!'
        assert i - int(total) == 1

    @allure.title('04——1.单用户每场仅能抽3次2.免费抽，可以多次中奖3.奖池为空时不能继续抽奖(5个卡券)')
    @allure.severity('critical')
    def test_cj04(self, driver):
        """
        活动-抽奖验证：单用户每场仅能抽3次2.免费抽，可以多次中奖3.奖池为空时不能继续抽奖(5个卡券)
        """
        r = Cj().add_cj04()
        response = json.loads(r[0])
        activity_name = r[1]
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('抽奖', activity_name)
        # 获取活动详情

        activity_details = Uat30().activity_details(activity_name).json()

        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']

        # 查询奖品id
        jiangpin = Uat30().chxunjingpin(activity_id).text
        test_json = json.loads(jiangpin)
        jiangpinid = test_json['body']['list'][0]['id']
        strjingpinid = str(jiangpinid)

        # 上架奖品
        TEST = Uat30().shangjiajp(strjingpinid).text
        test_json = json.loads(TEST)
        jiangpinid = test_json['message']
        assert jiangpinid == '操作成功'

        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '6')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'

        flag = True
        total = 3  # 单用户可领取数量
        i = 0  # 轮次
        k = 5  # 卡券数

        while flag:
            if i == 4:
                log_out.Logout(driver).log_out()
                login.Login(driver).login('18305632668')
            else:
                pass
            # H5页面参加活动
            start = LuckDrawActivity(driver).join_luck_draw_activity(driver, activity_name)
            # 开始积分
            integral_start = start[0]
            # 开始卡券数
            coupon_amount_start = start[1]
            # 切换到frame
            driver.switch_to.frame(0)
            time.sleep(1)
            # 点击立即抽奖
            driver.find_element_by_xpath(loc.Activity.loc_draw_immediately).click()
            # 判断单用户奖品是否领完，False-领完
            try:
                WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@class="dialogue_content"]')))
                flag1 = False
                if k == 0:
                    flag = False
                else:
                    flag = True
            except:
                flag1 = True
                flag = True
                k -= 1
            finally:
                i += 1
            # 进入个人中心页面
            Base(driver).go_user_center()
            driver.refresh()
            time.sleep(2)
            # 获取当前积分
            integral_end = PagePersonalCenter(driver).get_my_integral()
            # 获取当前卡券数
            coupon_amount_end = PagePersonalCenter(driver).get_my_coupon_amount()
            if flag1:
                assert int(coupon_amount_start) + 1 == int(coupon_amount_end)
                assert int(integral_start) == int(integral_end)
                # 进入卡包
                driver.find_element_by_xpath(loc.PersonalCenter.loc_my_card_bag).click()
                time.sleep(1)
                coupon_name = Base(driver).find_ele(loc.MyCardBag.loc_first_coupon).text
                assert coupon_name == 'VR体验券'
            else:
                assert int(integral_start) == int(integral_end)
                assert int(coupon_amount_start) == int(coupon_amount_end)
                if i < k:
                    assert i - int(total) == 1

    @allure.title('05——前台不显示')
    @allure.severity('critical')
    def test_cj05(self, driver):
        """
        前台不显示
        """
        r = Cj().add_cj05()
        response = json.loads(r[0])

        activity_name = r[1]
        assert response['message'] == '操作成功'

        # iwf审核
        ActivityAudit(driver).activity_notice_uat('抽奖', activity_name)
        # 获取活动详情

        activity_details = Uat30().activity_details(activity_name).json()

        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']

        # 查询奖品id
        jiangpin = Uat30().chxunjingpin(activity_id).text
        test_json = json.loads(jiangpin)
        jiangpinid = test_json['body']['list'][0]['id']
        strjingpinid = str(jiangpinid)

        # 上架奖品
        TEST = Uat30().shangjiajp(strjingpinid).text
        test_json = json.loads(TEST)
        jiangpinid = test_json['message']
        assert jiangpinid == '操作成功'

        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '6')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'

        # H5页面参加活动
        # 进入活动页面，等待
        Base(driver).go_activity()
        time.sleep(2)
        # 点击搜索框
        loc_search1 = driver.find_elements_by_xpath(loc.Activity.loc_search1)[-1]
        loc_search1.click()
        # 在搜索框中输入活动名称
        Base(driver).send_text(loc.Activity.loc_search2, activity_name)
        time.sleep(2)
        # 点击活动搜索后的第一个活动
        if Base(driver).find_ele(loc.Activity.loc_activity_name):
            Base(driver).click_ele(loc.Activity.loc_activity_name)
            # 当前页面活动名称
            time.sleep(1)
            name = driver.find_elements_by_xpath('//div[contains(@class,"shop_detail_wrap")]/div[1]')[-1].text
        else:
            name = None
        assert name is None
