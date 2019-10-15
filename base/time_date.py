#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: caizhicheng
#Time : 2019/10/15 16:56
#File : time_date.py
import time,datetime

#time.time()返回1970开始的那个时间值,localtime(),strftime('%Y-%m-%d')自定义格式输出
#datetime,可以用来做日期的运算,也可以快速得到日期
#可以用datetime.timedelta来得到一个时间偏移量，再用datetime+/-操作来得到新的时间
def test_time():
    t1=time.time()
    t2=time.localtime()
    t3=time.strftime('%Y-%m-%d %H:%M:%S')
    print(t1)
    print(t2)
    print(t3)
    d1=datetime.date.today()
    d2=datetime.datetime.now()
    d3=datetime.datetime(2018,11,11)
    timeshift=datetime.timedelta(minutes=20)
    print('===============')
    print(d1)
    print(d2)
    print(d1+timeshift)

if __name__ == '__main__':
    test_time()