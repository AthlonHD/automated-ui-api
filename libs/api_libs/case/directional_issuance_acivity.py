# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


"""
定向发券活动测试用例
"""

import json
from libs.selenium_libs.common import base
from apis.uat30 import Uat30
from libs.env_conf import config as env_conf


class DirectionalIssuanceActivity:

    def __init__(self):
        self.r = Uat30()
        self.path = env_conf.path

    # 不使用券包
    def add_coupons_activity(self):
        with open(env_conf.path + r'\use_case\directional_issuance_data\coupons.json', encoding='utf-8') as f:
            data = f.read()
        name = '定向发单张券（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.add_directional_issuance(data.encode('utf-8'))
        return r.text, activity_name

    # 使用券包
    def add_coupons_bag_activity(self):
        with open(env_conf.path + r'\use_case\directional_issuance_data\coupons_bag.json', encoding='utf-8') as f:
            data = f.read()
        name = '定向发券包（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.add_directional_issuance(data.encode('utf-8'))
        return r.text, activity_name

    # 发送卡券
    def send_coupons(self, activity_id, member_id):
        body = {
            "id": activity_id,
            "channelID": 0,
            "pattern": 1,
            "memberCard": member_id
        }
        r = self.r.send_coupons(json.dumps(body))
        return r.text


if __name__ == '__main__':
    r = DirectionalIssuanceActivity().send_coupons('F98755D56E3EDAA2', '860000000129331')
    print(r)
