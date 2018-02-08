

import sys
import unittest
import HTMLTestRunner
import time,os


allcase='C:\\Users\\chutf\\PycharmProjects\\uniitled\\unitest'

def createSuite():
    testunit=unittest.TestSuite()

    discover=unittest.defaultTestLoader.discover(allcase,pattern='start_*.py')



allcasenames=createSuite()

now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename='C:\\Users\\chutf\\PycharmProjects\\uniitled\\unitest\\Report\\'+now+"test_all.html"
fp=file(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test report',description='test case')
runner.run(allcasenames)
fp.close()


