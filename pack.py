"""
def function(named_arg,*args):  # name_arg=1 and args=2,3,4,5
   print(named_arg)
   print(args)

def function1(*args):
    print(args)

function(1,2,3,4,5)
function1(1,2,3,4,5)
"""

"""
def fun(name,*arg): # we can also called def fun(name,name2,*arg)

    for i in arg:
        print(i**name)

fun(2,3,4,5)

def fun1(name,*arg):
    print(arg)
    for i in arg:
        print(i+name)

fun1("ram","sita","laxmi")

"""

"""
def fun(x,y,z="apple"):
    print(x+y)
    print(z)

fun(1,2)
fun(3,4,z="orange")
fun(3,4,z="6")


def fun1(a="apple"):
    print(a)
fun1("grapes")

def fun2(a=""):
    print(a)

fun2("noone")
"""
"""
def fun(x,y=7,*args,**kwargs):
    print(x+y)
    print(args)
    print(kwargs)

fun(1,2,3,4,5,a=6,b=7)
"""
"""
numbers=(1,2,3)

a,b,c=numbers

print(a)

a,b,c=c,b,a

print(a,b,c)

a=b+c
print(a)

c=a+b
print(c)
"""
"""
a,b,c,*d=[1,2,3,4,5,6,7,8]
print(a)
print(b)
print(c)    # *c prints left over values i.e a=1 b=2,d=last value i.e 8 and rest for c i.e *c takes all values
print(d)

print("\n")

a,b,*c,d=(1,2,3)  # c prints  []
print(c)
"""

"""

a=3

b=5 if a>=4 else 7
print(b)

word1="ram"
word3="hari"
word2="sita" if word1=="ram" else "noone"
word21="geeta" if word3=="hari" else "noone1"
print(word21)
print(word2)
"""

"""
#You are given a program for a bank card withdrawals system.
#Code to get the money available on your balance.

#ternary operator

code="A1B1 NIC"

balance="10000000" if code==code else "wrong code"

print(balance)


# short cut method
a = 7
print(1 if a >= 5 else 42)

"""
"""
# Write a program that breaks the loop and outputs 'Too young!'
# in case of finding a value less than 16.

for i in range(16,20):
    if i>15:
        pass
else:
    print("Too Young")

#eg
for i in range(50):
    if i==51:
        break
else:
    print("finished")
"""
"""
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break   # break means exit the loop if we put pass then "unbroken 2 " will be printed
else:
    print("Unbroken 2")
"""
"""
for i in range(16,20):
    if i>15:
        break
else:
    print("not ")
"""
"""
try:
    print(1/0)
except ZeroDivisionError:
    print(2) # 2 is printed because zero division error occur
             # so else is not executed after exception occurs
else:
    print(3)

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)
"""

"""
# To order a restaurant dish online, the user should enter the
# code of the desired dish, which contains only digits.

import re

code=input("Enter Your Code : ")

pattern=r"(pizza)([A-Z])([0-9])([a-z])"

if re.match(pattern,code):
    print("your order has been packed")
else:
    print("Incorrect code, Please! re-type your code")
"""

"""
def good(string):
    return f"the good one {string}"

def bad(num1,num2):
    return num1+num2

if __name__=="__main__":
    print(good("boy"))
    print(bad(3,2))

else:
    print("module is imported")     # open regular.py 

"""

"""
for i in range(10):
    try:
        if 10 / i == 2.0:
            break
    except ZeroDivisionError:
        print(1)

    else:
        print(2)
"""




























































