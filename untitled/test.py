import requests

host = 'http://httpbin.org/'
#hosttest = 'https://www.zhidaow.com'

meth='get'
urltest="".join([host,meth]);
print(urltest);
r = requests.get(host);
print(r.url);
print(r.headers);
print(r.text);
print(r.reason);
print(r.request);
print(r.status_code);