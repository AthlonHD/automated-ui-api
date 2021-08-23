# -*- coding=utf-8 -*-


import requests


url = 'https://bmecouponuat.capitaland.com.cn/api/coupon/DownFile?fileName=CouponDetail_2021_06_18_469770684127878.xls'

result = requests.get(url)

with open('table.xls', 'wb') as f:
    f.write(result.content)
