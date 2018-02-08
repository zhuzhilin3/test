#coding=utf-8
"""
这个是计算器程序
jia
jian
cheng
chu
a
b
"""

def jia(a,b):
    return a+b

def jian(a,b):
    return a-b

def cheng(a,b):
    return a*b

def chu(a,b):
    if(b!=0):
        return a/b
    else:
        return "除数不能为0"

if __name__ == "__main__":
    c=jia(1.1,2)
    print(c)

    c=jian(1,3)
    print c

    c=cheng(2,5)
    print c

    c=chu(20,5)
    print c

    c=chu(2,0)
    print c
