# coding=gbk
import os
while True:
    head = input("请输入头数：")
    z = input("请输入腿数：")
    big = input("请输入多的：")
    small = input("请输入少的：")
    cha = big - small
    x = str((z - small * head) / cha)
    y = str(head - int(x))
    print "结果是："
    print "多的：" + x
    print "少的：" + y
    os.system("pause&cls")
