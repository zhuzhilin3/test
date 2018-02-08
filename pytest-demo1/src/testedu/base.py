#coding=utf-8

import copy
import math

from testdate import author,print_author

for i in "python":
    if(i=="h"):
        break
    print "当前字符为：",i

var =10
while(var>0):
    print "当前值是:",var
    var = var - 1
    if(var==5):
        break

for i in "python":
    if(i=="h"):
        continue
    print i,
print "\n少了h"

var =10
while(var>0):
    var = var - 1
    if(var==5):
        continue
    print "当前值是:", var
print "少了5"


for i in range(10):
    if(i%2==0):
        continue
    print i,


for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"

vara=1
varb=10
print id(vara)
#del vara
print id(vara)#如果上面del删除成功的话，没有注释，那么这句话执行就会报错


vara=range(1,20)
print vara #不含20
varb=range(1,20,3)
print varb #1开始，步长为3

varc=ord("0")
print hex(varc)
varc=ord("a")
print hex(varc)
varc=ord("A")
print hex(varc)

vard=chr(100)
print vard

vare=abs(-10)
print vare

varf=math.fabs(-10)
print varf

strt=010100
print str(strt)+"11"


a="helloword"
print a[0],a[-len(a)]
print a[len(a)-1],a[-1]
print "ttttt1",a[1:3]


a=[1,2,34,6,88]
print a[0],a[-len(a)]
print a[len(a)-1],a[-1]
print "ttttt2",a[1:3]

a=("hel","trst",1,5,"33")
print a[0],a[-len(a)]
print a[len(a)-1],a[-1]
print "ttttt3",a[1:3]


name_list=["张三","李四","张无极","李叔平","张涛","宋智孝"]
count=0
for i in name_list:
    if("张" in i):
        print i
        count=count+1
print "姓张的总共为",count,"位"



str1="hello"
str2="world"
str3=str1+str2

str4=str3.upper()
print str3
print str4

print "%s %s"%(str1,str2)

print"%d + %f"%(12,23)

print "my first name is %s,my age is %d"%("chu",31)

a=["a","b","c","d"]
print "&".join(a)
print "_".join(a)

str="HFAAaaddASA"
print str.lower()


stra="   sassa"
strb="asdas d  "
strc="  a  s d as  sa"
print stra.lstrip()
print strb.rstrip()
print strc.strip()

stra='a;g;c;d;e'
listb=stra.split(';')
print "split:",listb
listc=listb.pop()
print listc
print listb

listb.sort()
print listb
listb.reverse()
print  listb

#qiankaobei
a=[1,2,3,4,5]
b=a
b[1]="t"
print "浅拷贝",b
print "浅拷贝",a

#shengkaobei
a=[1,2,3,4,5]
print "深拷贝",a
b=a
# b=a.copy()
b[1]="t"
print "深拷贝",a
print "深拷贝",b


def sms_msg(code):
    res_str="中国工商银行提示你，你本地的验证码是%s，不要告诉其他人"%(code)
    return res_str


def if_demo(a):
    if(a>0):
        print "a大于0"
    elif(a==0):
        print "a等0"
    else:
        print "a小于0"


def parm(a,b):
    print "a=%d,b=%d"%(a,b)

def parmdefalt(a=1,b=5):
    print "a=%d,b=%d"%(a,b)


def parmpule(*args):
    #print args
    for i in args:
        print i



def parmdict(**args):

    name=args.get("name",None)
    age=args.get("age",None)
    print "name=%s,age=%d"%(name,age)

def moudle_demo():
    print "author is %s"%author
    print_author()

if __name__ =="__main__":
    code=1233431
    print sms_msg(code)
    if_demo(5.5)
    parm(5,6)
    parm(b=5,a=6)
    parmdefalt()
    parmdefalt(7,8)
    arg=(1,2,3,5)
    parmpule(*arg)#正确调用方式
    #parmpule(arg)  # 错误调用方式

    dict={"name":"张三","age":33}
    parmdict(**dict)
    moudle_demo()