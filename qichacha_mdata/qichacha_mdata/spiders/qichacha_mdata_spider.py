# -*- coding: utf-8 -*-
import scrapy
import time
import urllib.request
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request
from bs4 import BeautifulSoup
import json
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from qichacha_mdata.items import QichachaMdataItem
from qichacha_mdata.items import DengjiMdataItem
from qichacha_mdata.items import JSONMdataItem

class MoiveSpider(CrawlSpider):
    name = "qichacha_mdata"
    allowed_domains = ["qichacha.com"]
    # start_urls = ["https://www.qichacha.com/gongsi_area.shtml?prov=AH&p=1"]
    ID = ""

    def start_requests(self):
        for id in range(1, 3):
            url_gongsi = "https://www.qichacha.com/gongsi_area.shtml?prov=AH&p=%d"%id
            yield Request(url=url_gongsi,  callback=self.parse)

    def parse(self, response):
        selector = Selector(response)
        company_list = selector.xpath('//div[@class="col-md-12"]/section[@class="panel panel-default" and @id="searchlist"]/a/@href').extract()
        name = selector.xpath('//*[@id="searchlist"]/a/span[2]/span[1]/text()').extract()
        i = 0
        for info in company_list:
            ID = info.replace("/firm_", "").replace(".html", "")
            word = urllib.parse.quote(name[i])
            url = "https://www.qichacha.com/company_getinfos?unique="+ID+"&companyname="+word+"&tab=base"
            i = i+1
            yield Request(url=url, meta={"ID": ID}, callback=self.parse1)



    def parse1(self, response):
        selector = Selector(response)

        #分别按字段保存
        # if "工商信息" in selector.xpath('//*[@id="Cominfo"]/div[1]/span[1]/text()').extract_first():
        #     print("工商信息================================")
        #     item = QichachaMdataItem()
        #     item['registered_capital'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[1]/td[2]/text()').extract_first()
        #     item['establishment_data'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[1]/td[4]/text()').extract_first()
        #     item['operating_state'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[2]/td[2]/text()').extract_first()
        #     item['credit_code'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[2]/td[4]/text()').extract_first()
        #     item['taxpayer_id_number'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[3]/td[2]/text()').extract_first()
        #     item['registration_number'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[3]/td[4]/text()').extract_first()
        #     item['organization_code'] = selector.xpath('//*[@id="Cominfo"]/table[2]/tr[4]/td[2]/text()').extract_first()
        # if "登记信息" in selector.xpath('//*[@id="Cominfo"]/div/span[1]/text()').extract_first():
        #     print("登记信息================================")
        #     item=DengjiMdataItem()
        #     item['legal_person'] = selector.xpath('//*[@id="Cominfo"]/table/tr[2]/td[2]/text()').extract_first()
        #     item['registered_capital'] = selector.xpath('//*[@id="Cominfo"]/table/tr[2]/td[4]/text()').extract_first()
        #     item['establishment_data'] = selector.xpath('//*[@id="Cominfo"]/table/tr[3]/td[2]/text()').extract_first()
        #     item['register_state'] = selector.xpath('//*[@id="Cominfo"]/table/tr[3]/td[4]/text()').extract_first()
        #     item['social_type'] = selector.xpath('//*[@id="Cominfo"]/table/tr[4]/td[2]/text()').extract_first()
        #     item['registration_authority'] = selector.xpath('//*[@id="Cominfo"]/table/tr[4]/td[4]/text()').extract_first()

        #保存为json
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
        item = JSONMdataItem()
        item['jsondata'] = jsoninfo
        yield item


