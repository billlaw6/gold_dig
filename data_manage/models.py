# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or
# field names.
from __future__ import unicode_literals

from django.db import models


class ForecastData(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=6, blank=True, null=True)
    report_date = models.DateField(blank=True, null=True)
    pre_eps = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
     null=True)
    range = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
     null=True)
    created_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'forecast_data'
        unique_together = (('code', 'report_date'),)


class FundHoldings(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    nums = models.IntegerField(blank=True, null=True)
    nlast = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    clast = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    ratio = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    created_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fund_holdings'
        unique_together = (('code', 'date'),)


class GetHData(models.Model):
    date = models.DateTimeField()
    open = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    high = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    close = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    low = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    price_change = models.DecimalField(
        max_digits=12, decimal_places=6, blank=True, null=True)
    p_change = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        blank=True,
        null=True)
    ma5 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    ma10 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    ma20 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    v_ma5 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    v_ma10 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    v_ma20 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    diff = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    dea = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    macd = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    code = models.CharField(max_length=6, blank=True, null=True)
    ktype = models.CharField(max_length=6, blank=True, null=True)
    type = models.CharField(max_length=6, blank=True, null=True)
    delete = models.IntegerField(blank=True, null=True)
    fenxing = models.CharField(max_length=6, blank=True, null=True)
    fx_weight = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    bi_to_be = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    bi_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    duan_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    operate = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'get_h_data'
        unique_together = (('code', 'date', 'ktype'),)


class GetHistData(models.Model):
    date = models.DateTimeField()
    open = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    high = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    close = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    low = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    price_change = models.DecimalField(
        max_digits=12, decimal_places=6, blank=True, null=True)
    p_change = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        blank=True,
        null=True)
    ma5 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    ma10 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    ma20 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    v_ma5 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    v_ma10 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    v_ma20 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    turnover = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    diff = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    dea = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    macd = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    code = models.CharField(max_length=6, blank=True, null=True)
    ktype = models.CharField(max_length=6, blank=True, null=True)
    type = models.CharField(max_length=6, blank=True, null=True)
    delete = models.IntegerField(blank=True, null=True)
    fenxing = models.CharField(max_length=6, blank=True, null=True)
    fx_weight = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    bi_to_be = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    bi_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    duan_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    operate = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'get_hist_data'
        unique_together = (('code', 'date', 'ktype'),)


class GetIndex(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    change = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    open = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    preclose = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    close = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    high = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    low = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    amount = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'get_index'
        unique_together = (('code', 'date'),)


class GetReportData(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    esp = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    esp_yoy = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    bvps = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    roe = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    epcf = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    net_profits = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    profits_yoy = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    distrib = models.CharField(blank=True, null=True)
    report_date = models.DateField(blank=True, null=True)
    year = models.IntegerField()
    quarter = models.IntegerField()
    created_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'get_report_data'
        unique_together = (('code', 'year', 'quarter'), ('year', 'quarter'),)


class GetStockBasics(models.Model):
    code = models.CharField(max_length=6, null=True)
    name = models.CharField(blank=True, null=True)
    industry = models.CharField(blank=True, null=True)
    area = models.CharField(blank=True, null=True)
    pe = models.FloatField(blank=True, null=True)
    outstanding = models.FloatField(blank=True, null=True)
    totals = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    totalassets = models.FloatField(
        db_column='totalAssets', blank=True, null=True)
    # Field name made lowercase.
    liquidassets = models.FloatField(
        db_column='liquidAssets', blank=True, null=True)
    # Field name made lowercase.
    fixedassets = models.FloatField(
        db_column='fixedAssets', blank=True, null=True)
    reserved = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    reservedpershare = models.FloatField(
        db_column='reservedPerShare', blank=True, null=True)
    esp = models.FloatField(blank=True, null=True)
    bvps = models.FloatField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    timetomarket = models.BigIntegerField(
        db_column='timeToMarket', blank=True, null=True)
    undp = models.FloatField(blank=True, null=True)
    perundp = models.FloatField(blank=True, null=True)
    rev = models.FloatField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    gpr = models.FloatField(blank=True, null=True)
    npr = models.FloatField(blank=True, null=True)
    holders = models.FloatField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'get_stock_basics'


class GetTodayAll(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    changepercent = models.DecimalField(
        max_digits=12, decimal_places=4, blank=True, null=True)
    trade = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    open = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    high = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    low = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    settlement = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    turnoverratio = models.DecimalField(
        max_digits=20, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=True,
        null=True)
    per = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    pb = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    mktcap = models.DecimalField(
        max_digits=20,
        decimal_places=6,
        blank=True,
        null=True)
    nmc = models.DecimalField(
        max_digits=20,
        decimal_places=6,
        blank=True,
        null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'get_today_all'
        unique_together = (('code', 'date'),)


class NewStocks(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    ipo_date = models.DateField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    pe = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    limit = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    funds = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    ballot = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    created_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'new_stocks'
        unique_together = (('code', 'issue_date'),)


class ProfitData(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    report_date = models.DateField(blank=True, null=True)
    divi = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    shares = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    created_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profit_data'
        unique_together = (('code', 'report_date'),)


class XsgData(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    ratio = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=True,
        null=True)
    created_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'xsg_data'
        unique_together = (('code', 'date', 'count'),)
