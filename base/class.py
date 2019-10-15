#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: caizhicheng
#Time : 2019/10/15 11:51
#File : class.py
import time


#类的定义.使用super可以复用父类的方法，避免重复性定义
class Animal(object):
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def output(self):
        print(self.name,self.type)

class Cat(Animal):
    def __init__(self,name,type):
        super().__init__(name,type)
    def output(self):
        super().output()

#可以用type查看类名，可以用isinstance查看2个类之间是否有父子继承关系,注意第一个参数必须是一个类的实例而不是类名
def test_class():
    a=Animal('dog','run')
    b=Cat('bull','cat')
    a.output()
    b.output()
    print(type(a))
    print(isinstance(Cat('bird','fly'),Animal))


#__enter__,__exit__能控制实例创建和结束时候动作
class Test(object):
    def __enter__(self):
        print('this is start')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('this is over')


def test_class_2():
    with Test():
        print('starting')
        time.sleep(1)
        print('111')



if __name__=='__main__':
    # test_class()
    test_class_2()