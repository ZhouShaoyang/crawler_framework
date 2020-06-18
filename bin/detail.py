# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

import time

import config
from util import downloader
from util import dbredis
from util import dbpostgresql
from util import logger


class CrawlDetail():

    def __init__(self):
        self.timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
        self.dbredis = dbredis.DBRedis()
        self.dbpostgresql = dbpostgresql.DBPostgresql(timestamp=self.timestamp)
        self.logger = logger.Logger()

    def crawl(self):
        '''
        main crawler function
        '''
        self.__create_table()
        while self.dbredis.len_index() > 0:
            urls = self.dbredis.get_index()
            download = downloader.Downloader(urls=urls, headers=self.__headers())
            responses = download.downloader()
            for response in responses:
                download.parser(parser_response=response, parser_function=self.__parser_function, error_function=self.__error_function)

    def __create_table(self):
        '''
        create storage table
        '''
        pass

    def __headers(self):
        '''
        construct request header
        '''
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
        return headers

    def __parser_function(self, response):
        '''
        parse response and store result to postgresql
        '''
        pass

    def __error_function(self, response):
        '''
        get response url and restore url to redis index
        '''
        self.dbredis.set_index(response, 'retry')


if __name__ == "__main__":
    crawldetail = CrawlDetail()
    crawldetail.crawl()
