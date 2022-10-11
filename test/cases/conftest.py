import pytest
import requests



@pytest.fixture(scope='function')
def test_login():
    u='http://cq.zkxqgroup.com:10060/api/v1/tenant/user/login'
    d={'username':'admin','password':'123456'}
    h={'X-TenantID':'system'}
    res=requests.post(url=u,json=d,headers=h)
    assert  res.status_code==200


    return res.json()['data']['token']