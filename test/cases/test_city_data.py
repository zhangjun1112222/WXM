from config.config import ServerInfo

import requests

class TestCityData:
    '''
    市级数据
    '''

    def test_loan_stat(self,test_login):
        '''
        贷款统计
        '''
        u = ServerInfo.get_url('/index/city/loan/stat?loan_periods_id=acf9e591704e4cdeae74e8df70be265f&city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_loan_top_20(self,test_login):
        '''
        前20大贷款客户及余额
        '''
        u = ServerInfo.get_url(
            '/index/city/loan/stat/top/20?loan_periods_id=acf9e591704e4cdeae74e8df70be265f&city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_new_risk_customer(self,test_login):
        '''
        新增风险客户及原因
        '''
        u = ServerInfo.get_url(
            '/index/city/new/risk/customer?loan_periods_id=b435b13adfde42f1a1b4062ec2f37842&city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_new_riskloan_customer(self,test_login):
        '''
        新增风险贷款客户
        '''
        u = ServerInfo.get_url(
            '/index/city/new/risk/loan/customer?loan_periods_id=b435b13adfde42f1a1b4062ec2f37842&city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_risk_customer_top10(self,test_login):
        '''
        前十大风险客户统计
        '''
        u = ServerInfo.get_url(
            '/index/city/risk/customer/top/10?loan_periods_id=b435b13adfde42f1a1b4062ec2f37842&city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_riskloan_stat(self,test_login):
        '''
        风险贷款统计
        '''
        u = ServerInfo.get_url(
            '/index/city/risk/loan/stat?loan_periods_id=b435b13adfde42f1a1b4062ec2f37842&city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_city_stat_map(self,test_login):
        '''
        数据统计-地图展示
        '''
        u = ServerInfo.get_url(
            '/index/city/stat/map?loan_periods_id=b435b13adfde42f1a1b4062ec2f37842&city_id=030e05384f8a11ed885d0a1f715d4995')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200