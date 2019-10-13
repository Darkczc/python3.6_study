#-*- coding:utf-8 -*-

#file
#open  文件位置，读写模式
# f=open('./1.txt','w')
# f.writelines("111\n")
# f.write("222")
# f.close()


#

#with 自动处理关闭文件句柄的操作
map1={}
print(map1.get('aaa'))
with open(r'./1.txt','r') as f:
    for cont in f.readlines():
        print(cont.strip())
        if not map1.get(cont.strip()):
            map1[cont.strip()] = 1
        else:
            map1[cont.strip()] += 1

print(map1)

# ip='192.168.0.101'
# t=ip.split('.')
# print(t,type(t))
#
#
# def get_bin(target):
#     if not target.isdigit():
#         raise Exception('bad ip address')
#     target = int(target)
#     assert target < 256, 'bad ip address'
#     res = ''
#     temp = target
#     for t in range(8):
#         a, b = divmod(temp, 2)
#         temp = a
#         res += str(b)
#         if temp == 0:
#             res += '0' * (7 - t)
#             break
#     return res[::-1]
#
#
# print(get_bin('192'))