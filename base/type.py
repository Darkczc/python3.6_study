#-*- coding:utf-8 -*-

#string
a='你好\n你们'
if '\n'  in a:
    print(u'是的'+u'才怪')
    print(u'是的'*2)
    print(u'是的'[:1])


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
