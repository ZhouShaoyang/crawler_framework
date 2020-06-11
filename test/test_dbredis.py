# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

from util import dbredis


if __name__ == "__main__":
    dbredis = dbredis.DBRedis()
    dbredis.clear_start()
    dbredis.set_start('start key', 'start value')
    print('start len: ', dbredis.len_start())
    print('start hash: ', dbredis.get_start())
    dbredis.clear_index()
    dbredis.set_index('index key', 'index value')
    print('index len: ', dbredis.len_index())
    print('index hash: ', dbredis.get_index())
    print('proxy hash: ', dbredis.get_proxy(count=10))
