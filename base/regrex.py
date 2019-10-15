#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: caizhicheng
#Time : 2019/10/15 15:38
#File : regrex.py
import re

#re.compile()得到正则表达式匹配模式pattern;match/search通过pattern来得到匹配结果,match和=search里的参数是待正则匹配的原始数据
#常用的re符号  . ^ * + ? {m} {m,n} | \D \d \s (),^在[]外面表示以开头，在[]里面表示非
#  * 0~n 次，+ 1~n次，? 0~1次，[0-9] 范围表达，\d+  =[0-9]+ 数字 \D [^0-9]
#贪婪模式，默认.*会匹配到最长的，而.*?只匹配到第一个符合的,.*?就是非贪婪模式
#分组功能用()先分组，然后用group(下标)来得到对应的匹配结果,groups()得到分组元组
#match是完全匹配，从第一位开始，search是查找,#
#match从目标字符串的开始进行匹配一旦不符合pattern就返回none,search也是从字符串开始匹配，但是如果第一个字符不符合可以后移，直到末尾都不符合才返回none
#sub用来进行替换，类似shell的sed,(，，)参数分别放置pattern匹配模式，要转化成的内容，被处理初始数据
def test():
    pat=re.compile(r'(\d+)-(\d+)-(\d+)')
    # res=pat.match('2019-10-01')
    res=pat.search('aaa2019-10-01bbb')
    print(res.group(1),res.groups()[1])
    year,month,day=res.groups()
    print(year,month,day)
    s1=re.sub(pat,'8888-8888-8888','aaa2019-10-01bbb')
    print(s1)
if __name__=='__main__':
   test()