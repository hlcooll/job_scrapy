# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
# 分发器
from scrapy.xlib.pydispatch import dispatcher
#信号量
from scrapy import signals
import logging
import time
from scrapy.http import Request
#域名拼接
from urllib import parse
from scrapy import log
from job.items import JobItem

from scrapy.http import HtmlResponse

logging.basicConfig(level=logging.DEBUG)
class A51jobSpider(scrapy.Spider):
    name = 'a51job'
    allowed_domains = ['www.51job.com']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="D:/PycharmProjects/geckodriver.exe")
        super(A51jobSpider, self).__init__()
        # dispatcher.connect(self.parse,signals.engine_started)
        dispatcher.connect(self.spider_closed,signals.spider_closed)

    #python整体页面所有公司URL
    def parse(self, response):
        py_list = response.css(".el p>span>a::attr(href)").extract()
        # print(py_list+'传递的这个')
        for list in py_list:
            yield Request(url=list,callback=self.python_job,dont_filter=True)
        #dont_filter = True
        # , dont_filter = True

        # logging.info("zheli",response.url)

    def python_job(self,response):
        items=JobItem()
        print(11)
        if response.url!='http://51rz.51job.com/sc/show_job_detail.php?jobid=86521374':
            url=response.url
            position=response.css(".cn > h1:nth-child(1)::attr(title)").extract()#职位
            salary=response.css(".cn > strong:nth-child(3)::text").extract()#薪水
            t_company=response.css(".cname > a:nth-child(1)::attr(title)").extract()#公司
            address=response.css(".lname::text").extract()#'地址
            touch = response.css("div.tBorderTop_box:nth-child(3) > div:nth-child(2) > p:nth-child(1)::text").extract()[1].spid()#联系方式
            items['position']=position
            items['salary']=salary
            items['t_company']=t_company
            items['address']=address
            items['touch']=touch
            items['url'] =url
            yield items

    def spider_closed(self,spider):
        #当爬虫退出的时候quit掉
        print("close")
        self.driver.quit()
