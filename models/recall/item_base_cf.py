# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 下午5:09
# @Author  : Rocket,Money
# @Project : recommendation
# @File    : item_base_cf.py
from tqdm import tqdm
import numpy as np


class ItemBaseCf(object):
    def __init__(self, train_file):
        """
        读取文件
        用户和item历史 item相似度计算
        训练
        """
        self.train = dict()
        self.user_item_history = dict()
        self.item_to_item = dict()
        self.read_data(train_file)

    def read_data(self, train_file):
        """
        读文件，并生成数据集（用户、分数、新闻，user,score,item）
        :param train_file: 训练文件
        :return: {"user_id":{"content_id":predict_score}}
        """
        with open(train_file, mode='r', encoding='utf-8') as rf:
            for line in tqdm(rf.readlines()):
                user, score, item = line.strip().split(",")
                self.train.setdefault(user, {})
                self.user_item_history.setdefault(user, {})
                self.train[user][item] = int(score)
                self.user_item_history[user].append(item)

    def cf_item_train(self):
        """
        基于item的协同过滤，计算相似度
        :return: 相似度矩阵{content_id?:{content_id:score}}
        """
        self.item_to_item, self.item_count = dict(), dict()

        for user, items in self.items():
            for i in items.keys():
                self.item_count.setdefault(i, 0)
                self.item_count[i] += 1

        for user, items in self.train.items():
            for i in items.keys():
                self.item_to_item.setdefault(i, {})
                for j in items.keys():
                    if i == j:
                        continue
                    self.item_to_item[i].setdefault(j, 0)
                    self.item_to_item[i][j] += 1 / (
                        np.math.sqrt(self.item_count[i] + self.item_count[j]))  # item i  j 共现一次就加1

        for _item in self.item_to_item:
            self.item_to_item[_item] = dict(sorted(self.item_to_item[_item].items(),
                                                   key=lambda x: x[1], reverse=True)[0:30])

    def cal_rec_item(self, user, N=50):
        """
        给用户user推荐前N个感兴趣的文章
        :param user:
        :param N:
        :return:  推荐的文章列表
        """
        rank = dict()
        try:
            action_item = self.train[user]
            for item, score in action_item.items():
                for j, wj in self.item_to_item[item].items():
                    if j in action_item.keys():  # 如果j被阅读过了，那么就不会推荐了
                        continue
                    rank.setdefault(j, 0)
                    rank[j] += score * wj / 10000 + 4  # 推过4次以后就不推了

            res = dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])
            return list(res)

        except:
            return {}
