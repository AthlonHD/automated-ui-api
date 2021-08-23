# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import pymssql


def get_verification_code(phone):
    """
    获取前端H5验证码
    """
    # 生产数据库地址
    # connect = pymssql.connect("tcp:cnliudu090.a9aaf93aa695.database.chinacloudapi.cn", "apps_viewer", "F*F)2fwei21joifN", "KD_Wathet_Member")

    # 测试数据库地址
    connect = pymssql.connect("10.171.109.6", "kd_weixin", "companycn_weixin_2014", "KD_Wathet_Member")
    cursor = connect.cursor()
    sql = "select verify_code from t_Member_Login_Code where phone=" + str(phone) + 'order by createTime desc'
    cursor.execute(sql)
    result = cursor.fetchall()
    code = str(result).split('\'')[1]
    cursor.close()
    connect.close()
    print(code)
    return code


def publish_collect_coupons_activity(activity_id):
    # 中台数据库地址
    connect = pymssql.connect('10.171.109.9', 'kd_bme', 'CapitaBME@123', 'KD_Bme_Activity')
    cursor = connect.cursor()
    sql = 'update t_Sale_RewardCoupon set auditStatus=2,publishStatus=1 where id=' + str(activity_id)
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()

