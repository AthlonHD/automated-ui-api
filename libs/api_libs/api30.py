# -*- coding=utf-8 -*-
# ! /usr/bin/env python3


import requests
import urllib3
from libs.api_libs.crmuattoken import CrmuatToken
from libs.env_conf import config as env_conf


class Api30:
    """
    封装请求方式
    """

    def __init__(self):

        self.bmeuat_url = env_conf.bmeuat_url
        self.bmeparkuat = env_conf.bmeparkuat_url
        self.kmalluat_url = env_conf.kmalluat_url
        self.bmecouponuat_url = env_conf.bmecouponuat_url

        # self.crmuat_url = 'https://bmeactuat.capitaland.com.cn/api'

        self.token = CrmuatToken().check_token()
        self.crmuat_header = {
            'Content-Type': 'application/json',
            'token': self.token
        }
        urllib3.disable_warnings()

    def get(self, api, linkget, header=None, body=None):

        if linkget == 'a':
            get_url = self.kmalluat_url + api
        elif linkget == 'b':
            get_url = self.bmeparkuat + api
        elif linkget == 'c':
            get_url = self.bmeuat_url + api
        elif linkget == 'd':
            get_url = self.bmecouponuat_url + api
        else:
            return None
        if header is not None:
            # 合并两个dict变量，**代表作为字典处理
            get_header = {**self.crmuat_header, **header}
            # print(post_header)
            result = requests.request('GET', get_url, headers=get_header, data=body, verify=False)
        else:
            result = requests.request('GET', get_url, headers=self.crmuat_header, data=body, verify=False)

        return result

    def post(self, api, linkpost, header=None, body=None):
        """
        :type header: object
        :param linkpost:
        :param body:
        :param api:
        :rtype: object
        """
        if linkpost == 'a':
            post_url = self.kmalluat_url + api
        elif linkpost == 'b':
            post_url = self.bmeparkuat + api
        elif linkpost == 'c':
            post_url = self.bmeuat_url + api
        elif linkpost == 'd':
            post_url = self.bmecouponuat_url + api
        else:
            return None

        if header is not None:
            # 合并两个dict变量，**代表作为字典处理
            get_header = {**self.crmuat_header, **header}
            # print(post_header)
            result = requests.request('POST', post_url, headers=get_header, data=body, verify=False)
        else:
            result = requests.request('POST', post_url, headers=self.crmuat_header, data=body, verify=False)

        return result


if __name__ == '__main__':
    r = Api30()
