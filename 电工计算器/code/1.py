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
    i = input("1：功率计算器\n2：耗电量计算器（输入功率、时间\n3：\
耗电量计算器（输入电压、电流、时间）\n>>>")
    if i == 1:
        v = input("电压：")
        a = input("电流：")
        print "结果" + str(vaw(v, a))
    elif i == 2:
        w = input("功率：")
        h = input("时间：")
        print "结果" + str(whkw_h(w, h))
    else:
        v = input("电压：")
        a = input("电流：")
        h = input("时间：")
        print "结果" + str(vakw_h(v, a, h))
    os.system("pause&cls")
