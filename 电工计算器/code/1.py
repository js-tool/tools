# coding:gbk
from __future__ import division
import os


def vaw(v, a):
    w = v * a
    return w


def whkw_h(w, h):
    kw = w / 1000
    kw_h = kw * h
    return kw_h


def vakw_h(v, a, h):
    w = vaw(v, a)
    kw_h = whkw_h(w, h)
    return kw_h


while True:
    i = input("1�����ʼ�����\n2���ĵ��������������빦�ʡ�ʱ��\n3��\
�ĵ����������������ѹ��������ʱ�䣩\n>>>")
    if i == 1:
        v = input("��ѹ��")
        a = input("������")
        print "���" + str(vaw(v, a))
    elif i == 2:
        w = input("���ʣ�")
        h = input("ʱ�䣺")
        print "���" + str(whkw_h(w, h))
    else:
        v = input("��ѹ��")
        a = input("������")
        h = input("ʱ�䣺")
        print "���" + str(vakw_h(v, a, h))
    os.system("pause&cls")
