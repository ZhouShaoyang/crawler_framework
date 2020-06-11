# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

import grequests
import requests
import traceback
from random import choice

import config
from util import dbredis
from util import logger


class Downloader():

    def __init__(self, urls):
        self.urls = urls
        self.headers = config.DOWNLOADER_HEADERS
        self.timeout = config.DOWNLOADER_TIMEOUT
        self.size = config.DOWNLOADER_SIZE
        self.proxy_count = config.DOWNLOADER_PROXY_COUNT
        self.dbredis = dbredis.DBRedis()
        self.logger = logger.Logger()
    
    def downloader(self):
        urls = self.urls
        headers = self.headers
        proxies = self.__proxies()
        timeout = self.timeout
        size = self.size
        mapping = [grequests.get(url=url, headers=headers, proxies=choice(proxies), timeout=timeout) for url in urls]
        responses = grequests.imap(mapping, size=size, exception_handler=self.__handler)
        return responses

    def parser(self, parser_response, parser_function, error_function):
        '''
        parser_response: requests.models.Response type object
        parser_function: need one requests.models.Response type object parameter called 'response'
        error_function: need one string type parameter called 'url'
        '''
        try:
            parser_function(response=parser_response)
        except Exception:
            if type(parser_response) == requests.models.Response:
                error = traceback.format_exc()
                self.logger.error(message=f'<downloader> <parser> {parser_response.url} {error}')
                error_function(response=parser_response.url)
            else:
                error = traceback.format_exc()
                self.logger.error(message=f'<downloader> <parser> {parser_response} {error}')
                error_function(response=parser_response)

    def __proxies(self):
        return self.dbredis.get_proxy(count=self.proxy_count)

    def __handler(self, request, exception):
        return request.url
