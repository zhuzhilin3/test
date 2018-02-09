#coding=utf-8

import  requests
import json

def get_token():
    url='http://192.168.1.26:83/easytong_app/api/token'
    resfile=open('../config/resources.txt',mode='r')
    str=resfile.readlines()
    appid='8C2A7F7C3B8667293F43C298AE94D674'
    appsecret='C6B36E783888D1F4694B11EE91E21539'
    d= {'appid':appid,'appsecret':appsecret}
    res=requests.get(url,params=d)
    print (res.url)
    print (res.status_code)
    print(res.text)
    res_list=json.loads(res.text)
    token=res_list['access_token']
    print('token:',token)
    return token

def get_sign(**vargs):



def get_account():

    url='http://192.168.1.26:83/easytong_app/api/infoqueryservice/getaccount'
    access_token=get_token()
    queryType='1'
    idType=''
    uniqueId='100142'

    sign=
    d = {'access_token': access_token}
    res = requests.post(url, data=d)
    print(res.url)
    print(res.status_code)
    print(res.text)


if __name__=='__main__':
    get_token()

