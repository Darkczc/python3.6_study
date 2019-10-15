#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: caizhicheng
#Time : 2019/10/15 12:50
#File : thread.py
import threading
from threading import current_thread,Thread
from queue import Queue
import  time
import random

def test_thread(a1,a2):
    print(current_thread().getName(),current_thread().ident)
    print('{},{}'.format(a1,a2))

quene=Queue(5)


#Queue类类似golang的channel，支持并发读写，可以定义queue长度，queue消费端每次get完可以通过task_done来告诉queue这把的任务已经完成了
class Producter(Thread):
    def run(self):
        name=current_thread().getName()
        nums=range(100)
        global quene
        while True:
            seq=random.choice(nums)
            quene.put(seq)
            sleeptime=random.choice([1,2,3])
            print('生产者{},id{},生产->{}'.format(current_thread().getName(),current_thread().ident,seq))
            time.sleep(sleeptime)

class Consumer(Thread):
    def run(self):
        name=current_thread().getName()
        global quene
        while True:
            ack=quene.get()
            # quene.task_done()
            sleeptime=random.choice([1,2,3])
            print('消费者{}，id{},消费<-{}'.format(current_thread().getName(),current_thread().ident,ack))
            time.sleep(sleeptime)

if __name__=='__main__':
    # a1='aaa'
    # a2='bbb'
    # t1=threading.Thread(target=test_thread,args=(a1,a2))
    # t1.start()
    # t1.join()
    p1=Producter()
    p1.start()
    c1=Consumer()
    c1.start()
    c2=Consumer()
    c2.start()
