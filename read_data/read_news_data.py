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
        score_dict = dict()
        data = self.read_collection.find()
        for info in data:
            # 做分数计算
            score_dict.setdefault(info['user_id'], {})
            score_dict[info['user_id']].setdefault(info['content_id'], 0)

            query = {'user_id': info['user_id'], "content_id": info['content_id']}

            exist_count = 0
            # 去每一个表里面进行查询，如果存在数据，就加上相应的得分

            # ["str(1),str(8),str(6145ec828451a2b8577df7b3)"]
            # result.append()
            pass
        pass

        def to_csv(self, user_score_content, res_file):
            if not os.path.exists('../data/news_score'):
                os.mkdir('../data/news_score')
            with open(res_file, mode='w', encoding='utf-8') as wf:
                # info = "1,8,6145ec828451a2b8577df7b3"
                for info in user_score_content:
                    wf.write(info + '\n')

            print(len(user_score_content))


if __name__ == '__main__':
    news_data = NewsData()
    news_data.cal_score()
