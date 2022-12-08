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
        u = ServerInfo.get_url('/loan/stat/1/list/20?risk_level=-1&green_loan=-1&period_id=b435b13adfde42f1a1b4062ec2f37842&page=1&size=20')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200