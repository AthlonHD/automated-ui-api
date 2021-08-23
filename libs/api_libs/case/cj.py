# -*- coding=utf-8 -*-
# ! /usr/bin/env python3

"""
活动摇一摇抽奖用例
"""

from libs.env_conf import config as env_conf
from libs.selenium_libs.common import base
from apis.uat30 import Uat30


class Cj:

    """
    摇一摇抽奖
    """

    def __init__(self):
        self.r = Uat30()
        self.path = env_conf.path

    # 活动-抽奖验证：1.抽奖次数无限制2.免费抽奖3.奖池为空时不可以继续抽奖（2个积分奖品）
    def add_cj01(self):
        with open(env_conf.path + r'\use_case\draw_shake_date\shake_1.json', encoding='utf-8') as f:
            data = f.read()
        name = '摇一摇1（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addcj(data.encode('utf-8'))
        return r.text, activity_name

    # 添加奖品
    def add_jinmgpin01(self, activity_id):
        with open(env_conf.path + r'\use_case\draw_shake_date\shake_tianjiajingopin.json', encoding='utf-8') as f:
            data = f.read()
            activityId = 'E075F4EB1606E98C'
            # replace(“目标值”,“替换值”).astype(“目标类型”)
        data = data.replace(activityId, activity_id)
        r = self.r.addjp(data.encode('utf-8'))
        return r.text

    # 活动-抽奖验证：1.总抽奖次数为2次2.消耗2积分抽奖3.不可多次中奖4.奖池为空可继续抽奖（只有一个积分奖品）
    def add_cj02(self):
        with open(env_conf.path + r'\use_case\draw_shake_date\shake_2.json', encoding='utf-8') as f:
            data = f.read()
        name = '摇一摇2（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addcj(data.encode('utf-8'))
        return r.text, activity_name

    # 活动-抽奖验证：1.单用户抽奖次数1次2.验证2积分（5个卡券包）
    def add_cj03(self):
        with open(env_conf.path + r'\use_case\draw_shake_date\shake_3.json', encoding='utf-8') as f:
            data = f.read()
        name = '摇一摇3（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addcj(data.encode('utf-8'))
        return r.text, activity_name

    # 活动-抽奖验证：单用户每场仅能抽3次2.免费抽，可以多次中奖3.奖池为空时不能继续抽奖(5个卡券)
    def add_cj04(self):
        with open(env_conf.path + r'\use_case\draw_shake_date\shake_4.json', encoding='utf-8') as f:
            data = f.read()
        name = '摇一摇4（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addcj(data.encode('utf-8'))
        return r.text, activity_name

    # 活动-抽奖验证：1.前台不显示
    def add_cj05(self):
        with open(env_conf.path + r'\use_case\draw_shake_date\shake_5.json', encoding='utf-8') as f:
            data = f.read()
        name = '摇一摇5（测试专用领取无效）'
        activity_name = name + base.get_time_stamp()
        data = data.replace(name, activity_name)
        r = self.r.addcj(data.encode('utf-8'))
        return r.text, activity_name


if __name__ == '__main__':
    r = Cj().add_jinmgpin01('FB9E270A2878117C')
    print(r[0])
