import  requests


host='http://httpbin.org/'
enpoint='cookies/set/sessioncookie/12345678'

url=''.join([host,enpoint])
url1='http://httpbin.org/cookies'


r=requests.get(url1)
print(r.text)

session=requests.Session()
session.get(url)
r1=session.get(url1)
print(r1.text)



headera={'testa':'aaaa'}
headerb={'testb':'bbbbb'}
sessiona=requests.Session()
sessiona.headers.update(headera)
urlheader='http://httpbin.org/headers'
ra=sessiona.get(urlheader,headers=headerb)
print(ra.text)



sessiona.headers['testa']=None
r3=sessiona.get(urlheader,headers=headerb)
print(r3.text)


