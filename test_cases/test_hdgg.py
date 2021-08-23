# -*- coding=utf-8 -*-
# ! /usr/bin/env python3

import json

import allure
import pytest

from apis.uat30 import Uat30
from libs.selenium_libs.case.activity_notice import ActivityNotice
from libs.api_libs.case.ggcx import Hdgg
from libs.selenium_libs.common.activity_audit import ActivityAudit


@allure.feature('活动公告')
class TestHdgg:

    # 活动-活动公告验证前台3.0活动公告显示正常
    @allure.title('12560-活动公告3.0')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/12560/')
    def test_hdgg_01(self, driver):
        """
        活动-活动公告3.0
        """
        # 接口创建活动公告活动
        r = Hdgg().add_hdgonggao()
        response = json.loads(r[0])  # 接口响应值
        activity_name = r[1]  # 活动名称
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('活动公告', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '11')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'
        # H5页面获取活动名称
        name = ActivityNotice(driver).join_activity_notice(activity_name)
        assert name == activity_name
        # 撤回活动
        r = json.loads(Uat30().withdraw(activity_id, '11').text)
        assert r['message'] == "操作成功"

    # 活动-活动公告验证:前台为明天项目活动公告在3.0不显示
    @allure.title('12560-活动公告为明天-公告')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/12560/')
    def test_hdgg_02(self, driver):
        """
        活动公告为明天-公告
        """
        # 接口创建活动公告活动
        r = Hdgg().add_weiming()
        response = json.loads(r[0])  # 接口响应值
        activity_name = r[1]  # 活动名称
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('活动公告', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '11')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'
        # H5页面获取活动名称
        name = ActivityNotice(driver).join_activity_notice(activity_name)
        assert name is None
        # 撤回活动
        r = json.loads(Uat30().withdraw(activity_id, '11').text)
        assert r['message'] == "操作成功"

    # 活动-活动公告验证:前台为明天项目微刊在3.0不显示
    @allure.title('12560-活动公告为明天-微刊')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/12560/')
    def test_hdgg_03(self, driver):
        """
        活动公告为明天-微刊
        """
        # 接口创建活动公告活动
        r = Hdgg().add_weikan()
        response = json.loads(r[0])  # 接口响应值
        activity_name = r[1]  # 活动名称
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('活动公告', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '11')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'
        # H5页面获取活动名称
        name = ActivityNotice(driver).join_activity_notice(activity_name)
        assert name is None
        # 撤回活动
        r = json.loads(Uat30().withdraw(activity_id, '11').text)
        assert r['message'] == "操作成功"

    # 活动-活动公告验证:前台为明天项目新闻在3.0不显示
    @allure.title('12560-活动公告为为明天-新闻')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/12560/')
    def test_hdgg_04(self, driver):
        """
        活动公告为为明天-新闻
        """
        # 接口创建活动公告活动
        r = Hdgg().add_weimingnews()
        response = json.loads(r[0])  # 接口响应值
        activity_name = r[1]  # 活动名称
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('活动公告', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '11')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'
        # H5页面获取活动名称
        name = ActivityNotice(driver).join_activity_notice(activity_name)
        assert name is None
        # 撤回活动
        r = json.loads(Uat30().withdraw(activity_id, '11').text)
        assert r['message'] == "操作成功"

    # 活动-活动公告验证:3.0活动公告不在前台显示
    @allure.title('12560-活动公告-不在前台显示')
    @allure.severity('critical')
    @allure.link('https://dev.azure.com/CLNexTen/%E5%87%AF%E5%BE%B7%E6%98%9F3.0/_workitems/edit/12560/')
    def test_hdgg_05(self, driver):
        """
        活动公告-不在前台显示
        """
        # 接口创建活动公告活动
        r = Hdgg().add_nodisplay()
        response = json.loads(r[0])  # 接口响应值
        activity_name = r[1]  # 活动名称
        assert response['message'] == '操作成功'
        # iwf审核
        ActivityAudit(driver).activity_notice_uat('活动公告', activity_name)
        # 获取活动详情
        activity_details = Uat30().activity_details(activity_name).json()
        # 获取活动对应id
        activity_id = activity_details['body']['list'][0]['id']
        # 发布活动
        response_fabu = Uat30().fabu(activity_id, '11')
        test_json = json.loads(response_fabu.text)
        assert test_json['message'] == '操作成功'
        # H5页面获取活动名称
        name = ActivityNotice(driver).join_activity_notice(activity_name)
        assert name is None
        # 撤回活动
        r = json.loads(Uat30().withdraw(activity_id, '11').text)
        assert r['message'] == "操作成功"


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_hdgg.py::TestHdgg::test_hdgg_04', '--alluredir=C:\\Project\\mall30\\report'])
