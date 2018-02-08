#coding=utf-8

import qrcode

opfile = open('gshmc.csv', mode='r')
count=0
for i in opfile.readlines():
    count=count+1
    print i
    data = i
    img_file = r'D:\tmp\qrcode%d.png'%count
    img = qrcode.make(data)
    # 图片数据保存至本地文件
    img.save(img_file)
opfile.close()




# # 显示二维码图片
# img.show()