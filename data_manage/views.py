#!/usr/bin/env python
# -*-coding=utf-8-*-
#
# File Name: ".expand("%"))
# Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
# Author LiuBin on: Thu Nov  9 11:32:05 CST 2017
#
# @desc:
#
# @history
#

from django.shortcuts import render
from django.http import HttpResponse
import tushare as ts
from data_manage.models import GetStockBasics
from utils.db_engine import DBEngine
import pandas as pd
engine = DBEngine.get_engine()


# Create your views here.
def get_stock_basics(request):
    """
    比较本地股票数量和tushare获取的股票数量，若本地有缺失，补全到与tushare获取
    的一致。
    """
    n_data = ts.get_stock_basics()
    m_data = GetStockBasics.object.all()
    if len(m_data) < len(n_data):
        l_data = pd.read_sql_table('get_stock_basics', engine, index_col='code')
        d_data = n_data.drop(l_data.index)
        d_data.to_sql('get_stock_basics', engine, if_exists='append', index=True)
        return HttpResponse('%d item inserted' % len(d_data))
    else:
        return HttpResponse('No data to be insert')


