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


class GetForecastData(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    type = models.CharField(max_length=6, blank=False, null=False)
    report_date = models.DateField(blank=False, null=False)
    pre_eps = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
     null=False)
    range = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
     null=False)
    created_on = models.DateField(blank=False, null=False)

    class Meta:
        managed = True
        unique_together = (('code', 'report_date'),)


class GetFundHoldings(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    nums = models.IntegerField(blank=False, null=False)
    nlast = models.IntegerField(blank=False, null=False)
    count = models.IntegerField(blank=False, null=False)
    clast = models.IntegerField(blank=False, null=False)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    ratio = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    created_on = models.DateField(blank=False, null=False)

    class Meta:
        managed = True
        unique_together = (('code', 'date'),)


class GetHData(models.Model):
    date = models.DateTimeField()
    open = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    high = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    close = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    low = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    price_change = models.DecimalField(
        max_digits=12, decimal_places=6, blank=False, null=False)
    p_change = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        blank=False,
        null=False)
    ma5 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    ma10 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    ma20 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    v_ma5 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    v_ma10 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    v_ma20 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    diff = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    dea = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    macd = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    code = models.CharField(max_length=6, blank=False, null=False)
    ktype = models.CharField(max_length=6, blank=False, null=False)
    type = models.CharField(max_length=6, blank=False, null=False)
    delete = models.IntegerField(blank=False, null=False)
    fenxing = models.CharField(max_length=6, blank=False, null=False)
    fx_weight = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    bi_to_be = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    bi_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    duan_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    operate = models.CharField(max_length=6, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'get_h_data'
        unique_together = (('code', 'date', 'ktype'),)


class GetHistData(models.Model):
    date = models.DateTimeField()
    open = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    high = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    close = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    low = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    price_change = models.DecimalField(
        max_digits=12, decimal_places=6, blank=False, null=False)
    p_change = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        blank=False,
        null=False)
    ma5 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    ma10 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    ma20 = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    v_ma5 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    v_ma10 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    v_ma20 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    turnover = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    diff = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    dea = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    macd = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    code = models.CharField(max_length=6, blank=False, null=False)
    ktype = models.CharField(max_length=6, blank=False, null=False)
    type = models.CharField(max_length=6, blank=False, null=False)
    delete = models.IntegerField(blank=False, null=False)
    fenxing = models.CharField(max_length=6, blank=False, null=False)
    fx_weight = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    bi_to_be = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    bi_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    duan_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    operate = models.CharField(max_length=6, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'get_hist_data'
        unique_together = (('code', 'date', 'ktype'),)


class GetIndex(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    change = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    open = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    preclose = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    close = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    high = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    low = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    amount = models.IntegerField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'get_index'
        unique_together = (('code', 'date'),)


class GetReportData(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    esp = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    esp_yoy = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    bvps = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    roe = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    epcf = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    net_profits = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    profits_yoy = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    distrib = models.CharField(max_length=6, blank=False, null=False)
    report_date = models.DateField(blank=False, null=False)
    year = models.IntegerField()
    quarter = models.IntegerField()
    created_on = models.DateField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'get_report_data'
        unique_together = (('code', 'year', 'quarter'), ('year', 'quarter'),)


class GetStockBasics(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=60, blank=False, null=False)
    industry = models.CharField(max_length=60, blank=False, null=False)
    area = models.CharField(max_length=60, blank=False, null=False)
    pe = models.FloatField(blank=False, null=False)
    outstanding = models.FloatField(blank=False, null=False)
    totals = models.FloatField(blank=False, null=False)
    # Field name made lowercase.
    totalassets = models.FloatField(
        db_column='totalAssets', blank=False, null=False)
    # Field name made lowercase.
    liquidassets = models.FloatField(
        db_column='liquidAssets', blank=False, null=False)
    # Field name made lowercase.
    fixedassets = models.FloatField(
        db_column='fixedAssets', blank=False, null=False)
    reserved = models.FloatField(blank=False, null=False)
    # Field name made lowercase.
    reservedpershare = models.FloatField(
        db_column='reservedPerShare', blank=False, null=False)
    esp = models.FloatField(blank=False, null=False)
    bvps = models.FloatField(blank=False, null=False)
    pb = models.FloatField(blank=False, null=False)
    # Field name made lowercase.
    timetomarket = models.BigIntegerField(
        db_column='timeToMarket', blank=False, null=False)
    undp = models.FloatField(blank=False, null=False)
    perundp = models.FloatField(blank=False, null=False)
    rev = models.FloatField(blank=False, null=False)
    profit = models.FloatField(blank=False, null=False)
    gpr = models.FloatField(blank=False, null=False)
    npr = models.FloatField(blank=False, null=False)
    holders = models.FloatField(blank=False, null=False)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'get_stock_basics'


class GetTodayAll(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    changepercent = models.DecimalField(
        max_digits=12, decimal_places=4, blank=False, null=False)
    trade = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    open = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    high = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    low = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    settlement = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    turnoverratio = models.DecimalField(
        max_digits=20, decimal_places=6, blank=False, null=False)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        blank=False,
        null=False)
    per = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    pb = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    mktcap = models.DecimalField(
        max_digits=20,
        decimal_places=6,
        blank=False,
        null=False)
    nmc = models.DecimalField(
        max_digits=20,
        decimal_places=6,
        blank=False,
        null=False)
    date = models.DateField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'get_today_all'
        unique_together = (('code', 'date'),)


class GetNewStocks(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    ipo_date = models.DateField(blank=False, null=False)
    issue_date = models.DateField(blank=False, null=False)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    pe = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    limit = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    funds = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    ballot = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    created_on = models.DateField(blank=False, null=False)

    class Meta:
        managed = True
        unique_together = (('code', 'issue_date'),)


class GetProfitData(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    report_date = models.DateField(blank=False, null=False)
    divi = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    shares = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    created_on = models.DateField(blank=False, null=False)

    class Meta:
        managed = True
        unique_together = (('code', 'report_date'),)


class GetXsgData(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=6, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    count = models.IntegerField(blank=False, null=False)
    ratio = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        blank=False,
        null=False)
    created_on = models.DateField(blank=False, null=False)

    class Meta:
        managed = True
        unique_together = (('code', 'date', 'count'),)
