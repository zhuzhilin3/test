#coding=utf-8

import sys
sys.path.append("\unitest")
from test_case import *
import unittest
import HTMLTestRunner
import time

#注意使用套件时，在单个py文件中下的多个用例用  (类名（"方法名")),
#导入多个py的类下，用（py名.类名）

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(category.test_category))
suite.addTest(unittest.makeSuite(product.test_product))

now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename='C:\\Users\\DELL\\Desktop\\Report\\'+now+"test_all.html"
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'产品管理和分类管理的自动化测试报告',description=u'测试用例结果')
runner.run(suite)
fp.close()