# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import json
from libs.api_libs.api30 import Api30


class Uat30:
    """
    会员领券
    """

    def __init__(self):
        self.r = Api30()

    # 创建定向发券活动
    def add_directional_issuance(self, body):
        url = '/SaleSendCoupon/Add'
        response = self.r.post(url, linkpost='c', body=body)
        return response

    # 创建领券中心活动
    # 定向发券活动发送卡券
    def send_coupons(self, body=None):
        url = '/SaleSendCoupon/Send'
        response = self.r.post(url, linkpost='c', body=body)
        return response

    def add(self, body_data):
        r_api = '/SaleRewardCoupon/Add'
        r_response = self.r.post(r_api, linkpost='c', body=body_data)
        return r_response

    # 卡券领取详情
    def card_collection_details(self, coupons_id):
        url = '/Coupon/CouponReceiveHistory?id=' + str(coupons_id) + '&isUsed=false&page=1&pageSize=10'
        r_response = self.r.get(url, linkget='d')
        return r_response

    # 退还卡券库存
    def tuihuan(self, activity_id):
        tapi = '/Coupon/ReturnInventory?&type=8&id=' + str(activity_id)
        r_response = self.r.post(tapi, linkpost='d')
        return r_response

    # 通过活动id查看卡券id和卡券名
    def card_manage(self, activity_id):
        url = '/VTActivity/ActivityCoupon?page=1&pageSize=10&type=8&activityId=' + str(activity_id)
        r_response = self.r.get(url, linkget='c')
        return r_response

    # 发布活动
    def fabu(self, activity_id, type_id):
        """
        typeId=8:领券活动
        typeId=26：定向发券活动
        typeId=11：活动公告
        typeId=6:摇一摇抽奖
        """
        url = '/VTActivity/Publish?&typeId=' + str(type_id) + '&publishStatus=true&id=' + str(activity_id)
        r_r = self.r.post(url, linkpost='c')
        return r_r

    # 撤回活动
    def withdraw(self, activity_id, type_id):
        url = '/VTActivity/Publish?id=' + str(activity_id) + '&typeId=' + str(type_id) + '&reason=1&publishStatus=false'
        response = self.r.post(url, linkpost='c')
        return response

    # 根据活动名称查看活动详情
    def activity_details(self, activity_name):
        url = '/VTActivity/ViewList?page=1&pageSize=10&keyword=' + activity_name
        response = self.r.get(url, linkget='c')
        return response

    # 创建活动公告活动
    def addhdgongao(self, body_data):
        hdgg_api = '/SalePromotion/Add'
        pijie = self.r.post(hdgg_api, linkpost='c', body=body_data)
        return pijie

    # 创建抽奖活动
    def addcj(self, body_data):
        cj = '/SaleLuckDraw/Add'
        pinjiecj = self.r.post(cj, linkpost='c', body=body_data)
        return pinjiecj

    # 添加奖品
    def addjp(self, body_data):
        jpycc = '/Prize/Add'
        pingjieurl = self.r.post(jpycc, linkpost='c', body=body_data)
        return pingjieurl

    # 验证报表里的抽奖人
    def ynzhengcjr(self, body_data, activityid):
        jpycc = '/Activity/PrizeDetail?page=1&pageSize=10&id=' + activityid + '&activityType=6&prizeId=62538'
        pingjieurl = self.r.get(jpycc, linkget='c')
        return pingjieurl

    # 验证报表里的抽奖次数和参与人数和奖品领取数
    def ynzhengcj(self):
        cjyanzheng = '/Activity/Dashboard?id=D0AC4F061518C0A3&activityType=6'
        pingjieurl = self.r.get(cjyanzheng, linkget='c')
        return pingjieurl

    # 查询奖品
    def chxunjingpin(self, activityid):
        chxunjingpin = '/Prize/List?activityId=' + activityid + '&activityType=6&page=1&pageSize=9999'
        pingjieurl = self.r.get(chxunjingpin, linkget='c')
        return pingjieurl

    # 上架奖品
    def shangjiajp(self, jingpinid):
        shangji = '/Prize/Disable?id=' + jingpinid + '&activityType=6&valid=true'
        pingjieurl = self.r.post(shangji, linkpost='c')
        return pingjieurl


if __name__ == '__main__':
    # '''获取抽奖信息'''
    # test = Uat30().ynzhengcj().text
    # test_json = json.loads(test)
    # member_id = test_json['body'][0]['signCount']  # 参与人数
    # cj_quantity = test_json['body'][0]['totalReward'] # 奖品领取数
    # cj_jpquantity = test_json['body'][0]['luckdrawCount']   # 抽奖次数
    # print(member_id)
    # print(cj_quantity)
    # print(cj_jpquantity)
    # if member_id == '860000000128294':
    #     print('成功')
    # else:
    #     print('失败')
    #     '''获取奖品id''
    # test = Uat30().chxunjingpin('BE1EC0D26CEAAFF1').text
    # test_json = json.loads(test)
    # jiangpinid = test_json['body']['list'][0]['id']

    TEST = Uat30().shangjiajp('6285').text
    print(TEST)
    test_json = json.loads(TEST)
    jiangpinid = test_json['message']
    print(jiangpinid)
    # if member_id == '操作成功':
    #         print('成功')
    # else:
    #         print('失败')
# 获取活动id
# test = Uat30().chahd().text
# test_json = json.loads(test)
# hdslist = test_json['body']['list'][0]['id']
# print(hdslist)

# 通过活动读取到卡券id和卡券名和库存
# test = Uat30().chahd_kq().text
# test_json = json.loads(test)
# hdslist = test_json['body']['list'][0]['id']
# kqlistname = test_json['body']['list'][0]['name']
# kqshengyu = test_json['body']['list'][0]['coupon']['stockCount']
# print(kqlistname,hdslist,kqshengyu)
