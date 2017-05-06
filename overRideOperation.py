# File name: overRideOperation.py
# Create Date: 06-May-2017
# Author:  Liyan
# Function: Mainly to study object oriented programming


import math


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        c=math.gcd(self.p,self.q)
        return "%s/%s" % (self.p/c, self.q/c)
    __repr__ = __str__

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return float(self.p) / self.q


def rational_class():
    r1 = Rational(1, 2)
    r2 = Rational(1, 4)
    print (r1 + r2)
    print (r1 - r2)
    print (r1 * r2)
    print (r1 / r2)
    print(float(Rational(7, 2)))
    print(float(Rational(1, 3)))


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.__score>=80:
            return "A"
        elif self.__score<60:
            return "C"
        else:
            return "B"


def student_class():
    s = Student('Bob', 59)
    print(s.grade)
    s.score = 60
    print(s.grade)
    s.score = 99
    print(s.grade)


class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender



class StudentSlots(Person):

    __slots__ = ('score')

    def __init__(self, name, gender, score):
        super(StudentSlots, self).__init__(name, gender)
        self.score = score


def student_slot_class():
    s = StudentSlots('Bob', 'male', 59)
    s.name = 'Tim'
    s.score = 99
    print(s.score)



class Fib(object):
    def __call__(self,number):
        a,b,L=0,1,[]
        for i in range(number):
            L.append(a)
            a,b=b,a+b
        return L

def fib_class():
    f = Fib()
    print(f(10))

if __name__ == "__main__":
    rational_class()
    student_class()
    student_slot_class()
    fib_class()