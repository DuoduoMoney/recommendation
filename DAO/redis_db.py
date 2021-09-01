# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 下午2:40
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : redis_db.py

import redis


class Redis(object):
    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost',
                                       port=6379,
                                       db=0,
                                       password='',
                                       decode_responses=True)
