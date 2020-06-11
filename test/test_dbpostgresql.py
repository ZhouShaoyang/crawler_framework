# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

from util import dbpostgresql


if __name__ == "__main__":
    timestamp = 'timestamp'
    dbpostgresql = dbpostgresql.DBPostgresql(timestamp=timestamp)
    dbpostgresql.create('crawler_framework_test', test1='text', test2='int8', test3='float8')
    dbpostgresql.insert('crawler_framework_test', test1='测试数据', test2='8', test3='8.8')
