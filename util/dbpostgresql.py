# -*- coding: utf-8 -*-

import os
import sys
ROOT = os.getcwd()
sys.path.append(ROOT)

import re
import psycopg2
import traceback

import config
from util import logger


class DBPostgresql():

    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.host = config.POSTGRE_HOST
        self.port = config.POSTGRE_PORT
        self.user = config.POSTGRE_USER
        self.passwd = config.POSTGRE_PASSWD
        self.dbname = config.POSTGRE_DBNAME
        self.conn = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.passwd, dbname=self.dbname)
        self.logger = logger.Logger()
    
    def create(self, tablename, **kargs):
        '''
        kargs input: field='field type'
        '''
        option = []
        for key, value in kargs.items():
            option.append(f'{key} {value}')
        optionsql = str(tuple(option)).replace('\'', '')
        try:
            self.conn.cursor().execute(f"CREATE TABLE {tablename}_{self.timestamp} {optionsql};")
            self.conn.commit()
        except Exception:
            error = traceback.format_exc()
            self.logger.error(message=f'<postgresql> <create> {error}')
            self.conn.rollback()
        
    def insert(self, tablename, **kargs):
        '''
        kargs input: field='field value'
        '''
        columns, values = [], []
        for key, value in kargs.items():
            columns.append(key)
            if type(value) == str:
                values.append(self.__clear(value))
            else:
                values.append(value)
        columns_query = str(tuple(columns)).replace('\'', '')
        values_query = str(tuple(values))
        try:
            self.conn.cursor().execute(f"INSERT INTO {tablename}_{self.timestamp} {columns_query} VALUES {values_query};")
            self.conn.commit()
        except Exception as error:
            error = traceback.format_exc()
            self.logger.error(message=f'<postgresql> <insert> {error}')
            self.conn.rollback()

    def __clear(self, string):
        '''
        clear value
        '''
        delete = re.compile(r'[\n\r\t\'\"]')
        result = re.sub(delete, '', string)
        return result
