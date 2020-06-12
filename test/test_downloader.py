# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

import config
from util import downloader


def parser_func(response):
    print('parser_function:', response.text[0:31])


def error_func(response):
    print('error_function:', response)


if __name__ == "__main__":
    urls = [
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
    ]
    headers = config.DOWNLOADER_HEADERS
    downloader = downloader.Downloader(urls=urls, headers=headers)
    responses = downloader.downloader()
    for response in responses:
        print('downloader:', response)
        downloader.parser(parser_response=response, parser_function=parser_func, error_function=error_func)
