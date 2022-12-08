import pytest

from config.config import ServerInfo

import requests

class TestPageHomeData:
    '''
    首页数据
    '''

    def test_feedback_list(self,test_login):
        '''
        风险关注列表
        '''
        u = ServerInfo.get_url('/index/feedback/list')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_industry_loan_stat(self,test_login):
        '''
        行业贷款统计占比
        '''
        u = ServerInfo.get_url('/index/industry/loan/stat?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_industry_loanstat_list(self,test_login):
        '''
        行业贷款统计占比-详情列表
        '''
        u = ServerInfo.get_url('/index/industry/loan/stat/list?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json()['data'][-1])
        assert res.json()['code'] == 200
        assert res.status_code == 200

    @pytest.mark.skip(reason='前端没用到')
    def test_industry_risk_diff(self,test_login):
        '''
        行业风险及客户变动
        '''
        u = ServerInfo.get_url('/index/industry/risk/diff?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    @pytest.mark.skip(reason='前端没用到')
    def test_industry_risk_diff_list(self, test_login):
        '''
        行业风险及客户变动-详情列表
        '''
        u = ServerInfo.get_url('/index/industry/risk/diff/list?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_loan_stat(self, test_login):
        '''
        省市贷款统计占比
        '''
        u = ServerInfo.get_url('/index/loan/stat?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_loan_stat_list(self, test_login):
        '''
        省市贷款统计占比-详情列表
        '''
        u = ServerInfo.get_url('/index/loan/stat/list?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.json()['data'][0])
        assert res.json()['code'] == 200
        assert res.status_code == 200

    @pytest.mark.skip(reason='前端未用到')
    def test_risk_diff(self, test_login):
        '''
        风险及客户变动
        '''
        u = ServerInfo.get_url('/index/risk/diff?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200

    @pytest.mark.skip(reason='前端未用到')
    def test_risk_diff_list(self, test_login):
        '''
        风险及客户变动-列表详情
        '''
        u = ServerInfo.get_url('/index/risk/diff/list?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_risk_new(self,test_login):
        '''
        本期新增风险
        '''
        u = ServerInfo.get_url('/index/risk/new?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    @pytest.mark.skip(reason='后端没数据且前端为用到')
    def test_risk_new_read(self,test_login):
        '''
        本期新增风险-已读
        '''
        u = ServerInfo.get_url('/index/risk/new/read')
        h = {"X-TenantID": 'system', "x-token": test_login}
        d={"customer_id": "66840ab1505e11edbc770a1f715d4995","loan_periods_id": "b0f565f1e42440e89439e5a534521cc7"}
        res = requests.put(url=u, headers=h,json=d)
        print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == 200


    def test_stat(self,test_login):
        '''
        首页数据统计(贷款规模和客户规模)
        '''
        u = ServerInfo.get_url('/index/stat?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_stat_map(self,test_login):
        '''
        首页省市数据统计-地图展示
        '''
        u = ServerInfo.get_url('/index/stat/map?loan_periods_id=b0f565f1e42440e89439e5a534521cc7')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.json()['data']['data_list'][0])
        assert res.json()['code'] == 200
        assert res.status_code == 200

