"""
import re

pattern=r"hello123"

if re.match(pattern,"hello123"):   #it must print same pattern [hello123] 
#pattrn=hello123 so if we write (pattern,"123hello") it would print no match
#because sting start with hello123 and we wrote 123hello must have same pattern

    print("match")
else:
    print("mo match")
"""

"""
import re
while True:
    word=input(":")
    pattern=r"gl"
    if re.match(pattern,word):
        print("match")
    else:
        print("no match")

"""

"""
import re

pattern=r"letter"

if re.match(pattern,"cannotletterwordletter"): 
    #letter is matched with the strings lettersings
    print(True)
else:
    print(False)

if re.search(pattern,"helloletternoneletter"):
    #re.search function search for the  string anywhere
    #letter is searched or found so it prints true although it does not match pattern
    print(True)
else:
    print(False)

print(re.findall(pattern,"thereisnoletterintheletterstringfunction"))
#if "letter" is found in the string then it prints that string
#as there is 2 letter in string so re.findall prints ['letter','letter']
"""
"""
import re

word="spam1eggspam2eggspam3eggspam4egg"

pattern = r'eggspam'
myiter = re.finditer(pattern,word)
print(next(myiter).group())
print(next(myiter).group())
print(next(myiter).group())

#above prints the 'eggspam' serially 

"""
"""
import re

pattern=r"spam"

match=re.search(pattern,"eggsausagespam egg")
if match:
    print(match.group())
    #returns the matched string i.e spam is matched so spam will be printed
    print(match.start())
    #returns the start position i.e 10
    print(match.end())
    #returns the end position i.e 14
    print(match.span())
    #returns the both start and end position as a tuple i.e(10,14)
"""
"""
import re

word="Hello Mr.Alex. Nice to meet you Mr.Alex. Good Mr.Alex"

pattern=r"Mr.Alex"

word1=re.sub(pattern,"Mrs.Alexis",word,count=2)
#Mr.Alex will be replaced by Mr.Alexix
#if count=0 then Mr.Alexx be replaced with Mr.Alexis and will  be printed i.e-->
#if count=1 then only Mr.Alexis will be printed i.e-->Hello Mrs.Alexis. Nice to meet you Mr.Alex. Good Mr.Alex
#for count=2 then -->Hello Mrs.Alexis. Nice to meet you Mrs.Alexis. Good Mr.Alex
print(word1)
"""

"""
#Create a program that will take the phone number as input, and if the number starts with '00', replace them with '+'.

import re

while True:
    number=input(":")
    number1="00"+number
    print(number)
    print(number1)

    print("\n")
    choice=input(":")

    if choice in ("number1","number2"):
        if choice=="number1":
            pattern=r"00"
            word=re.sub(pattern,"+",number1)
            print(word)
        if choice=="number2":
            print(number)

"""


"""
choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        print("true")
"""
"""
import re

#pattern=r"gr[a-z]*y"
#pattern=r"gr.*y"
#pattern=r"gr..y"
pattern=r"...."





if re.match(pattern,"gray"):
    print("the string is matched")
if re.match(pattern,"grely"):
    print("the second string is also matched")
    #for this pattern gr..y(double dots is used because grely has must be matched with same length gr..y)
if re.match(pattern,"blue"):
    print("the third string is matched")
else:
    print("not matched")

"""

"""
import re

pattern=r"^sa...a$"
# ^ and $ means start and end position 
# i.e '^sa' means start with sa and 'a$' means end with a


if re.match(pattern,"sabina"):
    print("matched")
else:
    print("not matched")

pattern2=r"^sa.*a$"
if re.match(pattern2,"sakna"):
    print("matched2")
else:
    print("not matched")
"""
"""
import re

pattern=r"[ae][iou]"
#means any character i.e aeiou must contain in below string
if re.search(pattern,"paeuln"): 
    # i.e any three two letters out of ae and any three letters out of iou
    #becoz aeiou must be in order i.e paeuln where aeu are in order
    print("found")

else:
    print("not found")

if re.search(pattern,"rhym"):
    print("found")
else:
    print("not found 2")

pattern1=r"[a-z][A-Z][0-9]"
# first character must start with small, second one with capital and third one with number
if re.search(pattern1,"lA9"):
    print("found 001")
if re.search(pattern1,"Ln8"):
    print("found 002")
else:
    print("not found 3")
"""

