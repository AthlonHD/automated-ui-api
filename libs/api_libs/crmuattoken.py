# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import json
import requests
import urllib3
import time

import libs.env_conf


class CrmuatToken:

    def __init__(self):

        with open(libs.env_conf.mall_path + r'logs/config.json', 'r') as f_t:
            self.config = json.loads(f_t.read())

        self.token = self.config['token']['token']
        self.expire_time = self.config.get('token').get('expire_time')

    def get_token(self):
        """
        请求新的token
        :return:
        """
        urllib3.disable_warnings()

        header = {'Content-Type': 'application/json'}

        # 区域账号
        # body = json.dumps({'loginName': 'dc\\vr_dingmeng', 'loginPwd': 'dm@61252031'})
        # response = requests.request('POST', 'https://crmmpapiuat.dc.capitaland.com/api/UserCurr/Login',
        #                             headers=header, data=body, verify=False)

        # ADFS账号
        body = json.dumps({'loginName': '5D0D61EE04BE2E97'})
        response = requests.request('POST', 'https://kamall30apiuat.capitaland.com.cn/api/UserCurr/AdfsLogin',
                                    headers=header, data=body, verify=False)

        # print(response.text)
        new_token = response.json()['body']['token']
        self.config['token']['token'] = new_token
        current_time = time.time()
        expire_time = current_time + 600
        self.config['token']['expire_time'] = expire_time

        with open(libs.env_conf.mall_path + 'logs/config.json', 'w') as f_t:
            json.dump(self.config, f_t)

        return new_token

    def check_token(self):
        """
        获取token
        :return:
        """

        # 参数内的token为空或已过期
        if self.token == '' or self.expire_time <= time.time():
            new_token = self.get_token()
            return new_token
        else:
            return self.token


if __name__ == '__main__':
    token = CrmuatToken().check_token()
    print(CrmuatToken().__init__())
    print(token)

    with open(libs.env_conf.logs_exact_path, 'r') as f:
        print(f.read())
