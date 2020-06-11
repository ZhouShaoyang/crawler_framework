# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)


# [BIN] MAIN CRAWLER
START_COUNT = 200
INDEX_COUNT = 200
URL = 'http://base_start_url'


# [DATA] AIM DATA
DATA_FILE = f'{ROOT}/data/data_for_start_url.txt'


# [UTIL] TOOLS
## [DBREDIS]
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '19922'
REDIS_PROXY_NAME = 'crawler_proxy_checked'
REDIS_START_NAME = 'crawler_start'
REDIS_INDEX_NAME = 'crawler_index'


# [UTIL] TOOLS
## [DBPOSTGRESQL]
POSTGRE_HOST = '127.0.0.1'
POSTGRE_PORT = '19921'
POSTGRE_USER = 'postgres'
POSTGRE_PASSWD = 'postgres'
POSTGRE_DBNAME = 'crawler_framework'


# [UTIL] TOOLS
## [DOWNLOADER]
## REQUESTS HEADERS
DOWNLOADER_HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'}
## REQUESTS TIMEOUT
DOWNLOADER_TIMEOUT = 3
## GREQUESTS REQUEST SIZE
DOWNLOADER_SIZE = 30
## GREQUESTS PROXY COUNT (None means unlimited)
DOWNLOADER_PROXY_COUNT = None
