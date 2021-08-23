# -*- coding=utf-8 -*-
# ! /usr/bin/env python3

"""
活动公告用例
"""

from libs.env_conf import config as env_conf
from libs.selenium_libs.common import base
from apis.uat30 import Uat30


class Hdgg:

    def __init__(self):
        self.r = Uat30()
        self.path = env_conf.path

    # 01活动-活动公告3.0
    def add_hdgonggao(self):
        with open(env_conf.path + r'\use_case\notice_date\notice30.json', encoding='utf-8') as f:
            data = f.read()
        name = '公告3.0（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addhdgongao(data.encode('utf-8'))
        return r.text, activity_name

    # 02活动-为明天公告
    def add_weiming(self):
        with open(env_conf.path + r'\use_case\notice_date\for_tomorrow_notice.json', encoding='utf-8') as f:
            data = f.read()
        name = '为明天公告（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addhdgongao(data.encode('utf-8'))
        return r.text, activity_name

    # 03活动-为明天微刊
    def add_weikan(self):
        with open(env_conf.path + r'\use_case\notice_date\for_tomorrow_weikan.json', encoding='utf-8') as f:
            data = f.read()
        name = '为明天微刊（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addhdgongao(data.encode('utf-8'))
        return r.text, activity_name

    # 04活动-为明天新闻
    def add_weimingnews(self):
        with open(env_conf.path + r'\use_case\notice_date\for_tomorrow_news.json', encoding='utf-8') as f:
            data = f.read()
        name = '为明天新闻（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addhdgongao(data.encode('utf-8'))
        return r.text, activity_name

    # 05活动-3.0活动公告不在前台显示
    def add_nodisplay(self):
        with open(env_conf.path + r'\use_case\notice_date\notice3.0_Nodisplay.json', encoding='utf-8') as f:
            data = f.read()
        name = '活动公告不显示在前台（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addhdgongao(data.encode('utf-8'))
        return r.text, activity_name

if __name__ == '__main__':
    r = Hdgg().add_coupons_ming()
    print(r[0])
