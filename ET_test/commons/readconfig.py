#coding=utf-8

def get_resources():
    file=open('../config/resources.txt',mode='r')
    for i in file.readlines():
        print(i)

if __name__=="__main__":
    get_resources()