"""
class Ram :
    def __init__(hello,name,age,occupation):
        hello.name=name
        hello.age=age
        hello.occupation=occupation
    def hello_world(hello):
        print("my name is "+ hello.name)
        print("my age is "+ hello.age)
        print("my occupation is "+ hello.occupation)

r1=Ram("alex","24","computer engineer")

r1.hello_world()
"""
"""
class dog:
    def __init__(self,legs,color,gender):
        self.legs=legs
        self.color=color
        self.gender=gender

main=dog("4","white and black","male")

print(main.color)
"""
"""
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark():
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
Dog.bark()
"""
"""
class Dog:

    def __init__(self,color="red"):

        self.color = color

fido=Dog()
print(fido.color)
"""
"""
class student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def good(self):
        print("hello")
class male(student):
    def good(self): #(this line is printed because first it print hello and then again function is called and got replaced by this second function)
        print("this student name is "+self.name+" and his age is "+self.age)

class female(student):
    def bad(self):
        print("this student name is "+self.name+" and her age is "+self.age)

main1=male("ram","20","male")
main2=female("sita","20","female")

main1.good()
main2.bad()
"""
"""
class a:
    def method(self):
        print(1)
class b(a):
    def method(self):
        print(2)

b().method()         #or simply we can do b().method
                     #first 1 got printed and got replaced by 2

"""
"""
class father:
    def good_father(self):
        print("mine father is good at everything")
class son(father):
    def good_son(self):
        print("son is the best friend of father")
class daughter(son):
    def good_daughter(self):
        print("daughter is like princess for father")
class mother(daughter):
    def good_mother(self):
        print("mother is like goddess who take cares of every family member")
a=mother()
a.good_daughter()
a.good_father()
"""
"""
class a:
    def spam(self):
        print("hello")
class b(a):
    def spam(self):
        print("hi")
        super().spam()
class c(b):
    def spam(self):
        print("aeyy")
        super().spam()
c().spam()
"""

"""
magic module
+, __add__(self, other), Addition;
*, __mul__(self, other), Multiplication;
-, __sub__(self, other), Subtraction;
%, __mod__(self, other), Remainder;
/, __truediv__(self, other), Division;
<, __lt__(self, other), Less than;
<=, __le__(self, other), Less than or equal to;
==, __eq__(self, other), Equal to;
!=, __ne__(self, other), Not equal to;
>, __gt__(self, other), Greater than;
>=, __ge__(self, other), Greater than or equal to;
[index], __getitem__(self, index), Index operator;
in, __contains__(self, value), Check membership;
len, __len__(self), The number of elements;
str, __str__(self), The string representation
"""
"""
class vector2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __sub__(self,other):
        return vector2d(self.x-other.x,self.y-other.y)

r1=vector2d(5,3)
r2=vector2d(2,1)
sub=r1-r2
print(sub.x)
print(sub.y)
"""
"""
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __or__(self, other):
    line =" collapse with "
    return "-".join([self.cont, line, other.cont])  

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam|hello)

#note
#we can use any function instead of "add" such as
#pow,trudiv,or
#(** for pow)
#(/ for trudiv)
#(| for or)
"""
"""
class vegetables:
    def __init__(self,name):
        self.name=name

    def __truediv__(self,other):
        return ([self.name, other.name])

r1=vegetables("red")
r2=vegetables("potato")

print(r1/r2)
print(r2/r1)
"""

"""
# only 1 magic method implemented
class A:
    def __or__(self, other): 
        return ("A or")

# several magic methods
class B:
    def __xor__(self, other):
        return ("B or")
    def __rxor__(self, other):
        return ("B ror")
    def __xor__(self, other):
        return ("B xor")
    def __rxor__(self, other):
        return ("B rxor")

# compare classes directly
print(str(A() ^ B())) # B rxor - xor is not implemented for A
print(str(B() ^ A())) # B xor

"""
"""
class Movies:
    def __init__(self,name,budget,ratings):
        self.name=name
        self.budget=budget
        self.ratings=ratings

    def __repr__(self):
        word="the name of movie is"
        return word +" "+(self.name)

op=Movies("3idiots","50cr","85")
print(op)
"""
"""
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

"""

"""
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for i in range(2):
      result1 = self.cont[:4] + ">=" + other.cont[:3]
      print(result1)

spam = SpecialString("10,9,8,7")
eggs = SpecialString("5,4,3,2")
spam > eggs
"""

"""
import random
from random import randint
for i in range(3):
    value=random.randint(-1,1)
    print(value)

"""

"""
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

"""

"""
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(vague_list[2])
"""

