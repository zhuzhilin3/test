#coding=utf-8

import hashlib



def genearteMD5(str):
    # 创建md5对象
    hl = hashlib.md5()

    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(str.encode(encoding='utf-8'))
    strmd5=hl.hexdigest()
    print('MD5加密前为 ：' + str)
    print('MD5加密后为 ：' + strmd5)

    return strmd5

if __name__=="__main__":
    genearteMD5("")