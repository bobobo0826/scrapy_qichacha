# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from qichacha_mdata.items import QichachaMdataItem
from qichacha_mdata.items import DengjiMdataItem
from qichacha_mdata.items import JSONMdataItem
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log


class QichachaMdataPipeline(object):
    #Connect to the MongoDB database
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["qichachamdata"]
        self.Register = db["Register"]
        self.Bussiness = db["Bussiness"]
        self.JSONbase = db["JSONbase"]


    def process_item(self, item, spider):
        if isinstance(item, QichachaMdataItem):
            try:
                self.Bussiness.insert(dict(item))
            except Exception:
                pass
        if isinstance(item, DengjiMdataItem):
            try:
                self.Register.insert(dict(item))
            except Exception:
                pass
        if isinstance(item, JSONMdataItem):
            try:
                self.JSONbase.insert(dict(item))
            except Exception:
                pass
        return item