#coding=utf-8
#Initialized by Levi Li
#Date: 19-Apr-2017
#Discription: multiple thread study
#History
#--------------------------------------------------------
#Date               Useer                   Discription
#16-Apr-2017        Levi Li                 Initial
#--------------------------------------------------------
from time import ctime , sleep
import threading

def Process1():
    for i in range(100):
        print("c1 %s"%(ctime()))
        print(threading.current_thread())
        sleep(0.3)

def Process2():
    for i in range(100):
        print("c2 %s"%(ctime()))
        sleep(0.5)

def OneThreading():
    Process1()
    Process2()

def MultiThreading():
    threads=[]
    t1=threading.Thread(target=Process1())
    #threads.append(t1)
    t2=threading.Thread(target=Process2())
    #threads.append(t2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__=='__main__':
    #OneThreading()
    MultiThreading()
