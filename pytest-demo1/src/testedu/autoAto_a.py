#coding=utf-8

def autoAto_a(str):
    """
    把iLoveYouPython转换为i_love_you_python
    :param str:
    :return:
    """
    strtemp=""
    for i in range(len(str)):
        c=str[i]
        #print c
        if(ord(c)>=0x41 and ord(c)<0x61):
            c="_"+c.lower()
        strtemp=strtemp+c
    print(strtemp)
    if(strtemp[0]=="_"):
        res=strtemp[1:len(strtemp)]
        print(res)
    return res




if __name__=="__main__":
    str="ITestLoveYouPython"
    autoAto_a(str)

