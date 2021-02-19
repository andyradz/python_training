

import matplotlib.pyplot as plt
import sys
import math
import numpy as np
from modnum import fib as fibonacci
from decimal import Decimal
from modsets import PrintOddNumber, PrintEvenNumber, Person, Student, Employee
import pandas as pd


def my_function(text):
      print(text)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)      

msg = "Hello;World;i;Andrzej;Radziszewski"


msg.capitalize()
msg.split(sep=";", maxsplit=2)

my_function(msg)


my_function(next(myit))
my_function(next(myit))
my_function(next(myit))

mystr = "banana"

for x in mystr:
  print(x)

myset = {"apple", "banana", "cherry", "zack", "basia", "stasia", "kasia"}  
myset.add("andrzej")
print("banana" in myset)

#https://www.programiz.com/python-programming/methods/built-in/next
sorted(myset)

for x in sorted(myset, reverse=True):
      print(x)

fibonacci(100)

resmax = max(10,-1)
resmin = min(10,-1)
print(resmax)
print(resmin)

# normal float
num = 2.675
print(round(num, 2))

# using decimal.Decimal (passed float as string for precision)
num = Decimal('2.675')
print(round(num, 2))

# print_num is an iterable
print_num = PrintOddNumber(20)
# creating a set
print(set(print_num))

# print_num is an iterable
print_num = PrintEvenNumber(20)
# creating a set
print(set(print_num))

#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
#plt.plot(x, np.sin(x))       # Plot the sine of each x point
#plt.show()                   # Display the plot

#python -m pip install matplotlib

array = ['A','B','C']
array[0]='0'
array[1]='1'
array[2]='2'
array.append("max")

operator = lambda a: print(('_' + a.upper()))
for item in array:
      operator(item)

power = lambda factor : factor**2 * (-1)     
print(power(4))
print(pow(2,10))


#first dictionary

glossary = {
      "name":"andrzej",
      "age":"26"}

print(glossary['name'])

"""
username = input("Enter username:")
print("Username is: " + username)
"""

person = Person("andy", "koks", 42)
print(person.name + person.surname + str(person.age))
person.toString()
Person.circle_area(12)


student = Student("andy", "koksiarz", 42, "i-009923")
print(student.name + student.surname + str(student.age) + student.index)
print(student.toString())

employee = Employee("stefek", "buła", 27, "developer")
print(employee.name + employee.surname + str(employee.age) + employee.profesion)
print(employee.toString())

set1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
set2 = {'z':-1}
union = {**set1, **set2}
print(type(student))
