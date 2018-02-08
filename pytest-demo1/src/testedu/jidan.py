#coding=utf-8

def egg_trick():
    """
    哪鸡蛋的智力题
    :return:
    """

x=range(5000)
for egg_total in x:
    if(egg_total%4!=1):
        continue
    if(egg_total%5!=4):
        continue
    if(egg_total%6!=3):
        continue
    if(egg_total%7!=5):
        continue
    if(egg_total%8!=1):
        continue
    if(egg_total%9!=0):
        continue
    print(egg_total)

print("test egg trick")


def egg_check():
    """
    检查鸡蛋数量
    :return:
    """
    x=range(50000)
    savefile = open('egg.txt', mode='w')
    for i in  x:
        if(i%4==1 \
                and i%5==4 \
                and i%6==3 \
                and i%7==5 \
                and i%8==1 \
                and i%9==0):
            print i
            savefile.writelines(str(i)+"\n")
    savefile.close()

if __name__ =="__main__":
    #egg_trick()
    egg_check()