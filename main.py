"""
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)


num=int(input("enter a number"))
print("factorial using recursive function is" ,factorial(num))
"""
"""

def fibonacci(x):
    while x<=5:
        if x==0:
           return 0
        elif x==1:
           return 1
        elif x>=2:
            return 1
        else:
           return fibonacci(x-1)+fibonacci(x-2)

for i in range(1,10):
    print(i,fibonacci(i))
num=int(input("enter your number: "))
print(fibonacci(num)
"""

"""
def factorial(x):

    return not x

print(factorial(5))   #output is false

 """

"""

def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)

print(is_odd(3))

"""


"""

"is_odd(3)"
"ret not is_even(3)"
"ret not (is_odd (3-1))"
"ret not (is_odd(2))"
"ret not (ret not is_even(2))"
"ret not (ret not (is_odd(2-1)))"
"ret not (ret not (is_odd(1)))"
"ret not(ret not (ret not is_even(1)))"
"ret not(ret not (ret not (is_odd(1-1))))"
"ret not(ret not (ret not (is_odd(0))))"
"ret not(ret not (ret not (ret not is_even(0))))"
"ret not(ret not (ret not(true))"
"ret not(ret not(false))"
"ret not(true) "
"false"

"""
"""
def hello_world(x):
    if x==0:
        return "hello "
    else:
        return hello_universe(x-1)

def hello_universe(x):
    return  hello_world(x)

print(hello_universe(4))

"""
"""
def choco(x):
    for i in range(2,10):
        if x==i:
            return True
        else:
            return pie(x-1)
def pie(x):
    return choco(x)

print(pie(3))

"""
"""
from itertools import cycle,repeat

mylist=[1,2,3,4,5]
for i in cycle(mylist):
    print(list(repeat(mylist,5)))
    if i>=4:
        break
"""
"""
print((lambda x,y,z:x+y+z)(2,4,6))
"""
"""
from itertools import accumulate,takewhile
i=7
nums=list(accumulate(range(i)))
print(nums)
print(list(takewhile(lambda x:x<=10,nums)))

hello=[1,2,3,4,5,6,7,8]
print(list(filter(lambda x:x%2==0,hello)))
print(list(takewhile(lambda x:x%2==0,hello))) #first test condition whether the condition is true or not

"""
"""
from itertools import chain
nums1=[1,2,3,4,5,6]
nums2=[4,5,6,7,8,9,1]
print(list(chain(nums1,nums2)))

#print all nums in order

"""
"""
from itertools import product,permutations

letters=["ram","shyam"]
print(list(product(letters)))
print(list(product(letters,range(2))))

nums=[1,2,3]
print(list(permutations(nums)))
print(list(permutations(nums,2)))

"""
"""
nums={1,2,3,4,5,6}
nums={0,1,2,3} & nums
nums=filter(lambda  x:x>1,nums)
print(len(list(nums)))
"""









