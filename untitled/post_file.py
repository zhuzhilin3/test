import requests

host='http://httpbin.org/'
enpoint='post'
url=''.join([host,enpoint])

#fangfa 1
#files={'files':open('test.txt','rb')}
#fangfa2
#files={'files':('test.txt','send ssss')}


#fangfa3
#files={'files':open('tttt.jpg','rb')}
#files={'files':('tttt.jpg',open('tttt.jpg','rb'),'image/png')}


#fangfa4
#files=[
#    ('filed1',('text.txt',open('test.txt','rb'))),
#    ('filed2',('tttt.jpg',open('tttt.jpg','rb'),'image/png'))
#]

#fangfa5 liushi
with open('test.txt') as f:
    r=requests.post(url,data=f)

#r=requests.post(url,files=files)
print(r.headers)
print(r.text)