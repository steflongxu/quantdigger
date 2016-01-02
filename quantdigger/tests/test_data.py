# -*- coding: utf-8 -*-
import pandas as pd
import os
import unittest
from logbook import Logger
logger = Logger('test')

class TestDataSource(unittest.TestCase):
    def test_local_data(self):
        logger.info('***** 数据测试开始 *****')
        from quantdigger.datasource.data import LocalData
        """ 测试本地数据接口 """ 
        db = LocalData()
        target = db.load_data('BB.SHFE-1.Minute')

        fname = os.path.join(os.getcwd(), 'data', 'CC.SHFE-1.Minute.csv')
        source = pd.read_csv(fname, parse_dates='datetime', index_col='datetime')
        self.assertFalse(source.equals(target), '本地数据接口负测试失败！')

        fname = os.path.join(os.getcwd(), 'data', 'BB.SHFE-1.Minute.csv')
        source = pd.read_csv(fname, parse_dates='datetime', index_col='datetime')
        self.assertTrue(source.equals(target), '本地数据接口正测试失败！')
        logger.info('-- 本地数据接口测试成功 --')
        logger.info('***** 数据测试结束 *****\n')

## @TODO test rolling_foward

if __name__ == '__main__':
    unittest.main()
