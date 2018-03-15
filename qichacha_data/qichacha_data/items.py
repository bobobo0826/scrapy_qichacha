# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QichachaDataItem(scrapy.Item):
    registered_capital = scrapy.Field()#注册资本
    establishment_data = scrapy.Field()#成立时间
    operating_state = scrapy.Field()#经营状态
    credit_code = scrapy.Field()#统一社会信用代码
    taxpayer_id_number = scrapy.Field()#纳税人识别号
    registration_number = scrapy.Field()#注册号
    organization_code = scrapy.Field()#组织机构代码
    pass
class JSONMdataItem(scrapy.Item):
    jsondata = scrapy.Field()
    pass
