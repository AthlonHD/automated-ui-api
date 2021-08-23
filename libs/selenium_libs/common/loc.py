# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


# 首页导航元素定位
class Home:
    loc_home = '//span[contains(text(),"首页")]'
    loc_activity = '//*[@id="root"]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/p/span'
    loc_news = '//span[contains(text(),"消息")]'
    loc_personal_center = '//span[contains(text(),"个人中心")]'


# 个人中心元素定位
class PersonalCenter:
    loc_login = '//div/div/div/div/div/div/h1'
    # 我的会员卡
    loc_my_member_card = '//a[contains(@class,"user_center_link_list")][2]/p'
    # 我的卡包
    loc_my_card_bag = '//a[contains(@class,"user_center_link_list")][3]/p'
    # 我的星积分
    loc_my_integral = '//div[contains(@class,"user_basic_info--XtJWO")]/div/a/h1'
    # 我的卡券数
    loc_my_card_bag_amount = '//h1[contains(@class,"hasnew")]'


# 登录页元素定位
class Login:
    loc_phone = '//body/div[1]/div[2]/div/div/div[3]/div[1]/div/label/input'
    # 获取验证码
    loc_get_verification_code = '//body/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div'
    # 输入验证码
    loc_input_verification_code = '//div/div/div/div[3]/div[2]/div[1]/label/input'
    # 勾选协议
    loc_check = '//div/div/div/div[3]/div[2]/div[2]/div/div/div/label/span/input'
    loc_login = '//div/div/div/div[3]/div[2]/div[2]/a'


# 我的会员卡里元素定位
class MyMemberCard:
    loc_my_card_no = '//div[contains(@class,"user_card_num")]'


# 活动页面里元素定位
class Activity:
    # 活动页面下的搜索框元素定位
    loc_search1 = '//div[contains(@class,"shop_search")]'
    loc_search2 = '//input[contains(@class,"shop_search")]'
    # 搜索后第一个活动元素定位
    loc_activity_name = '//div[contains(@class,"search_list_list--1Dvrj")]'

    # ****************** H5领券活动 ***************************************
    # 我要领券元素定位
    loc_collect_coupons = '//span[contains(text(),"我要领券")]'
    # 左下角活动参加方式元素定位
    loc_join_way = '//div[contains(@class,"left_get_coupon_title")]'
    # 点击确定按钮
    loc_define = '//div[contains(@class,"am-modal-button")]/a[2]'
    # *****************  H5抽奖活动 ************************************
    # 抽奖规则
    loc_luck_draw_rule = '//div[@class="lottery_join_tips"]'
    # 立即抽奖
    loc_draw_immediately = '//div[@class="lotteryShake_main_btns"]'


class MyCardBag:
    # 进入卡包后,排第一元素定位
    loc_first_coupon = '//div[contains(@class,"coupon_info_title")]'
