# -*- coding=utf-8 -*-
# ! /usr/bin/env python3

"""
领券活动用例
"""

from libs.selenium_libs.common import base
from apis.uat30 import Uat30
from libs.env_conf import config as env_conf


class ModifyMemberBankNoteInfo:
    # 修改活动信息
    def __init__(self):
        self.r = Uat30()
        self.path = env_conf.path

    # lqhd_001
    def modify_memberbanknoteinfo(self):
        modify_name = '免费领代金券-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(modify_name)

        modify_data = env_conf.free_daijin_json
        modify_data = modify_data.replace('免费领代金券-测试专用领取无效', modify_name)
        data = self.r.add(modify_data.encode('utf-8'))
        return data.text

    # lqhd_002
    def modify_free_lipin(self):
        lipin_name = '免费领礼品券-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(lipin_name)

        lipin_data = env_conf.free_lipin_json
        lipin_data = lipin_data.replace('免费领礼品券', lipin_name)
        data = self.r.add(lipin_data.encode('utf-8'))
        return data.text

    # lqhd_003
    def modify_free_tingche(self):
        tingche_name = '免费领停车券-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(tingche_name)
        tingche_data = env_conf.free_tingche_json
        tingche_data = tingche_data.replace('免费领停车券', tingche_name)
        data = self.r.add(tingche_data.encode('utf-8'))
        return data.text

    # lqhd_004
    def modify_free_tiyan(self):
        tiyan_name = '免费领体验券' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(tiyan_name)

        tiyan_data = env_conf.free_tiyan_json
        tiyan_data = tiyan_data.replace('免费领体验券', tiyan_name)
        data = self.r.add(tiyan_data.encode('utf-8'))
        return data.text

    # lqhd_005
    def modify_free_zhekou(self):
        zhekou_name = '免费领折扣券-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(zhekou_name)

        zhekou_data = env_conf.free_zhekou_json
        zhekou_data = zhekou_data.replace('免费领折扣券', zhekou_name)
        data = self.r.add(zhekou_data.encode('utf-8'))
        return data.text

    # lqhd_006
    def modify_point_daijin(self):
        p_daijin_name = '积分领代金券-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(p_daijin_name)

        p_daijin_data = env_conf.point_daijin_json
        p_daijin_data = p_daijin_data.replace('1积分领代金券', p_daijin_name)
        data = self.r.add(p_daijin_data.encode('utf-8'))
        return data.text

    # lqhd_007
    def modify_point_lipin(self):
        p_lipin_name = '积分领礼品券-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(p_lipin_name)

        p_lipin_data = env_conf.point_lipin_json
        p_lipin_data = p_lipin_data.replace('1积分领礼品券', p_lipin_name)
        data = self.r.add(p_lipin_data.encode('utf-8'))
        return data.text

    # lqhd_008
    def modify_point_tingche(self):
        p_tingche_name = '积分领停车券-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(p_tingche_name)

        p_tingche_data = env_conf.point_tingche_json
        p_tingche_data = p_tingche_data.replace('1积分领停车券', p_tingche_name)
        data = self.r.add(p_tingche_data.encode('utf-8'))
        return data.text

    # lqhd_009
    def modify_point_tiyan(self):
        p_tiyan_name = '积分领体验券-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(p_tiyan_name)

        p_tiyan_data = env_conf.point_tiyan_json
        p_tiyan_data = p_tiyan_data.replace('1积分领体验券', p_tiyan_name)
        data = self.r.add(p_tiyan_data.encode('utf-8'))
        return data.text

    # lqhd_010
    def modify_point_zhekou(self):
        p_zhekou_name = '积分领券包-测试专用领取无效' + base.get_time_stamp()
        with open('./activity_name.txt', 'w', encoding=',utf-8') as f:
            f.write(p_zhekou_name)

        p_zhekou_data = env_conf.point_zhekou_json
        p_zhekou_data = p_zhekou_data.replace('积分领取券包', p_zhekou_name)
        data = self.r.add(p_zhekou_data.encode('utf-8'))
        return data.text


if __name__ == '__main__':
    print(ModifyMemberBankNoteInfo().modify_memberbanknoteinfo())
