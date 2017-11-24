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

import time, threading

import tushare as ts
import pymysql
import pandas as pd
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()


class DataLocalizer(object):
    """
    Localize data from tushare to MySQL
    """
    engine_str = 'mysql://root:08110010@localhost/gold_dig?charset=utf8'
    stock_list = None

    def localize_basic(self):
        """
        localize data from get_stock_basics
        """
        n_data = ts.get_stock_basics()
        n_data['created_at'] = time.strftime('%Y-%m-%d', time.localtime())
        engine = create_engine(self.engine_str)
        l_data = pd.read_sql_table('data_manage_getstockbasics', engine,
                                   index_col=('code'))
        if len(n_data) > len(l_data):
            d_data = n_data.drop(l_data.index)
            d_data.to_sql('data_manage_get_stock_basics', engine,
                          if_exists='append', index=True)
        self.stock_list = n_data

    def localize_k_data(self, code=None, ktype='D'):
        """
        localize data from get_k_data
        """
        n_data = ts.get_k_data()
        n_data['code'] = code
        n_data['ktype'] = ktype
        n_data['created_at'] = time.strftime('%Y-%m-%d %H:%M:%S',
                                             time.localtime())
        engine = create_engine(self.engine_str)
        # n_data.to_sql('get_k_data', engine, if_exists='append', index=True)
        l_data = pd.read_sql_table('get_k_data', engine,
                                   index_col=('code', 'date', 'ktype'))
        if len(n_data) > len(l_data):
            d_data = n_data.drop(l_data.index)
            d_data.to_sql('get_stock_basics', engine, if_exists='append',
                          index=True)
        else:
            print("no fetch")

if __name__ == '__main__':
    data_localizer = DataLocalizer()

    data_localizer.localize_basic()

    # Effective python P21
    # for i, code in enumerate(data_localizer.stock_list, 0):
    for code in data_localizer.stock_list:
        t = threading.Thread(target=data_localizer.localize_k_data,
                             args=(code,))
        t.start()
