#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: caizhicheng
#Time : 2019/10/13 10:35
#File : functions.py
from functools import reduce

#和golang一样，函数传参也是浅copy，依据原参的类型决定是值copy还是,不可变类似是值copy，可变类型是指针copy
#和golang一样，[] {}等是可变类型，其他都是不可变，比较好理解
var1="sss"
l={}
def func(var1,list):
    var1="bbb"
    list[var1]="111"
    print(var1,list)

# func(var1,l)
# print(var1,l)



#高阶函数 filter,map,reduce,zip，sorted(filter,map,zip返回一个iter，reduce返回一个准确值,sorted直接返回一个list,sorted在py3中不再是高阶函数)
#filter(f,可迭代对象)过滤不满足条件的元素，返回一个过滤后的iter ,可以用list包起来形成list ，同理map reduce;f函数的返回值必须是true/false
#reduce略微不同于其他的高阶函数，reduce(f,iterable,initilazer)每次去可迭代对象中的2个元素进行f运算，运算的结果会和下一个可迭代对象中拿出的元素组成类似第一次的样子进行f函数，如果有初始值，就拿初始值和可迭代对象中的第一个元素进行f操作，依次类推
def big_4(x):
    return x>4


def map1(x):
    return x**2
def test_map():
    l=[2,1,3]
    print(list(map(map1,l)))



def minux_xy(x,y):
    return x+y

def test_filter():
    l=[3,4,5,6]
    l2=filter(big_4,l)
    print(next(l2))
    print(next(l2))


def test_reduce():
    l=[3,4,5,6]
    l3=reduce(minux_xy,l)
    print(l3)

#zip函数用于组合多个一维数组成一个二维数组
def test_zip():
    l1=[3,4,2,1]
    l2=['a','b','c','d']
    l3=['zz','yy','xx']
    print(list(zip(l1,l2,l3)))


def sort_rn(x,y):
    if x<y:
        return 1
    elif x==7:
        return 0
    else:
        return 1
#sorted(f,l)用f对list进行排序，默认从小到大排序
def test_sort():
    l1=[2,1,3]
    print(sorted(l1))



#函数嵌套和闭包
#f1函数定义返回的是函数名f2，这样调用f1(a)(b)才能真正完成这个函数的调用，注意f1(x)只是return f2，但是f2只是个函数名，所以还得传一个参数，所以是f1(a)(b)=f2(b)/x=a
def f1(x):
    def f2(y):
        return x*y
    return  f2




#计数器和内存释放
#这个内容涉及到变量的作用范围，py有LEGB的规则，local-enclosing(闭包)-global-built-in，如果内部函数的变量还没有被声明就做了运算，是违法的，如果外部函数有这个变量,也就是闭包内有定义这个变量，那么可以通过使用nonlocal在内部声明一下，如果想使它成为全局变量，可以使用global来申明，那么他就可以使用全局变量的初始值来进行计算,LEGB的优先级L>E>G>B

#全局有效的作用域的变量类型[],{},(),其他都被对应的作用域取代，
def counter():
    # cnt=0
    cnt=[0]
    def f1():
        # nonlocal  cnt
        # cnt+=1
        cnt[0]+=1
        return cnt
    return f1


#闭包可以用来制造工厂函数，宽泛的来表示一种线性关系可以用闭包,使用line1=line(3,4)来得到3x+4和line2=line(-1,1)得到-x+1这两条直线函数
def line(a,b):
    def ll(x):
        return a*x+b
    return ll





if __name__=='__main__':
    # test_filter()
    # test_reduce()
    # test_zip()*
    # test_sort()
    # test_map()
    # print(f1(1)(10))
    num1=counter()
    print(num1())
    print(num1())
    # print(cnt[0])
