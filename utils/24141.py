import pymysql
import time

import datetime


conn = pymysql.connect(host='cq.zkxqgroup.com', port=3306, user='zhzl', password='Zhzl_2022', database='zhzl_equipment', charset='utf8')
cur = conn.cursor()
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
