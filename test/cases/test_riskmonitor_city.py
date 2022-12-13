import pytest

from config.config import ServerInfo

import requests

class TestRiskMonitorCity:
    '''
    风险监测-市级
    '''

    def test_city_loan(self,test_login):
        '''
        贷款余额
        '''
        u = ServerInfo.get_url('/risk/monitor/city/loans?city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_map_stat(self,test_login):
        '''
        客户信息-地图展示
        '''
        u = ServerInfo.get_url('/risk/monitor/city/map/stat?city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert len(res.json()['data']['data_list'])==10

    def test_risk_growth(self,test_login):
        '''
        风险贷款增加额
        '''
        u = ServerInfo.get_url('/risk/monitor/city/risk/growth?city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert len(res.json()['data'])==10

    def test_risk_loans(self,test_login):
        '''
        风险贷款余额
        '''
        u = ServerInfo.get_url('/risk/monitor/city/risk/loans?city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert len(res.json()['data'])==2

    def test_risk_type(self,test_login):
        '''
        风险类别占比
        '''
        u = ServerInfo.get_url('/risk/monitor/city/risk/type?city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200
        assert res.json()['data'][0]['value']==8
