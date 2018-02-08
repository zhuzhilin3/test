if __name__=="__main__":
#unittest.main()

    suite=unittest.TestSuite()
    suite.addTest(test_category("test_addCategory"))
    suite.addTest(test_category("test_modifyCategory"))
    suite.addTest(test_category("test_delCategory"))
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename='C:\\Users\\DELL\\Desktop\\2.a .py a report\\'+now+"category.html"
    fp=file(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner( stream=fp, title=u"产品分类测试", description=u"用例执行情况")
    runner.run(suite)
    fp.close()