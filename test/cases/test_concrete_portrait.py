from config.config import ServerInfo

import requests

class TestPortrait:
    '''
    客户具体画像
    '''


    def test_basic_info(self,test_login):
        u=ServerInfo.get_url('/customer/profile/basic-info?customer_id=a3f5e8034f5b11edaded0a1f715d4995')
        h={"X-TenantID":'system',"x-token":test_login}
        res=requests.get(url=u,headers=h)
        print(res.text)
        assert res.json()['code']==200
        assert res.status_code==200

    def test_external_data(self,test_login):
        '''
        外部其他数据
        '''
        u=ServerInfo.get_url('/customer/profile/external-data?customer_id=a3f5e8034f5b11edaded0a1f715d4995')
        h = {'X-TenantID': 'system', 'x-token': test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_finance_data(self,test_login):
        '''
        财务数据
        '''
        u=ServerInfo.get_url('/customer/profile/finance-data?customer_id=a3f5e8034f5b11edaded0a1f715d4995&all_data=true')
        h = {'X-TenantID': 'system', 'x-token': test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_industry_risk_analysis(self,test_login):
        '''
        行业风险分析
        '''
        u=ServerInfo.get_url('/customer/profile/industry-risk-analysis?customer_id=a3f5e8034f5b11edaded0a1f715d4995')
        h = {'X-TenantID': 'system', 'x-token': test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200



    def test_loan(self,test_login):
        '''
        贷款余额
        '''
        u=ServerInfo.get_url('/customer/profile/loans?customer_id=a3f5e8034f5b11edaded0a1f715d4995')
        h = {'X-TenantID': 'system', 'x-token': test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] ==200
        assert res.status_code == 200


    def test_monitor_indicators(self,test_login):
        '''
        检测指标
        '''
        u=ServerInfo.get_url('/customer/profile/monitor-indicators?customer_id=a3f5e8034f5b11edaded0a1f715d4995')
        h = {'X-TenantID': 'system', 'x-token': test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_public_opinion_data(self,test_login):
        '''
        舆论数据
        '''
        u=ServerInfo.get_url('/customer/profile/public-opinion-data?customer_id=a3f5e8034f5b11edaded0a1f715d4995')
        h = {'X-TenantID': 'system', 'x-token': test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_risk_trend(self,test_login):
        '''
        风险等级走势
        '''
        u=ServerInfo.get_url('/customer/profile/risk-trend?customer_id=a3f5e8034f5b11edaded0a1f715d4995')
        h = {'X-TenantID': 'system', 'x-token': test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200
