#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: caizhicheng
#Time : 2019/10/15 17:38
#File : math_rand.py

import random
# random主要几个方法，random()返回一个0.xxx的浮点数
# randint(a,b)返回一个随机整数，其中()内代表 x>a&&x<b的[]
# randrange(a,b,c)类似于randint,c代表[]元素之间的step
# choice从一[]里随机选一个元素
# sample([],int)从一个[]里随机选n个数
def test_math():
    r1=random.sample([x+x for x in '[a-z]'],2)
    r2=random.randint(2,10)
    print(r1,r2)
    l=[x for x in range(10)[1:10]]
    print(l)
if __name__ == '__main__':
    test_math()