"""
[]	A set of characters	"[a-m]"
\	Signals a special sequence (can also be used to escape special characters)	"\d"
.	Any character (except newline character)	"he..o"
^	Starts with	"^hello"
$	Ends with	"world$"
*	Zero or more occurrences	"aix*"
+	One or more occurrences	"aix+"
{}	Exactly the specified number of occurrences	"al{2}"
|	Either or	"falls|stays"
()	Capture and group

"""
"""
import re

pattern = r"[^A-Z]"    #if ^[A-Z] then only uppercase character
#metacharacter i.e [^A-Z] ie '^' is put inside to neglect uppercase character
# i.e atleast one lowercase or number must contain to print for e.g ABCde12 it prints
if re.search(pattern, "this will be printed"):
    print("Match 1")
#it does not contain uppercase so matched
if re.search(pattern, "AbCdEfG123"):
    print("Match 2")
# it contains some lowercase some uppercase or some number so matched
if re.search(pattern, "ADEFGHIJKLMNOPQRSTUVWXYZ"):
    print("Match 3")
# it does not matched because all are uppercase

"""
"""
#Write a program for a search tool that will take the ID as input and
# output 'Searching' if the format is correct, and 'Wrong format', if it's not.


import re,time

ID=input(r"Enter your ID : ")
print(ID)

pattern=r"[A-Z][0-5][6-9][a-z]"

if re.search(pattern,ID):
    print("searching")
    time.sleep(5) #for time delay for 5 sec and import time must be written
    print("the format is correct")
else:
    print("wrong format")

"""
"""
import re

pattern1=r"ds{2}"  # atleast 2 or more than 2 'ds' must contain
                   # minimum 2 or more than 2
if re.search(pattern1,"ddss2"):
    print("matched1")

else:
    print("not matched")


pattern2=r"ao{2,3}" # (min,max) i.e min 2 , max 3

if re.search(pattern2,"aoo"):
    print("mathced2")

pattern3=r"\w"   #i.e '\d' must contain decimal 0-9 '\w' must contain any character a-z

if re.search(pattern3,"asfdfdvfg"):
    print("matched3")
"""

"""
import re

pattern=r"spam(egg)*"
# '*' means word must start with spam(because I use re.matched) and then either zero or more egg contain 

if re.match(pattern,"eggspam"):
    print("matched1")

if re.match(pattern,"spamegg"):
    print("matched2")

if re.match(pattern,"spam"):
    print("matched3")


pattern2=r"[a^]*"    # means zero or more repetition of any character

if re.match(pattern2,"bgshfusdhfd12323s"):
    print("matched4")


pattern3=r"g+"    #means one or more 'g'   #put r"g+$"-->ends with g
# but must start with 'g' to print it for re.matched

if re.match(pattern3,"geeta"):
    print("matched5")

if re.search(pattern3,"Asus_rog"):
    print("matched6")

a=re.findall(pattern3,"nogisksdjkgoergaddbbgbnbg")
print(a)

pattern4=r"(42)+$"
# means '$' must end with 42 for one or more 42

if re.match(pattern4,"4242"):
    print("matched7")

pattern5=r"(no)?one"
# (no)? means zero or one repition of (no)
if re.match(pattern5,"one"):
    print("matched8")

pattern6=r"noone?"
# means zero or one repitition of 'e'
if re.match(pattern6,"noon"):
    print("matched9")
"""

"""
import re

pattern = r"9{1,3}$"    # {,2} zero or upto 2  {1,} 1 or upto infinite
#means min 1 or max 3 must contain and
#if we put $ then end with 9 with upto three or one 9 i.e 999
if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "999"):
    print("Match 3")
"""

"""
import re

#Create a program that takes password as input and returns 'Password created' if all requirements are met.

password=input("enter your password : ")

pattern=r"[A-B][a-z][0{1,3}]"

if re.match(pattern,password):
    print("Password created")
else:
    print("wrong password")
"""

