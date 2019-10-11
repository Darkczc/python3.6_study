#-*- coding:utf-8 -*-
import json
#string
a='你好\n你们'
if '\n'  in a:
    print(u'是的'+u'才怪')
    print(u'是的'*2)
    print(u'是的'[:1])

b=2018

#元组
c=(3,2)
print(type(c))


array=[2,1,9,0]
a1=[item for item in array[1:] if item <array[0]]
print(a1)
qk_sout=lambda array:array if len(array)<=1 else qk_sout([item for item in array[1:] if item <array[0]])+[array[0]]+qk_sout([item for item in array[1:] if item > array[0]])

print (qk_sout(array))
fc=lambda x:x<10
print(fc(3))


#list类型
#操作
l1=[1,2,3,4]
#CRUD
l1.append('5')
l1.insert(2,{"a":5})
l1.remove({"a":5})
l1.pop()
print(l1)
print(1 in l1)



#字典
#key是不可变类型，不能是[]，value随意
#CRUD
#直通通过dic['key']=赋值来新增/更新元素
#dic.get()
z='wnt'
d={}
for i in z:
    d[i]=0
#python2中的item()是一个值copy过程，会占用内存,iteritems返回一个迭代器，不占内存，时间复杂度也低，py3将iteritem的实现在item上
print(d.values(),type(d.keys()))
for j in d.keys():
    print(j)
for k in d.items():
    print(k)


#[]和{}的推导式，快速生成过滤性对象
print([i+1 for i in range(10)])
print([i*i for i in range(2,10)])
print({i:"k" for i in  range(5)})

#测试传参和golang的过程差异，是否进行值copy还是会影响原值
def par(x,y):
    for i in range(len(x)):
        if x[i]<y:
            x[i]=y
    print(x)



par(l1,2)
print(l1)

#可以看到python在函数内部对元素修改会改变他的原值，因此不是值copy
