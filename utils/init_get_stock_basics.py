#!/usr/bin/env python
# -*-coding=utf-8-*-
#
# File Name: ".expand("%"))
# Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
# Author LiuBin on: Thu Nov  2 19:51:05 CST 2017
#
# @desc:
#
# @history
#

import tushare as ts
import pymysql
import time
import pandas as pd
from datetime import datetime
from sqlalchemy import ( create_engine, MetaData, Table, Column, DateTime,
    Boolean, Date, Integer, Numeric, String, Text, Index)


pymysql.install_as_MySQLdb()
class DataAccessLayer(object):
    """ 缠中学缠数据库结构层 """
    connection = None
    engine = None
    conn_string = 'mysql+pymysql://root:08110010@localhost/gold_dig?charset=utf8'
    metadata = MetaData()

    # 股票列表
    get_stock_basics = Table('get_stock_basics', metadata,
                             Column('id', Integer(), primary_key=True),
                             Column('code', String(6)),
                             Column('name', String(50), index=True),
                             Column('industry', String(30)),  # 所属行业
                             Column('area', String(30)),  # 地区
                             Column('pe', Numeric(12, 4)),  # 市盈率
                             Column('outstanding', Numeric(12, 4)),  # 流通股本(亿)
                             Column('totals', Numeric(12, 4)),  # 总股本(亿)
                             Column('totalAssets', Numeric(20, 4)),  # 总资产(万)
                             Column('liquidAssets', Numeric(20, 4)),  # 流动资产
                             Column('fixedAssets', Numeric(20, 4)),  # 固定资产
                             Column('reserved', Numeric(20, 4)),  # 公积金
                             Column(
                                 'reservedPerShare', Numeric(
                                     12, 4)),  # 每股公积金
                             Column('esp', Numeric(12, 4)),  # 每股收益
                             Column('bvps', Numeric(12, 4)),  # 每股净资
                             Column('pb', Numeric(12, 4)),  # 市净率
                             Column('timeToMarket', Numeric(12, 4)),  # 上市日期
                             Column('undp', Numeric(12, 4)),  # 未分利润
                             Column('perundp', Numeric(12, 4)),  # 每股未分配
                             Column('rev', Numeric(12, 4)),  # 收入同比(%)
                             Column('profit', Numeric(12, 4)),  # 利润同比(%)
                             Column('gpr', Numeric(12, 4)),  # 毛利率(%)
                             Column('npr', Numeric(12, 4)),  # 净利润率(%)
                             Column('holders', Integer()),  # 股东人数
                             Column(
                                 'date', DateTime(), default=datetime.now),  # 获取时间
                             Index(
                                 'ix_get_stock_basics', 'code', 'date', unique=True),
                             )

    def db_init(self, conn_string=None):
        self.engine = create_engine(conn_string or self.conn_string)
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()

dal = DataAccessLayer()




if __name__ == '__main__':
    n_data = ts.get_stock_basics()
    n_data['created_at'] = time.strftime('%Y-%m-%d', time.localtime())
    engine = create_engine('mysql://root:08110010@localhost/gold_dig?charset=utf8')
    # n_data.to_sql('get_stock_basics', engine, if_exists='append', index=True)
    l_data = pd.read_sql_table('get_stock_basics', engine, index_col=('code'))
    if len(n_data) > len(l_data):
        print("fetch again")
        print(n_data.index)
        print(l_data.index)
        d_data = n_data.drop(l_data.index)
        print(len(d_data))
        print(d_data)
        d_data.to_sql('get_stock_basics', engine, if_exists='append', index=True)
    else:
        print("no fetch")
