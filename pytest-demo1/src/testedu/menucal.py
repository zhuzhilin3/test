#coding=utf-8
def jia(a,b):
    """
    加法计算
    :param a:
    :param b:
    :return:
    """
    print "%d+%d=%d"%(a,b,a+b)
    return  a+b

def jian(a,b):
    """
     减法计算
    :param a:
    :param b:
    :return:
    """
    print "%d-%d=%d" % (a, b, a - b)
    return a - b


def cheng(a,b):
    """
     乘法计算
    :param a:
    :param b:
    :return:
    """
    print "%d*%d=%d" % (a, b, a*b)
    return a * b

def chu(a,b):
    """
     除法计算
    :param a:
    :param b:
    :return:
    """
    if(b!=0):
        print "%d/%d=%d" % (a, b, a/b)
        return a / b
    else:
        print "被除数不能为0"

if __name__ =="__main__":
    testa=1
    testb=testa
    print id(testa),id(testb)
    testa=5
    print id(testa), id(testb)
    testc="hello python"
    print id(testc)
    testc="testhello"
    print id(testc)

    testlist=[1,2,4,6,"testd"]
    print id(testlist)
    testlist=[2,2,4,6,"testd"]
    print id(testlist),testlist
    testlist[0]="hello"
    print id(testlist),testlist


    testtuple=(1,2,3,5,6)
    print id(testtuple)
    #testtuple[0]=2  #不可变
    print id(testtuple)


    testdict={"key1":"value1","key2":"test2","key3":3}
    print id(testdict),id(testdict["key2"]),id(testdict["key3"]),testdict
    testdict["key2"]=5
    print id(testdict),id(testdict["key2"]),id(testdict["key3"]),testdict


    while 1:
       a=input("1｜加法  2｜减法 \n"+"3｜乘法  4｜除法\n")
       if(int(a)==1):
           print"你选择了加法计算"
           i = input("请输入第一个数字")
           j = input("请输入第二个数字")
           jia(int(i),int(j))
           continue
       if(int(a)==2):
           print "你选择了减法计算"
           i = input("请输入第一个数字")
           j = input("请输入第二个数字")
           jian(int(i), int(j))
           continue
       if(int(a)==3):
           print "你选择了乘法计算"
           i = input("请输入第一个数字")
           j = input("请输入第二个数字")
           cheng(int(i), int(j))
           continue
       if(int(a)==4):
           print "你选择了除法计算"
           i = input("请输入第一个数字")
           j = input("请输入第二个数字")
           chu(int(i), int(j))
           continue
       else:
           print"输入错误，请重新输入"


