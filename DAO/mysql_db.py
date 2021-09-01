# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 下午3:08
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : mysql_db.py
import sys

sys.path.append('..')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  # 定义一个实例，所有表必须继承该实例


class Mysql(object):
    def __init__(self):
        Base = declarative_base()
        self.engine = create_engine("mysql+pymysql://root:qian1234@127.0.0.1:3306/sina", encoding='utf-8')
        self._DBSession = sessionmaker(bind=self.engine)


'''
if __name__ == "__main__":
    mysql = Mysql()
    session = mysql.engine._DBSession()
    session.query
'''
