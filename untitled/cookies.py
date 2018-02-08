import  requests

host = "http://httpbin.org/"
enpoint='cookies'
url=''.join([host,enpoint])
url1='http://www.baidu.com/'

r=requests.get(url)
print(r.cookies)
print(r.text)
d=requests.utils.dict_from_cookiejar(r.cookies)
print(d)
print({a.name:a.value for a in r.cookies})

cookies={'cookies-name':'chutianfeitest'}
r1=requests.get(url,cookies=cookies)
print(r1.text)

s=requests.Session()
c=requests.cookies.RequestsCookieJar()
c.set('cookie-name','cookie-value',path='/',domain='.test.com')
s.cookies.update(c)
print(s.cookies)

