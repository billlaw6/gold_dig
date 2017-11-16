#!/usr/bin/env python
# -*-coding=utf-8-*-
#
# File Name: ".expand("%"))
# Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
# Author LiuBin on: Thu Nov  9 12:46:57 CST 2017
#
# @desc:
#
# @history
#
from sqlalchemy import create_engine


class DBEngine(object):
    """
    返回用于pandas.dataframe与数据库交互的引擎
    """
    engine = create_engine(
        'mysql://root:08110010@localhost/gold_dig?charset=utf8')

    # 也可以用get_engine = classmethod(get_engine)
    @classmethod
    def get_engine(self):
        return self.engine

    # 也可以用get_engine = staticmethod(get_engine_static)
    @staticmethod
    def get_engine_static():
        return create_engine(
            'mysql://root:08110010@localhost/gold_dig?charset=utf8')
