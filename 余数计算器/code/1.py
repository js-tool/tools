# -*- coding:gbk -*-
import os
while True:
    x1 = input("被除数：")
    x2 = input("除数：")
    print "结果：" + str(x1 / x2)
    print "余数：" + str(x1 % x2)
    os.system("pause&cls")
