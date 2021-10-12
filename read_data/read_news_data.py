# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 下午4:34
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : read_news_data.py

from DAO.mongo_db import MongoDB
import os
import time


class NewsData(object):
    def __init__(self):
        self.mongo = MongoDB(db='recommendation')
        self.db_client = self.mongo.db_client
        self.read_collection = self.db_client['read']
        self.like_collection = self.db_client['likes']
        self.collection = self.db_client['collection']
        self.content = self.db_client['content_labels']

    def cal_score(self):
        result = list()
