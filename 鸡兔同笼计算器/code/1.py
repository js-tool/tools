# coding=gbk
import os
while True:
    head = input("������ͷ����")
    z = input("������������")
    big = input("�������ģ�")
    small = input("�������ٵģ�")
    cha = big - small
    x = str((z - small * head) / cha)
    y = str(head - int(x))
    print "����ǣ�"
    print "��ģ�" + x
    print "�ٵģ�" + y
    os.system("pause&cls")
