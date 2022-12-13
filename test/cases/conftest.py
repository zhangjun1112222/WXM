import pytest
import requests
from utils.exceltools import  ExcelTools
from config.config import ServerInfo
data=ExcelTools.read_excel(r'C:\Users\zj_001\Desktop\g-ruc脚本\g-ruc\data\g_ruc数据.xls', 'Sheet1',skip_first=True)
print(data)

@pytest.fixture(scope='function')
def test_login():
    u=ServerInfo.get_url('/tenant/user/login')
    d={'username':'admin','password':'123456'}
    h={'X-TenantID':'system'}
    res=requests.post(url=u,json=d,headers=h)
    assert  res.status_code==200


    return res.json()['data']['token']