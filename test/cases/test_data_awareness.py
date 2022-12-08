import pytest

from config.config import ServerInfo

import requests


class TestDataAwareness:
    '''
    数据感知
    '''

    @pytest.mark.skip(reason='前端没用到')
    def test_cur_month_list(self,test_login):
        '''
        本月信息统计（前端没有做）
        '''
        u = ServerInfo.get_url('/data/aware/common/adds/cur-month/list')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_adds_stat(self,test_login):
        '''
        其他信息更新统计
        '''
        u = ServerInfo.get_url('/data/aware/common/adds/stat')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_source_stat(self,test_login):
        '''
        原始数据来源统计
        '''
        u = ServerInfo.get_url('/data/aware/common/source/stat')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    @pytest.mark.skip(reason='前端没用到')
    def test_all_list(self,test_login):
        '''
        数据信息统计-total
        '''
        u = ServerInfo.get_url('/data/aware/satellite/adds/all/list')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    @pytest.mark.skip(reason='前端没用到')
    def test_cur_month_list(self, test_login):
        '''
        卫星数据本月新增统计：卫星资源
        '''
        u = ServerInfo.get_url('/data/aware/satellite/adds/cur-month/list')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_stat_heat_map(self,test_login):
        '''
        卫星每日新增数据热力图
        '''
        u = ServerInfo.get_url('/data/aware/satellite/stat/heat-map')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200

    def test_stat_type_count(self,test_login):
        '''
        卫星分类统计
        '''
        u = ServerInfo.get_url('/data/aware/satellite/stat/type-count')
        h = {"X-TenantID": 'system', "x-token": test_login}
        res = requests.get(url=u, headers=h)
        # print(res.text)
        assert res.json()['code'] == 200
        assert res.status_code == 200


