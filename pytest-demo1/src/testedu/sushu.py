#encoding=utf-8

for i in range(2,100):
    j=2
    while(j<=i/j):
        if(i%j==0):
            break
        j=j+1
    if(j>i/j):
        print i ,"是素数"
    i=i+1
print "goodbye"

a=1
print a is None
a=None
print a is None
a=False
print a is None
