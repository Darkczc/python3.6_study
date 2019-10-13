#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: caizhicheng
#Time : 2019/10/13 12:02
#File : iters_generator.py


#生成器yield，return并且能迭代，减少内存占用
def frange(start,end,step):
    x=start
    while x<end:
        yield x
        x+=step

# a = frange(10, 20, 0.5)
# print(type(a))
# for i in a:
#     print(i)

#enumerate()，对[]增加下标成为[()]类型
def test_en():
    l=[1,2,3,4]
    a=enumerate(l)
    print(list(a))
    print(a,type(a))




if __name__== '__main__':
    # test_en()
