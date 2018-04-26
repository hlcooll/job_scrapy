# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position=scrapy.Field()#职位
    salary=scrapy.Field()#薪水
    t_company=scrapy.Field()#公司
    address=scrapy.Field()#地址
    p_claim=scrapy.Field()# 职位要求
    touch=scrapy.Field()#联系方式
    rests=scrapy.Field()#其他
    t_message=scrapy.Field()#公司信息
    url=scrapy.Field()#网页路径