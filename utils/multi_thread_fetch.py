#!/usr/bin/env python
# -*-coding=utf-8-*-
#
# File Name: ".expand("%"))
# Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
# Author LiuBin on: Thu Nov 16 08:58:43 CST 2017
#
# @desc:
#
# @history
#
import threading

import tushare as ts
import pymysql
pymysql.install_as_MySQLdb()

from db_engine import DBEngine
engine = DBEngine.get_engine()


def localize_k_data(code, ktype='D'):
    print('fetching data of %s' % code)
    d = ts.get_k_data(code, '2017-10-01', '2017-11-01')
    d['code'] = code
    d['ktype'] = ktype
    d1 = d.reset_index(drop=True)
    d2 = d1.set_index(['code', 'date', 'ktype'])
    d2.to_sql('get_k_data', engine, if_exists='append', index=True)


def main():
    total = ts.get_stock_basics()
    list = total[0:10]
    threads = []

    for code in list.index:
        # print('code: %s' % code)
        t = threading.Thread(target=localize_k_data, args=(code,))
        threads.append(t)

    for t in threads:
        t.start()

if __name__ == '__main__':
    main()
