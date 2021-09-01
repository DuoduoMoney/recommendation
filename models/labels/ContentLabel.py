# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 下午4:40
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : ContentLabel.py

from DAO.mysql_db import Mysql
from DAO.mongo_db import MongoDB
from sqlalchemy import distinct
from models.labels.entity.content import Content
from datetime import datetime
import re
from models.keywords.tfidf import Segment


class ContentLabel(object):
    def __init__(self):
        self.seg = Segment(
            stopword_files=['/Users/qianzhen/Desktop/workspace_pycharm/recommendation/data/stopwords/1.txt',
                            '/Users/qianzhen/Desktop/workspace_pycharm/recommendation/data/stopwords/2.txt',
                            '/Users/qianzhen/Desktop/workspace_pycharm/recommendation/data/stopwords/3.txt',
                            '/Users/qianzhen/Desktop/workspace_pycharm/recommendation/data/stopwords/4.txt'],
            userdict_files=[])
        self.engine = Mysql()
        self.session = self.engine._DBSession()
        self.mongo = MongoDB(db='recommendation')
        self.collection = self.mongo.db_client['content_labels']

    def get_data_from_mysql(self):
        types = self.session.query(distinct(Content.type))
        for i in types:
            res = self.session.query(Content).filter(Content.type == i[0])
            # print(res.count())  # 每种类别有多少条数据
            if res.count() > 0:
                for x in res.all():
                    keywords = self.get_keywords(x.content, 10)
                    word_nums = self.get_words_nums(x.content)
                    create_time = datetime.utcnow()
                    content_collection = dict()
                    content_collection['word_num'] = word_nums
                    content_collection['keywords'] = keywords
                    content_collection['describe'] = x.content
                    content_collection['news_date'] = x.times
                    content_collection['hot_heat'] = 10000
                    content_collection['type'] = x.type
                    content_collection['title'] = x.title
                    content_collection['likes'] = 0
                    content_collection['read'] = 0
                    content_collection['collections'] = 0
                    content_collection['create_time'] = create_time
                    self.collection.insert(content_collection)

    def get_words_nums(self, contents):
        ch = re.findall('([\u4e00-\u9fa5])', contents)
        num = len(ch)
        return num

    def get_keywords(self, contents, num=10):
        keywords = self.seg.extract_keyword(contents)[:num]
        return keywords


if __name__ == '__main__':
    content_labels = ContentLabel()
    content_labels.get_data_from_mysql()
