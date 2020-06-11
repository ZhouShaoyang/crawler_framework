# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

import re
import logging


class Logger():

    def __init__(self):
        self.logger = logging
        self.log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
        self.date_format = '%Y-%m-%d %H:%M:%S'
        self.log_file = f'{ROOT}/log/crawler.log'
        self.logger.basicConfig(level=logging.INFO, format=self.log_format, datefmt=self.date_format, filename=self.log_file)

    def info(self, message):
        self.logger.info(msg=self.__formater(message=message))

    def error(self, message):
        self.logger.error(msg=self.__formater(message=message))

    def __formater(self, message):
        return re.sub(re.compile(r'\s+'), ' ', message)
