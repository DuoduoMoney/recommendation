# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 下午6:38
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : SimpleRecList.py
from DAO import redis_db
from DAO.mongo_db import MongoDB


class SimpleRecList(object):
    def __init__(self):
        self._redis = redis_db.Redis()
        self._mongo = MongoDB(db='recommendation')
        self._collection = self._mongo.db_client['content_labels']

    def get_news_order_by_time(self):
        count = 10000
        data = self._collection.find().sort([{"news_date", -1}])
        for news in data:
            #print(str(news['_id']), str(news['news_date']))
            self._redis.redis.zadd('rec_list_by_time', {str(news['_id']): count})
            count -= 1


if __name__ == '__main__':
    simple = SimpleRecList()
    simple.get_news_order_by_time()
