#coding=utf-8
import unittest

import requests


class teststring(unittest.TestCase):

    def setUp(self):
        print('unittest setup')
    def tearDown(self):
        print('unittest teardown')
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    def test_isupper(self):
        """
        测试大小写是否正常
        :return:
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        """
        测试hello world
        :return:
        """
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_baiduisok(self):
        url='http://www.baidu.com'
        res=requests.get(url)
        self.assertEqual(res.status_code,200)


if __name__=="__main__":
    #unittest.main
    print("testsRun:start")
    test_cases=unittest.TestLoader.loadTestsFromTestCase(teststring)
    test_suit=unittest.TestSuite()
    test_suit.addTests(test_cases)
    test_result=unittest.TextTestRunner(verbosity=2).run(test_suit)
    print("testsRun:%s" % test_result.testsRun)
    print("failures:%s" % len(test_result.failures))
    print("errors:%s" % len(test_result.errors))
    print("skipped:%s" % len(test_result.skipped))

    print("testsRun:end")