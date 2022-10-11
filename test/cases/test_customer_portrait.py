from config.config import ServerInfo

import requests

class TestCustomerPortrait:
    '''
    客户画像
    '''

    def test_industry(self,test_login):
        '''
        行业分布
        '''
        u=ServerInfo.get_url('/customer/statistics/industry')
        h={"X-TenantID":'system',"x-token":test_login}
        res=requests.get(url=u,headers=h)
        print(res.text)
        assert res.json()['code']==200
        assert res.status_code==200

    def test_province(self,test_login):
        '''
        省市分布
        '''
        u = ServerInfo.get_url('/customer/statistics/province')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_risk_loans(self,test_login):
        '''
        风险贷款额（亿元）
        '''
        u = ServerInfo.get_url('/customer/statistics/risk-loans')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_risk_loans_change(self,test_login):
        '''
        风险贷款变动额
        '''
        u = ServerInfo.get_url('/customer/statistics/risk-loans-change')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_scale(self,test_login):
        '''
        客户体量分布
        '''
        u = ServerInfo.get_url('/customer/statistics/scale')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_scale_base_industry(self,test_login):
        '''
        客户体量行业分布
        '''
        u = ServerInfo.get_url('/customer/statistics/scale-base-industry')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_scale_base_province(self,test_login):
        '''
        客户体量省市分布
        '''
        u = ServerInfo.get_url('/customer/statistics/scale-base-province')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_scale_base_risk_level(self,test_login):
        '''
        客户体量风险等级分类
        '''
        u = ServerInfo.get_url('/customer/statistics/scale-base-risk-level')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_top_new_loan_industry(self,test_login):
        '''
        行业新增贷款前五
        '''
        u = ServerInfo.get_url('/customer/statistics/top-new-loan-industry')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_top_new_loan_province(self,test_login):
        '''
        省市新增贷款额前五
        '''
        u = ServerInfo.get_url('/customer/statistics/top-new-loan-province')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_top_new_riskloan_industry(self,test_login):
        '''
        行业新增风险贷款额前五
        '''
        u = ServerInfo.get_url('/customer/statistics/top-new-risk-loan-industry')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_top_new_riskloan_province(self,test_login):
        '''
        省市新增风险贷款前五
        '''
        u = ServerInfo.get_url('/customer/statistics/top-new-risk-loan-province')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_total_loans(self,test_login):
        '''
        贷款总额（亿元）
        '''
        u = ServerInfo.get_url('/customer/statistics/total-loans')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200
     