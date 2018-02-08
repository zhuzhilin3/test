import requests
import  json

host="http://httpbin.org/"
enpoint="post"
url=''.join([host,enpoint])

date={
 "info":{"code":1,"sex":"nan"},
 "code":1,
 "sex":"nan",
 "date":[{"code":1,"sex":"nan"},{"code":1, "sex":"nan"}],
 "id":1900
}

#r=requests.post(url,data=json.dumps(date));
r=requests.post(url,json=date)
print(r.text);
resp=r.json();
print(resp);
print(resp['json']);