#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Description:Study python class related
#History
#Date           User                History
#04-May-2017    Levi Li             Initial
#-----------------------------------------------------------------------------------------------------
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "%s age is %d"%(self.name, self.age)
    def __cmp__(self, other):
    __repr__ = __str__
if __name__=="__main__":
    m_xiaoMing = Person("Xiao Ming",10)
    m_xiaoQiang = Person("Xiao Qiang",25)
    print(m_xiaoMing)
    print(m_xiaoQiang)