import pytest

from config.config import ServerInfo

import requests

class TestIndustryRiskDetection:
    '''
    行业风险预警（风险检测进去）
    '''

    def test_commodity_price_trend(self, test_login):
        '''
        物价走势
        '''
        u = ServerInfo.get_url('/industry/risk/commodity-price-trend?industry_id=7e1840f174134fd288aba21b35e8efc0')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_finance_indicators(self, test_login):
        '''
        主要财务指标
        '''
        u = ServerInfo.get_url('/industry/risk/finance-indicators?industry_id=7e1840f174134fd288aba21b35e8efc0')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_loan_and_customer(self, test_login):
        '''
        行业贷款与客户数
        '''
        u = ServerInfo.get_url('/industry/risk/loans-and-customer?industry_id=e1f7961324954696bfd4dd49bc2c0147')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200


    def test_location(self, test_login):
        '''
        客户位置(地图数据)
        '''
        u = ServerInfo.get_url('/industry/risk/location?industry_id=e1f7961324954696bfd4dd49bc2c0147&risk_level=1,2,3')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200


    def test_macro_industry_data(self, test_login):
        '''
        行业宏观数据
        '''
        u = ServerInfo.get_url('/industry/risk/macro-industry-data?industry_id=e1f7961324954696bfd4dd49bc2c0147&one_year=1')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200


    def test_real_estate_indicator(self, test_login):
        '''
        房地产行业指标(输入如何行业id参数，返回的都一样)
        '''
        u = ServerInfo.get_url('/industry/risk/real-estate-indicator?industry_id=16272de764a047aa9e8c401e4dd5295d')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200


    def test_risk_loan_balance_grow(self, test_login):
        '''
        风险贷款余额增长
        '''
        u = ServerInfo.get_url('/industry/risk/risk-loan-balance-grow?industry_id=d0ab4b3b73e744d0b3fbda58b3b4ef69')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_risk_struct(self, test_login):
        '''
        风险结构
        '''
        u = ServerInfo.get_url('/industry/risk/risk-struct?industry_id=d0ab4b3b73e744d0b3fbda58b3b4ef69')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200







