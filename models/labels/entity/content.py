# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 下午4:46
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : content.py
from sqlalchemy import Column, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from DAO.mysql_db import Mysql


class Content(Base):
    __tablename__ = 'data'
    id = Column(Integer(), primary_key=True)
    times = Column(DateTime)
    title = Column(Text())
    content = Column(Text())
    type = Column(Text())

    def __init__(self):
        mysql = Mysql()
        engine = mysql.engines
        Base.metadata.create_all(engine)
