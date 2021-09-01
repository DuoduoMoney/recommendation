# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 下午4:08
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : mongo_db.py
import pymongo


class MongoDB(object):
    def __init__(self, db):
        mongo_client = self._connect('127.0.0.1', '27017', '', '', db)
        self.db_client = mongo_client[db]
        self.collection_test = self.db_client['test_collections']

    def _connect(self, host, port, user, pwd, db):
        mongo_info = self._splicing(host, port, user, pwd, db)
        mongo_client = pymongo.MongoClient(mongo_info, connectTimeoutMS=1200, connect=False)
        return mongo_client

    @staticmethod
    def _splicing(host, port, user, pwd, db):
        client = "mongodb://" + host + ':' + str(port) + '/'
        if user != '':
            client = "mongodb://" + user + ':' + pwd + '@' + host + ':' + str(port) + '/'
            if db != '':
                client + db
        return client

    # 测试
    def test_insert(self):
        test = dict()
        test['name'] = 'Rocket'
        test['job'] = 'AI Algorithmer'
        test['time'] = '2021.08.26'
        self.collection_test.insert_one(test)

# 测试
if __name__ == "__main__":
    mongo = MongoDB(db="Rocket_test")
    mongo.test_insert()
