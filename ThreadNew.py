#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Description:Study multiple thread
#History
#Date           User                History
#16-Apr-2017    Levi Li             Initial
#29-Apr-2017    Levi Li             Add class myThreadControl
#-----------------------------------------------------------------------------------------------------
import threading
import time

exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting" + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print( "%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

def thread_control_sample():
    '''
    This sample is copy from web.
    :return:
    '''
    # 创建新线程
    thread1 = myThread(1,"Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # 开启线程
    thread1.start()
    thread2.start()
    print("Exiting Main Thread")


'''
The following classes and method are creaded by myself
'''
class myThreadControl(threading.Thread):
    def __init__(self,threadName, printCounts, sleepTime):
        threading.Thread.__init__(self)
        self.threadName=threadName
        self.sleepTime=sleepTime
        self.printCount=printCounts
    def run(self):
        printNameByThread(self.threadName,self.printCount,self.sleepTime)

def printNameByThread(threadName,printCount,sleepTime):
    idx=1
    while(idx<=printCount):
        print("This is %d times printing by thread %s"%(idx,threadName))
        idx+=1
        time.sleep(sleepTime)

def thread_control_self_created():
    slowThread = myThreadControl("slow", 5, 1.5)
    fastThread = myThreadControl("fast", 5, 1)
    slowThread.start()
    fastThread.start()
if __name__=="__main__":
    #thread_control_sample()
    thread_control_self_created()
