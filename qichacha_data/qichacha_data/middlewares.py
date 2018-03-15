# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from qichacha_data.ipList import getProxy
import random
import base64
import time
from selenium import webdriver
from scrapy.http import HtmlResponse



class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = getProxy()
        request.meta['proxy'] = "http://%s" % proxy


class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        spider.browser.get(request.url)
        time.sleep(10)  # 等待JS执行
        content = spider.browser.page_source
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)







