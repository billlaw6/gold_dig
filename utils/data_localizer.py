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
class DataLocalizer(object):
    """
    Localize data from tushare to MySQL
    """
    engine_str = 'mysql://root:08110010@localhost/gold_dig?charset=utf8'
    def localize_basic(self):
        """
        localize data from get_stock_basics
        """
        n_data = ts.get_stock_basics()
        n_data['created_at'] = time.strftime('%Y-%m-%d', time.localtime())
        engine = create_engine(self.engine_str)
        # n_data.to_sql('get_stock_basics', engine, if_exists='append', index=True)
        l_data = pd.read_sql_table('get_stock_basics', engine, index_col=('code'))
        if len(n_data) > len(l_data):
            d_data = n_data.drop(l_data.index)
            d_data.to_sql('get_stock_basics', engine, if_exists='append', index=True)
        else:
            print("no fetch")

    def localize_k_data(self, code=None, ktype='D'):
        """
        localize data from get_k_data
        """
        n_data = ts.get_k_data()
        n_data['created_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        engine = create_engine(self.engine_str)
        # n_data.to_sql('get_k_data', engine, if_exists='append', index=True)
        l_data = pd.read_sql_table('get_k_data', engine, index_col=('code'))
        if len(n_data) > len(l_data):
            d_data = n_data.drop(l_data.index)
            d_data.to_sql('get_stock_basics', engine, if_exists='append', index=True)
        else:
            print("no fetch")

if __name__ == '__main__':
    data_localizer = DataLocalizer()

    data_localizer.localize_basic()
    data_localizer.localize_k_data()
