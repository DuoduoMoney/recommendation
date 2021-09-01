# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 下午3:05
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : mongo_to_redis.py

from DAO import redis_db
from DAO.mongo_db import MongoDB
import pymongo


class Write_to_redis(object):
    def __init__(self):
        self._redis = redis_db.Redis()
        self.mongo = MongoDB(db='recommendation')
        self.collection = self.mongo.db_client['content_labels']

    def get_from_mongo(self):
        pipelines = [{
            '$group': {
                '_id': "$type"
            }
        }]
        types = self.collection.aggregate(pipelines)
        count = 0
        for type in types:
            cx = {"type": type['_id']}
            data = self.collection.find(cx)
            for info in data:
                result = dict()
                result['content_id'] = str(info['_id'])
                result['describe'] = str(info['describe'])
                result['type'] = str(info['type'])
                result['title'] = str(info['title'])
                result['news_date'] = str(info['news_date'])
                result['likes'] = info['likes']
                result['read'] = info['read']
                result['hot_heat'] = info['hot_heat']
                result['collections'] = info['collections']
                self._redis.redis.set("news_detail:" + str(info['_id']), str(result))
                self._redis.redis.set("news_title:" + str(info['_id']), str(result['title']))
                self._redis.redis.set("news_date:" + str(info['_id']), str(result['news_date']))



                if count % 50 == 0:
                    print(count)
                count += 1


if __name__ == "__main__":
    write_to_redis = Write_to_redis()
    write_to_redis.get_from_mongo()
