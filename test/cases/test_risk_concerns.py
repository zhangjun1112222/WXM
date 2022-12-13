import pytest

from config.config import ServerInfo

import requests

class TestRiskConcerns:
    '''
    风险关注
    '''

    def test_risk_attention(self, test_login):
        '''
        新增风险关注
        '''
        u = ServerInfo.get_url('/risk/attention')
        h = {"X-TenantID": 'system', "x-token": test_login}
        d={
            "content": "358692",
            "customer_ids": [
            "686ef2a4505e11eda08a0a1f715d4995"],
            "province_id": "007037074f8a11eda3840a1f715d4995",
            "risk_level": 1
            }
        res = requests.post(url=u, headers=h,json=d)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_riskattention_list(self,test_login):
        '''
        风险关注列表(状态为开启的)
        '''
        u = ServerInfo.get_url('/risk/attention/1/list/20?state=0')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200
        print(res.json()['data']['list'][0]['id'])
        return res.json()['data']['list'][0]['id']

    def test_riskattention_list1(self,test_login):
        '''
        风险关注列表(全部数据)
        '''
        u = ServerInfo.get_url('/risk/attention/1/list/20')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200
        print(res.json()['data']['list'][0]['id'])
        return res.json()['data']['list'][0]['id']

    def test_riskattention_close(self, test_login):
        '''
        关闭风险关注
        '''
        q = self.test_riskattention_list(test_login)
        u = ServerInfo.get_url('/risk/attention/close?id='+q)
        h = {"X-TenantID": 'system', "x-token": test_login}
        print(u)
        res = requests.put(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_riskattention_customer(self, test_login):
        '''
        获取客户列表(新增时用到接口)
        '''
        u = ServerInfo.get_url('/risk/attention/customer?province_id=8be4aed34f8911ed87670a1f715d4995&risk_level=2')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_riskattention_customer(self, test_login):
        '''
        风险关注详情
        '''
        p = self.test_riskattention_list1(test_login)
        u = ServerInfo.get_url('/risk/attention/detail?id='+p)
        h = {"X-TenantID": 'system', "x-token": test_login}
        # print(u)
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200