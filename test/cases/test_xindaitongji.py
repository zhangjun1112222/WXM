import pytest

from config.config import ServerInfo

import requests

class TestIndustryRiskDetection:
    '''
    信贷统计
    '''

    def test_loan_list1(self, test_login):
        '''
        信贷统计（一期全部数据）
        '''
        u = ServerInfo.get_url('/loan/stat/1/list/20?risk_level=-1&green_loan=-1&period_id=b435b13adfde42f1a1b4062ec2f37842&page=1&size=20')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_loan_list2(self, test_login):
        '''
        信贷统计（查询）
        '''
        u = ServerInfo.get_url('/loan/stat/1/list/20?province_id=030070c84f8a11edb9310a1f715d4995&industry_id=e1f7961324954696bfd4dd49bc2c0147&risk_level=1&green_loan=1&period_id=b435b13adfde42f1a1b4062ec2f37842&page=1&size=20')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200