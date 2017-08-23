#! usr/bin/env python3
# -*- coding:utf-8 -*-

import pymongo
from 抓取招聘信息.craw_jobs.setting import *
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_to_mongo(result):
    if db['zhilianzhaopin'].insert(result):
        print('插入数据库成功', result)
    return None