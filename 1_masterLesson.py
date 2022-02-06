##Lesson 43: filter, map, reduce
from functools import reduce

def add_all(a,b):
    return a+b

nums = [1,3,5,2,7,9,12,14,18]

evens = list(filter(lambda n: n%2==0,nums))
print(evens)

doubles = list(map(lambda n : n*2,evens))

print(doubles)

sum = reduce(lambda a,b : a+b,doubles)

print(sum)

## Lesson 44 Decorators
## adding functions to existing function

def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
            return func(a,b)

    return inner


div = smart_div(div)

div(2,4)

## Lesson 45 Modules

### Module "Calc"

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*bdb

def div(a,b):
    return a/b

### Main file
import Calc

a = 9
b = 7

c = Calc.add(a,b)
print(c)

## Lesson 46/47 Special Variable__name__

import Calc

print("Demo Says : " + __name__)

###Module
def main():

    print("Hello")
    print("Welcome User")

####This if statement checks if the file is the main file or just an import
if __name__=="__main__":
    main()

##Lesson 48 Object Oriented Programming
### Class - Design ; Object - Instance

##Lesson 49 Class and Object

class Computer:

    def config(self):
        print("core i7 machine")

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()

a = 5
a.big_length()

##Lesson 50: __init__method


class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ",self.cpu,self.ram)

com1 = Computer('i5',16)
com2 = Computer('Ryzen 3',8)

com1.config()
com2.config()

##Lesson 51: Constructor, Self and Comparing Objects

class Computer:

    def __init__(self):
        self.name = "John"
        self.age = 43

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.update()
c2 = Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name, c1.age)
print(c2.name, c2.age)

##Lesson 52: Types of Variables

class Car:

    #Class Variable
    wheels = 4

    #Instance Variable
    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

##Lesson 53: Types of Methods
###Variables store data, Methods store behavior
###Instance / Class / Static

class Student:

    school = "HKU"

###Constructor
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

###Instance Method - self

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.ml

    def set_m1(self,value):
        self.ml = value


###Class Method -cls, define with @classmethod or @staticmethod

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class..  in abc module")

s1 = Student(23,14,5)
s2 = Student(23,6,11)


print(s2.avg())
print(Student.getSchool())

Student.info()

##Lesson 54 Inner Class (a class wtihin a class)


class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno) ##this prints from outer class
        self.lap.show() ##this prints from inner class

    ##Create Laptop Class INSIDE Student
    class Laptop:

        def __init__(self):
            self.brand = "ASUS"
            self.cpu = 'i7'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('John',2)
s2 = Student('Lillian',3)

s1.show()

###To show inner class has been created, and print the address ID
lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

##Lesson 55 Inheritance

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

###define B as subclass of a class B(A) thereby inherit it
class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B):  ###This is now a sub sub Class
    def feature5(self):
        print("Feature 5 working")

class A2:
    def feature1(self):
        print("Feature A1 working")

    def feature2(self):
        print("Feature A2 working")



###create multiclass
class D(A,A2):
    def feature6(self):
        print("Feature 6 working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

c1 = C()

d1 = D()

d1.feature6()

##Lesson 56: Constructor in Inheritance / MRO

class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")

###define B as subclass of a class B(A) thereby inherit it
class B:

    def __init__(self):
        super().__init__()  ##calls init of superclass A; "Inherits" the constructor
        print("in B Init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):

    def __init__(self):
        super().__init__() ##this automatically get from A first (left to right)
        print("in C init")

    def feat(self):
        super().feature2()

a1 = C()
a1.feature1()
a1.feat()

##Lesson 57: Introduction to Polymorphism (change its type)

##Lesson 58: Duck Typing

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

##Lesson 59: Operator Overloading
###Use definitions to OVERRIDE the default methods

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3

    def __gt__(self, other):  ##This overrided GT
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):  ##This overrides STR
        return self.m1, self.m2

s1 = Student(58,59)
s2 = Student(69,65)
s3 = s1 + s2  ## this is getting converted to -> Student.__add__(s1,s2)

print(s3.m1)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

###if want to print value of object, use __str__()

a = 9
print(a.__str__())  ##Uses overrided def __str__

print(s1.__str__())  ##Uses overrided def __str__

##Lesson 60: Method Overloading and Method Overriding

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        ##Method Overloading: keep default argument to None so if less than 3 values it still works

        s = 0

        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a

        return s


s1 = Student(58,69)

print(s1.sum(5))

###Method Overriding

class A:

    def show(self):
        print("in A Show")

class B(A):  ##inherits A methods but will override it!

    def show(self):
        print("in B Show")

a1 = B()
a1.show()

##Abstract Class

from abc import ABC, abstractmethod

class Computer:
    ##create the abstract class
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

com1 = Laptop()

com1.process()

print(com1)

##Lesson 61: Iterator (Get one by one value)

nums = [7,8,9,5]

it = iter(nums)  #function that converts nums to iterator

print(it.__next__())
for i in nums:
    print(i)
print()

###Part 2

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values))  ###once gotten the values in the iterator, will not run the one below

