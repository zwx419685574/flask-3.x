#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client.db_test  # 指定数据库名字

collection = db.students   # 表名
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
result = collection.insert(student)
print(result)

