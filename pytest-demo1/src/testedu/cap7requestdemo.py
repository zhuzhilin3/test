#coding=utf-8
import json

import requests

def requests_get_xml_demo():
    url='http://www.baidu.com'
    res=requests.get(url)
    print res.url
    print "code:",res.status_code

def requests_get_json_demo():
    url='https://api.github.com/events'
    res=requests.get(url)
    print(res.url)
    print(res.status_code)

    res_str=res.text
    res_list=json.loads(res_str)
    print(len(res_list))
    for my_dict in res_list:
        print (my_dict['id'])


if __name__=="__main__":
   # requests_get_xml_demo()
    requests_get_json_demo()