"""
celsius=float(input("enter the number "))
fahrenheit=celsius*9/5+32
print("the temperture in fahrenheit is:",fahrenheit,"and"+" the temperature in celsius is: ",celsius)
"""
"""
import sys

class Dog:
    def __init__(self):
        print('Dog created!')

charlie = Dog()
sys.getrefcount(charlie) # Start with 2 references
# Two references of this object maybe one is for reference in memory or in the Python main stack.

#bella = charlie
#sys.getrefcount(charlie) # Increased to 3 references
#sys.getrefcount(bella) # 3 references same as Charlie
char=charlie
#del charlie # Or delete bella it's the same
#sys.getrefcount(bella) # Decrease to 2 references

#del bella # This references is lost and the garbage collector destroy the variable in the memory address
"""
"""
class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents)

  def push(self, value):
    self._hiddenlist.insert(0, value)

  def pop(self):
    return self._hiddenlist.pop(1) #pop method returns remove value

  def __repr__(self):
    return "Queue{}".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue.pop()) #it prints 2 because it prints removed value
print(queue)       #now 2 is removed so only left item is printed
a=queue._hiddenlist #which means it only print list contents
print(a)

"""
"""

class animal:
    __elephant=5
    def mr_elephant(self):
        print(self.__elephant)
a=animal()
a.mr_elephant()
print(a._animal__elephant)  #to access from outside of class
                            #a._(class name)__(private method ) is used

print(a.__elephant )        #it doesnot print and says error because 
                            #it directly call the class and __elephant is private
                            #class so to print we should use(a._animal(class name)__elephant(private methods))

"""

"""
class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculation(self):
        return self.width*self.height
    def string_format(self):
        return self.width+"\n"+self.height

    @classmethod
    def math_cal(cls,total_length):
        return cls(total_length,6)
    @classmethod
    def math2_call_string(cls,min_string):
        return cls(min_string,"holland")



math1=rectangle.math_cal(5)     #pass argument 5 into class method then return some argument(5,6) then passed to actual class "rectangle" 
print(math1.calculation())
math2=rectangle(4,5)
print(math2.calculation())
math3=rectangle.math2_call_string("tom")
print(math3.string_format())

"""

"""
class animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def init_animal(self):
        return "animal name is "+self.name+" "+"and color is "+self.color

    @staticmethod   # only for returning output doesn't take any variable for just printing value inside class
    def wild_animals(string):
        if string=="elephant":
            raise ValueError("this animal is good")
        else:
            return "true animals"

Animal=animal("elephant","grey")
print(Animal.init_animal())

print(Animal.wild_animals("true"))
"""
"""
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self.examples= "word"
    @property
    def pineapple_allowed(self):   #property decorator is used just to perform simple calculation
        return self.toppings

    @property
    def slice(self):
        return self.examples.join(self.toppings)

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
print(pizza.slice)
"""
"""
string="this@that-is@thebest-deal"
a=string.split("@")[2]      #output=the-best-deal i.e only split the @ part ["this","that-is","the-best-deal"]
b=string.split("-")[2]
print(a)
print(b)                    #output=deal

"""
"""
class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def zoo(self):
        return f"{self.name}  {self.color}"

    @property
    def resource(self):
        return f"{self.name} {self.color}"

    @resource.setter
    def resource(self,string):      # we called setter to replace or change  {self.name} and {self.color}
        name=string.split(".")[0]
        color="light_grey"
        self.name=name
        self.color=color


a=Animal("lion","grey")
print(a.zoo())
print(a.resource)

a.name="elephant"
print(a.zoo())

a.resource="rhino"              #this attribute call setter

print(a.resource)

"""
"""
def get_input():
    command=input(": ").split(" ")      #say hello and split becomes ['say','hello']
    verb_word=command[0]                # this prints which is at command -->0 ie 'say'

    if verb_word in verb_dict:
        verb=verb_dict[verb_word]
    else:
        print("unknown verb {}".format(verb_word))
        return

    if len(command)>=2:
        noun=command[1]
        print(verb(noun))
    else:
        print(verb("nothing"))
#say is defined here because we haven't put {""-->this symbol in line 467}
def say(noun):
    return "you said '{}'".format(noun)

verb_dict = {"say":say}

while True:
    get_input()
"""
"""
class GameObject:
    class_name = ""
    desc = ""
    objects = {}
 
    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self
 
    def get_desc(self):
        return self.class_name + "\n" + self.desc
 
 
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)
 
    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line
 
    @desc.setter
    def desc(self, value):
        self._desc = value
 
 
goblin = Goblin("Gobbly")
 
 
def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health -= 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg
 
 
def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)
 
 
def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return
 
    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))
 
 
def say(noun):
    return 'You said "{}"'.format(noun)
 
 
verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit
}
 
while True:
    get_input()

"""
















































































































































































































































































