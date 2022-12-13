from config.config import ServerInfo
from utils.exceltools import    ExcelTools
data=ExcelTools.read_excel(r'C:\Users\zj_001\Desktop\g-ruc脚本\g-ruc\data\g_ruc数据.xls','Sheet1',skip_first=True)
import requests

class TestPortrait:
    '''
    客户具体画像
    '''


    def test_basic_info(self,test_login):
        '''
        基础信息
        '''
        u=ServerInfo.get_url(data[0][1])
        d=eval(data[0][2])
        h=eval(data[0][3])
        res=requests.get(url=u,headers=h,params=d)
        assert res.json()['code']==200
        assert res.status_code==data[0][4]
        assert res.json()['data']['loan_balance']==str(data[0][5])

    def test_external_data(self,test_login):
        '''
        外部其他数据
        '''
        u=ServerInfo.get_url(data[1][1])
        d=eval(data[1][2])
        h =eval(data[1][3])
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == data[1][5]
        assert res.status_code == data[1][4]

    def test_finance_data(self,test_login):
        '''
        财务数据
        '''
        u=ServerInfo.get_url(data[2][1])
        d=eval(data[2][2])
        h = eval(data[2][3])
        res = requests.get(url=u, headers=h,params=d)
        # print(res.json()['data'][0]['data']['利润总额'][0]['value'])
        assert res.json()['code'] == 200
        assert res.status_code == data[2][4]
        assert res.json()['data'][0]['data']['利润总额'][0]['value'] ==str(data[2][5])

    def test_industry_risk_analysis(self,test_login):
        '''
        行业风险分析
        '''
        u=ServerInfo.get_url(data[3][1])
        d=eval(data[3][2])
        h = eval(data[3][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[3][4]
        assert res.json()['data'][0]['value']==str(data[3][5])


    def test_loan(self,test_login):
        '''
        贷款余额
        '''
        u = ServerInfo.get_url(data[4][1])
        h = eval(data[4][3])
        d = eval(data[4][2])
        res = requests.get(url=u, headers=h,params=d)
        print(res.url)
        assert res.json()['code'] ==200
        assert res.status_code == 200


    def test_monitor_indicators(self,test_login):
        '''
        检测指标
        '''
        u=ServerInfo.get_url(data[5][1])
        d=eval(data[5][2])
        h = eval(data[5][3])
        res = requests.get(url=u, headers=h,params=d)
        assert res.json()['code'] == 200
        assert res.status_code == data[5][4]
        assert res.json()['data'][1]['value'] ==str(int(data[5][5]))

    def test_public_opinion_data(self,test_login):
        '''
        舆论数据
        '''
        u=ServerInfo.get_url(data[6][1])
        d=eval(data[6][2])
        h = eval(data[6][3])
        res = requests.get(url=u, headers=h,params=d)
        assert res.json()['code'] == 200
        assert res.status_code == data[6][4]
        assert res.json()['data'][0]['content']==data[6][5]

    def test_risk_trend(self,test_login):
        '''
        风险等级走势
        '''
        u=ServerInfo.get_url(data[7][1])
        d = eval(data[7][2])
        h= eval(data[7][3])
        res = requests.get(url=u, headers=h,params=d)
        assert res.json()['code'] == 200
        assert res.status_code == data[7][4]
        assert res.json()['data'][0]['value'] == data[7][5]