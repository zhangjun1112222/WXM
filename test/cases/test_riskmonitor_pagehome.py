import pytest

from config.config import ServerInfo

import requests

class TestRiskMonitorPageHome:
    '''
    风险监测-主页
    '''

    def test_customer_risk(self,test_login):
        '''
        企业风险预警
        '''
        u = ServerInfo.get_url('/risk/monitor/customer/risk')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_industry_newrisk_loans(self,test_login):
        '''
        行业-新增风险贷款额
        '''
        u = ServerInfo.get_url('/risk/monitor/industry/new/risk/loans')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_industry_newrisk_loans(self,test_login):
        '''
        行业-新增风险贷款额-详情列表
        '''
        u = ServerInfo.get_url('/risk/monitor/industry/new/risk/loans/list?loan_periods_id=acf9e591704e4cdeae74e8df70be265f')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_industry_risk(self,test_login):
        '''
        行业风险预警
        '''
        u = ServerInfo.get_url('/risk/monitor/industry/risk')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert res.json()['data'][0]['risk_index']==3.1

    def test_risk_top20(self,test_login):
        '''
        省内风险贷款额增加前20
        '''
        u = ServerInfo.get_url('/risk/monitor/loans/risk/top/20?province_id=f156e8054f8911edaff60a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert len(res.json()['data'])==8

    def test_map_stat(self,test_login):
        '''
        地图展示
        '''
        u = ServerInfo.get_url('/risk/monitor/map/stat')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert len(res.json()['data']['data_list'])==31


    def test_new_riskloans(self,test_login):
        '''
        新增风险贷款额
        '''
        u = ServerInfo.get_url('/risk/monitor/new/risk/loans')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert res.json()['data'][-1]['risk_loans_growth']=='-3.72'

    def test_newriskloans_list(self,test_login):
        '''
        新增风险贷款额-详情列表
        '''
        u = ServerInfo.get_url('/risk/monitor/new/risk/loans/list?loan_periods_id=acf9e591704e4cdeae74e8df70be265f')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert res.json()['data'][0]['new_risk_loans']=='8.9'