#coding=utf-8
import requests

def while_fore():
    #requests.post("http://www.baidu.com")
    try:
        req=requests.get("http://www.baidu.com")
        print(req.status_code)
    except BaseException as e:
         print(e)
    finally:
        print "finally"

if __name__=="__main__":
    assert 1==1
    while_fore()