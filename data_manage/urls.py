#!/usr/bin/env python
# -*-coding=utf-8-*-
#
# File Name: ".expand("%"))
# Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
# Author LiuBin on: Mon Nov 13 22:29:08 CST 2017
#
# @desc:
#
# @history
#
from django.conf.urls import url
from data_manage import views


urlpatterns = [
    url(r'^$', views.get_stock_basics, name='basics'),
]
