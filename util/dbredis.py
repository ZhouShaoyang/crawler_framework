# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

import json
import redis
import traceback
from random import sample

import config
from util import logger


class DBRedis():

    def __init__(self):
        self.host = config.REDIS_HOST
        self.port = config.REDIS_PORT
        self.redis = redis.StrictRedis(host=self.host, port=int(self.port), db=0, decode_responses=True)
        self.proxy_name = config.REDIS_PROXY_NAME
        self.start_name = config.REDIS_START_NAME
        self.index_name = config.REDIS_INDEX_NAME
        self.start_count = config.START_COUNT
        self.index_count = config.INDEX_COUNT
        self.logger = logger.Logger()

    def get_proxy(self, count=None):
        '''
        get proxy from redis
        '''
        try:
            proxys = []
            for item in list(self.redis.hgetall(name=self.proxy_name).items())[:count]:
                proxys.append(json.loads(item[0]))
            return proxys
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <get proxy> {error}')

    def clear_start(self):
        '''
        clear redis start hash
        '''
        try:
            self.redis.delete(self.start_name)
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <clear start> {error}')

    def set_start(self, key, value):
        '''
        set start url to start hash
        '''
        try:
            self.redis.hset(self.start_name, str(key), str(value))
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <set start> {error}')
    
    def len_start(self):
        '''
        get start hash length
        '''
        try:
            return self.redis.hlen(self.start_name)
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <len start> {error}')

    def get_start(self):
        '''
        get start url list from start hash
        '''
        try:
            indexes = []
            for item in list(self.redis.hgetall(name=self.start_name).items())[:self.start_count]:
                indexes.append(item[0])
                self.redis.hdel(self.start_name, item[0])
            return indexes
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <get start> {error}')

    def clear_index(self):
        '''
        clear redis index hash
        '''
        try:
            self.redis.delete(self.index_name)
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <clear index> {error}')

    def set_index(self, key, value):
        '''
        set index url to index hash
        '''
        try:
            self.redis.hset(self.index_name, str(key), str(value))
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <set index> {error}')
    
    def len_index(self):
        '''
        get index hash length
        '''
        try:
            return self.redis.hlen(self.index_name)
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <len index> {error}')

    def get_index(self):
        '''
        get index url list from index hash
        '''
        try:
            indexes = []
            for item in list(self.redis.hgetall(name=self.index_name).items())[:self.index_count]:
                indexes.append(item[0])
                self.redis.hdel(self.index_name, item[0])
            return indexes
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<redis> <get index> {error}')
