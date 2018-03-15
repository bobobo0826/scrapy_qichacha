# -*- coding: utf-8 -*-
import scrapy
import time
import re
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from qichacha_data.items import QichachaDataItem
from qichacha_data.items import JSONMdataItem
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class MoiveSpider(CrawlSpider):
    name = "qichacha_data"
    allowed_domains = ["qichacha.com"]
    # start_urls = ["https://www.qichacha.com/gongsi_area.shtml?prov=AH&p=1"]
    ID = ""

    def __init__(self):

        time.sleep(5)
        # 初始化时候，给爬虫新开一个浏览器
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        super(scrapy.Spider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def start_requests(self):
        for id in range(1, 500):
            url_gongsi = "https://www.qichacha.com/gongsi_area.shtml?prov=BJ&p=%d"%id
            yield Request(url=url_gongsi, callback=self.parse, dont_filter=False)



    def parse(self, response):
        selector = Selector(response)
        company_list = selector.xpath('//div[@class="col-md-12"]/section[@class="panel panel-default" and @id="searchlist"]/a/@href').extract()
        for info in company_list:
            url = "https://www.qichacha.com%s"%info
            yield Request(url=url, callback=self.parse1, dont_filter=False)


    def parse1(self, response):
        selector = Selector(response)

        #每个字段分别保存
        # item = QichachaDataItem()
        # item['registered_capital']=selector.xpath('//*[@id="Cominfo"]/table[2]/tr[1]/td[2]/text()').extract_first()
        # item['establishment_data'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[1]/td[4]/text()').extract_first()
        # item['operating_state'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[2]/td[2]/text()').extract_first()
        # item['credit_code'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[2]/td[4]/text()').extract_first()
        # item['taxpayer_id_number'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[3]/td[2]/text()').extract_first()
        # item['registration_number'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[3]/td[4]/text()').extract_first()
        # item['organization_code'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[4]/td[2]/text()').extract_first()


        #保存为json格式法一
        # dic=dict()
        # dic['registered_capital'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[1]/td[2]/text()').extract_first().replace("\n", "").strip()
        # dic['establishment_data'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[1]/td[4]/text()').extract_first().replace("\n", "").strip()
        # dic['operating_state'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[2]/td[2]/text()').extract_first().replace("\n", "").strip()
        # dic['credit_code'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[2]/td[4]/text()').extract_first().replace("\n", "").strip()
        # dic['taxpayer_id_number'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[3]/td[2]/text()').extract_first().replace("\n", "").strip()
        # dic['registration_number'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[3]/td[4]/text()').extract_first().replace("\n", "").strip()
        # dic['organization_code'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[4]/td[2]/text()').extract_first().replace("\n", "").strip()
        # # print("dic---------------------------------")
        # # print(dic)
        # jsoninfo = json.dumps(dic, sort_keys=True, indent=None, ensure_ascii=False)

        # 保存为json格式法二
        table = selector.xpath('//*[@id="Cominfo"]/table[2]').extract_first()
        soup = BeautifulSoup(table, "lxml")
        td_list = soup.find_all('td')
        odd_td_list = []
        even_td_list = []
        for i in range(0, len(td_list)):
            text = td_list[i].get_text().strip().strip('：').strip(':')
            if i % 2 == 0:
                odd_td_list.append(text)
            else:
                even_td_list.append(text)
        dic = dict(zip(odd_td_list, even_td_list))
        jsoninfo = json.dumps(dic, ensure_ascii=False)
        # print ("JSON输出：")
        # print (jsoninfo)
        item=JSONMdataItem()
        item['jsondata']=jsoninfo
        yield item

    def spider_closed(self, spider):
        # 当爬虫退出的时候关闭chrome
        print("spider closed")
        time.sleep(60)
        self.browser.quit()



