# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

import config
from util import downloader
from util import dbredis
from util import logger


class CrawlIndex():

    def __init__(self):
        self.dbredis = dbredis.DBRedis()
        self.logger = logger.Logger()
        self.url = config.URL
        with open(config.DATA_FILE, 'r') as datafile:
            self.datas = [data.replace('\n', '') for data in datafile.readlines()]

    def crawl(self):
        '''
        main crawler function
        '''
        self.__start_url()
        while self.dbredis.len_start() > 0:
            urls = self.dbredis.get_start()
            download = downloader.Downloader(urls=urls, headers=self.__headers())
            responses = download.downloader()
            for response in responses:
                download.parser(parser_response=response, parser_function=self.__parser_function, error_function=self.__error_function)

    def __start_url(self):
        '''
        construct initial url
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
        parse response and store result to redis index
        '''
        pass

    def __error_function(self, response):
        '''
        get response url and restore url to redis start
        '''
        self.dbredis.set_start(response, 'retry')

    def __fixurl(self, url, params):
        '''
        fix url parameters
        '''
        fix = ''
        for key, value in params.items():
            fix += f'&{key}={value}'
            fix = fix.lstrip('&')
        return f'{url}?{fix}'


if __name__ == "__main__":
    crawlindex = CrawlIndex()
    crawlindex.crawl()
