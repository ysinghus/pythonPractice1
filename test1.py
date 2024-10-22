import string
a=2
b=5
#single line comment
'''dsdas
sd'''

if(b>a):
    print("b is greater than a")
    
print('I will master the PYTHON course')
print("I will master the PYTHON course")
print("""I will master the PYTHON course""")

#multiline statements
#python is case sensitive
b="Carnival"
print(type(b))

b=20;phi=2.718; city='Delhi'
b,phi,city=20,2.718,'Delhi'
b=c=d=e=15

print(10%3)
print (2**3)
print(15//2)

print (2**0.5)
#find square root of a complex number

#5 is 101, 3 is 011

a=3
a += 3
print(a)

#21+7
'''
print(float('123.45'))
name=input('Enter your name:')
name= int(name)
name = name ** 0.5
print(name)'''

import math 
print(math.sqrt(25))

import datetime
current_time=datetime.datetime.now()
print(current_time)

import os
cwd= os.getcwd()
print(f"Current working directory: {cwd}")
items=os.listdir(cwd)
print("items in the current directory",items)

from datetime import date

today=date(2024,10,20)
birthday=date(2025,1,1)
print((birthday-today).days)
print(f"days until birthday:")