for i in values:
    print(i)

##Lesson 62 Generators

###Convert this function into a generator
###Use this when want to work with one value at a time
def topten():

    n = 1

    while n<= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()

for i in values:
    print(i)

##Lesson 63 Exception Handling
###Compile Error, Logic Error, Runtime Error

a = 5
b = 2

k = int(input("Enter a number"))
print(k)

###Use try except statement
try:
    print("resource Open")
    print(a/b)

except Exception as e:  ###can use ZeroDivisionError, ValueError to be specific
    print("Hey, You cannot divide number by zero")
    print("Error :", e)  ###print out e as error message
    print("resource Closed after Error")

finally:
    print("resource Closed") ###getting exception or not, it will still execute

print("Bye")

##Lesson 64: MultiThreading

from time import sleep
from threading import *


###put Thread in the object so they have their own Thread
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)  ##ask it to sleep for 1 second

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

###use "start", now they are running in parallel
t1.start()
sleep(0.2)  ###prevents them going into collision
t2.start()

t1.join()  ###asking the treads to wait for each other
t2.join()

print("Bye")

##Lesson 65 File Handling

f = open('MyData','r')  ###open the file MyData to read 'r"

print(f)  ###print file attributes

print(f.read())     ###print entire file

print(f.readline())  ###print only first line
print(f.readline())  ###print lines preceding
print(f.readline(4)) ###print first 4 characters

###Create new file

f1 = open('NewFile', 'w') ###create file and write 'w'
f1.write("Laptop")

f1 = open('NewFile', 'a') ###Open file and append 'a'
f1.write(" belongs to John Z")

###Copy everything in MyData and copy to NewFile

f = open("MyData", 'r') ###open MyData in read mode

f1 = open("NewFile", 'w') ###open NewFile in write mode

for data in f:  ###fetch everything in f then write into f1
    f1.write(data)

###Open an image file and save into another image file
f = open("ShilangPic.jpg",'rb')  ###for image files, read it in binary 'rb'

f1 = open("NewPic.jpg",'wb')  ###Create second file and write binary 'wb'

for i in f:
    f1.write(i)  ###write operation

##Lesson 66 Comments
###Python Virtual Machine PVM converts binary code into machine language

## 68 Linear Search Using Python

pos = -1

def searchwhileloop(list, n):
    i = 0

    while i< len(list):  ###len is the length of the array, or last value
        if list[i] == n:
            globals()['pos'] = i  ###use this to keep track of where in the loop
            return True
        i = i + 1

    return False

def searchforloop(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return True

list = [5,8,4,6,9,2]
n = 9

print(list)

if searchwhileloop(list, n):
    print("Found at ",pos+1) ###+1 to account for zero as first count
else:
    print("Not Found")

if searchforloop(list, n):
    print("Found at ",pos+1) ###+1 to account for zero as first count
else:
    print("Not Found")

## Lesson 69: Binary Search in Python
###Faster way to search

###Need the values to be sorted first

list = [4,7,8,12,45,99,123,124,423,888]

###First, assign First value and Last value, then find Mid index
###Then rotate FIrst value to Mid, then repeat

def searchwhileloop(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l + u) // 2  ####get mid value, use "//" for interger division

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1

    return False

n = 22

print(list)

if searchwhileloop(list, n):
    print("Found at ",pos+1) ###+1 to account for zero as first count
else:
    print("Not Found")


##Lesson 70: Bubble Sort a List
###Swapping concept

def sort(nums):
    for i in range(len(nums)-1,0,-1):###Iterative operation to go through the list
        for j in range(i):
            if nums[j] > nums[j+1]:  ###this is Swapping operation
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [5,3,8,6,7,2]
print(nums)

sort(nums)

print(nums)

##Lesson 71 Selection Sort
###Advantage is not swapping multiple times
###Go start to end find MINIMUM value in each iteration

def sort(nums):

    for i in range(5):
        minpos = i  ### Hold the minimum position
        for j in range(i,6):  ### Shrink size of unsorted array
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [5,3,8,6,7,2]

sort(nums)
