#coding=utf-8
def helloword():
    print "hello word，你好世界"


def testhello():
    print "test hello word"



if __name__ == "__main__":
     helloword()
     testhello()
     a=1
     b=input("请输入数字：")
     c=a+int(b)
     print c
     strtemp=""
     inputfile=open('input.txt',mode='r')
     for line in inputfile.readlines():
         strtemp=strtemp+line
     print(strtemp)
     outputfile=open('outsavefile.txt',mode='w')
     outputfile.writelines(strtemp)
     outputfile.writelines("\n"+str(c))
     outputfile.writelines("\n以上是输出保持的结果")
     outputfile.close()
