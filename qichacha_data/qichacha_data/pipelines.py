# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# -*- coding: utf-8 -*-
import pymongo
from qichacha_data.items import QichachaDataItem
from qichacha_data.items import JSONMdataItem
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class QichachaDataPipeline(object):
    #Connect to the MongoDB database
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["qichacha"]
        self.Movie = db["Industry"]

    def process_item(self, item, spider):
        if isinstance(item, QichachaDataItem):
            try:
                self.Movie.insert(dict(item))
            except Exception:
                pass
        if isinstance(item, JSONMdataItem):
            try:
                self.Movie.insert(dict(item))
            except Exception:
                pass
        return item