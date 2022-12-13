from config.config import ServerInfo

from utils.exceltools import    ExcelTools
data=ExcelTools.read_excel(r'C:\Users\zj_001\Desktop\g-ruc脚本\g-ruc\data\g_ruc数据.xls','Sheet2',skip_first=True)

import requests

class TestCustomerPortrait:
    '''
    客户画像
    '''

    def test_industry(self,test_login):
        '''
        行业分布
        '''
        u=ServerInfo.get_url(data[0][1])
        h=eval(data[0][3])
        res=requests.get(url=u,headers=h)
        # print(res.text)
        assert res.json()['code']==200
        assert res.status_code==data[0][4]
        assert res.json()['data'][0]['value']==data[0][5]

    def test_province(self,test_login):
        '''
        省市分布
        '''
        u = ServerInfo.get_url(data[1][1])
        h = eval(data[1][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[1][4]
        assert res.json()['data'][27]['value']==data[1][5]

    def test_risk_loans(self,test_login):
        '''
        风险贷款额（亿元）
        '''
        u = ServerInfo.get_url(data[2][1])
        h = eval(data[2][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[2][4]
        assert res.json()['data'][0]['value']==str(data[2][5])


    def test_risk_loans_change(self,test_login):
        '''
        风险贷款变动额
        '''
        u = ServerInfo.get_url(data[3][1])
        h = eval(data[3][3])
        res = requests.get(url=u, headers=h)
        # print(res.json())
        assert res.json()['code'] == 200
        assert res.status_code == data[3][4]
        assert res.json()['data'][0]['value']==str(data[3][5])

    def test_scale(self,test_login):
        '''
        客户体量分布
        '''
        u = ServerInfo.get_url(data[4][1])
        h = eval(data[4][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[4][4]
        assert res.json()['data'][2]['value'] == data[4][5]

    def test_scale_base_industry(self,test_login):
        '''
        客户体量行业分布
        '''
        u = ServerInfo.get_url(data[5][1])
        h = eval(data[5][3])
        res = requests.get(url=u, headers=h)
        # print(res.json()['data']['data']['体量分布']['房地产'][0]['value'])
        assert res.json()['code'] == 200
        assert res.status_code == data[5][4]
        assert res.json()['data']['data']['体量分布']['房地产'][0]['value']==data[5][5]

    def test_scale_base_province(self,test_login):
        '''
        客户体量省市分布
        '''
        u = ServerInfo.get_url(data[6][1])
        h = eval(data[6][3])
        res = requests.get(url=u, headers=h)
        # print(res.json()['data']['data']['体量分布']['重庆市'][0]['value'])
        assert res.json()['code'] == 200
        assert res.status_code == data[6][4]
        assert res.json()['data']['data']['体量分布']['重庆市'][0]['value'] ==data[6][5]

    def test_scale_base_risk_level(self,test_login):
        '''
        客户体量风险等级分类
        '''
        u = ServerInfo.get_url(data[7][1])
        h = eval(data[7][3])
        res = requests.get(url=u, headers=h)
        # print(res.json()['data']['data']['体量分布']['一般'][3]['value'])
        assert res.json()['code'] == 200
        assert res.status_code == data[7][4]
        assert res.json()['data']['data']['体量分布']['一般'][3]['value'] == data[7][5]

    def test_top_new_loan_industry(self,test_login):
        '''
        行业新增贷款前五
        '''
        u = ServerInfo.get_url(data[8][1])
        h = eval(data[8][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[8][4]
        assert res.json()['data'][0]['name'] == data[8][5]

    def test_top_new_loan_province(self,test_login):
        '''
        省市新增贷款额前五
        '''
        u = ServerInfo.get_url(data[9][1])
        h = eval(data[9][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[9][4]
        assert res.json()['data'][0]['name'] == data[9][5]

    def test_top_new_riskloan_industry(self,test_login):
        '''
        行业新增风险贷款额前五
        '''
        u = ServerInfo.get_url(data[10][1])
        h = eval(data[10][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[10][4]
        assert res.json()['data'][0]['name']==data[10][5]

    def test_top_new_riskloan_province(self,test_login):
        '''
        省市新增风险贷款前五
        '''
        u = ServerInfo.get_url(data[11][1])
        h = eval(data[11][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[11][4]
        assert res.json()['data'][0]['name'] == data[11][5]

    def test_total_loans(self,test_login):
        '''
        贷款总额（亿元）
        '''
        u = ServerInfo.get_url(data[12][1])
        h = eval(data[12][3])
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == data[12][4]
        assert res.json()['data'][0]['value'] == str(data[12][5])

     