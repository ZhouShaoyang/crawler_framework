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

def headers_func():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
    return headers


if __name__ == "__main__":
    urls = [
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
    ]
    downloader = downloader.Downloader(urls=urls, headers=headers_func())
    responses = downloader.downloader()
    for response in responses:
        print('downloader:', response)
        downloader.parser(parser_response=response, parser_function=parser_func, error_function=error_func)
