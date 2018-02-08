import  requests

#basic

r=requests.get('http://httpbin.org/basic-auth/user/passwd',auth=('user','passwd'))
print(r.text)


#fangfa2
from requests.auth import HTTPBasicAuth
r1=requests.get('http://httpbin.org/basic-auth/user/passwd',auth=HTTPBasicAuth('user','passwd'))
print(r1.text)



#ZHAIYAO
from requests.auth import HTTPDigestAuth
r2=requests.get('http://httpbin.org/digest-auth/auth/user/passwd/MD5',auth=HTTPDigestAuth('user','passwd'))
print(r2.text)
