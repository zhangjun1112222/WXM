import pytest

from config.config import ServerInfo

import requests
class TestUpdate:
    '''
    数据更新
    '''

    def test_update_city_list(self,test_login):
        '''
        获取用户所在省的市列表
        '''
        u = ServerInfo.get_url('/data/update/city/list')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    @pytest.mark.skip(reason='未知接口')
    def test_update_customer(self,test_login):
        '''
        客户更新
        '''
        u = ServerInfo.get_url('/data/update/customer')
        h = {"X-TenantID": 'system', "x-token": test_login}
        d={
              "city_id": "string",
              "customer_name": "string",
              "industry_id": "string",
              "lat": 0,
              "lng": 0,
              "loans": 0,
              "periods_id": "string",
              "repayment_plans": [
                {
                  "remaining_loans": 0,
                  "repayment_money": 0,
                  "repayment_time": "string"
                }
              ]}
        res = requests.post(url=u, headers=h,json=d)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200