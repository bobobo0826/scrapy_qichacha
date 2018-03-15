# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from qichacha_mdata.cookies import cookies
from qichacha_mdata.user_agents import agents


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        cookie = random.choice(cookies)
        cookie = dict(elem.split('=') for elem in cookie.split(';'))
        # cookie = eval(cookie)  # 将str类型的cookie转换成dict
        request.cookies = cookie