"""
import re

pattern=r"spam(eggs)"
#groups are reprsesent in parenthesis'()' i.e (eggs) represent a group
if re.match(pattern,"spameggsspam"):
    print("matched")
else:
    print("not matched")

print("\n")

pattern1 = r"a(bc)(de)(f(g)h)i"

match=re.match(pattern1, "abcdefghijklmnop")
if match:

    print(match.group())    #it prints all the whole match
    print(match.group(0))   #           "
    print(match.group(1))   #it prints 1st group i.e bc
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(match.groups())   # groups prints all the matched gropus in tuple()
    print("\n")

pattern3=r"spam(eggs)$"

match=re.match(pattern3,"spameggs")
if match:
    print(match.group())
    print(match.group(1))

else:
    print("not matched")

print("\n")

pattern4 = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern4, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

"""

"""
import re

pattern=r"(?P<name>012)(?:345)(678)"

# (?:...) this is just used to skip the group for e.g if we
# write (?:..) then it will skip and print another group
# (?:..) is also called hidden groups

match=re.search(pattern,"012345678")
if match:
    print(match.group())
    print(len(match.group()))
    print(match.group(1))
    print(match.group(2))
    print(match.group("name"))  #it will print 012
    print(match.groups())

print("\n")

pattern1=r"gee(t|a|n|p) is (good|not good)"

# means either t or a i.e either geet or geea
# either good or not good

if re.match(pattern1,"geet is good "):
    print("matched")

if re.match(pattern1,"geea is not good"):
    print("matched2")

if re.match(pattern1,"geetanp is good"):
    print("matched3")

"""
"""
import re

pattern=r"(.+) \1"

# (.+) means any character and \1 means repeat of first character


if re.match(pattern,"word word"):
    print("matched")

if re.match(pattern,"word class"):
    print("matched2")


pattern1=r"(.+) (.+) \1 \2"

# (.+) (.+) means double charcter group so for double group 
# \1 \2 is written i.e \1 for one group (.+) and \2 for another--
# --group (.+)

if re.match(pattern1,"word true word true"):
    print("matched3")

"""
"""

import re

pattern=r"(\D+\d)"

# \D+ means any non-digits and \d means digit i.e[0-9]

if re.match(pattern,"hello123"):    # although if we put space in between hello and 123 it 
# will print matched because \D+ means one or more character 
# so space is also a form of character.
    print("matched")
else:
    print("not matched")

pattern2=r"(\s)"

# [ \t\n\r\f\v] are white spaces try: print("the\tworld")

if re.findall(pattern2,"theindian\nexpress"):
    print("matched2")



pattern3=r"(\W)"

# \W means not any word or any number i.e only [;,''.,/;;]

if re.match(pattern3,"./.'"):
    print("matched3")


#if re.match(r"(\d+ \W)","12344 %,."):
    #print("matched")

"""

"""
import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!$%^")
if match:
    print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
    print ("Match 3")

print("\n")


if re.match(r"\A(al)(ex)\Z","alex"):
# \A and \Z means begining of string "al" and end of string "ex"
    print("fully matched")


if re.search(r"\B(haha)\B","456hahaplease"): #\B means invertion of
    print("nice matched")


if re.match(r"\A(spam) (egg)\Z","spam egg"):
    print("so it is matched")

if re.search(r"[^0-9][(a-z)$]","0123b@123b nabv"):
    print("whole matched")

"""
"""
import re

pattern = r"([\w\.-]+)@([\w\.]+)(\.[\w\.]+)"

match=re.match(pattern,"info@sololearn.com")
if match:
    print("matched")

print(match.group(0))
print(match.group(1))

print("\n")

date="2017 \ 03 \ 20"

pattern1=r"([\d]+) \\ (\d+) \\ (\d+)"

if re.match(pattern1,date):
    print("the date is matched")



import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())
"""

"""
import re

Phone_Number=input("Enter your phone number : ")

pattern=r"(^[1,8,9])([0-9]{1,9})"

if len(Phone_Number)==10:
    if re.match(pattern,Phone_Number):
        print("Valid Number")
    else:
        print("Invalid Number")
else:
    print("Number should contain ten digits")

match=re.match(pattern,"9840313932")

print(match.group())
"""

# style guide for python
"""
my_list=[
    1,2,3,
    4,5,6
]

print(my_list)

"""

import pack



























































