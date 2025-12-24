""
"""
Doubts Please:

Till now we have discussed required argument
functions.

== operator compares values
"""
# #New Program
# def add(a,b,c):
#     return a+b+c
#
# r=add(5,7)
# print(r)
#

"""
Identity Operator
is
is not
"""
# #New Program
# def add(a,b):   #add address 2000
#     return a+b
# x=add       #x address 2000
# r=x(5,7)
# print(r)



# #New Program
# a=5     #assume a address 500
# b=a     #b address 500 why: Because all variables in python are of ref type
# print(a==b) #Values are compared
# print(a is b)   #addresses are compared

"""
Data types: Core data types
Non Iterator/Single element:
int
float
complex
bool
NoneType

Iterator/Multi element:
str
list
tuple
dict
set
frozenset

class: is a data type
object: instance of a class

str: Collection of homogeneous data types ie characters
list: Collection of heterogeneous data types
tuple: : Collection of heterogeneous data types

str: Single, double or triple quotes
list: [comma separated elements]
tuple: (comma separated elements)

Indexing: Accessing a single element of an
iterator, if that iterator supports indexing.

If there are n elements in iterator
+ve indices: 0 to n-1 (Left to Right)
-ve indices: -1 to -n (Right to Left)

Syntax for indexing
var[index]

Interviews: In real life, generally numbers
starts with 1 but in programming, we starts
it with 0, why? Try to find out the answer
"""
# #New Program
# s="CETPA"   #0 to 4
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

"""
-ve indexing: -1 to -n: Right to Left Move
"""
# #New Program
# s="CETPA"   #-1 to -5
# print(s[-1])
# print(s[-2])
# print(s[-5])

# #New Program
# L=[10,20,99.5,True,"CETPA",[2,3]]
# print(L,type(L))

"""
Slicing: To access more than one element
"""

# #New Program
# L=[10,20,30,40,50]
# print(L[0])
# print(L[-1])

# #New Program
# t=(10,20,30)
# print(t[0],t[-2])

"""
Mutable Data Types: Which can be modified

Immutable: Which can't be modified

str: mutable or immutable.

There is no negative marking in our session
"""
# s="Cetpa"
# print(s,type(s))
# s="Hello"
# print(s,type(s))

"""
Variable: Whose value vary in the program

Mutable: list, dict and set are mutable data type
Immutable: Rest all: int, float, complex,
bool, NoneType, str, tuple, frozenset 

Mutable: We can change the data at the same
address. We can modify the elements
Immutable: We can't change the data at the same
address. We can't modify the elements

"""
# #New Program
# x="CETPA"    #x variable
# print(x)
# x=5
# print(x)
# x=[1,2,3]
# print(x)
# x=(1,2,3)
# print(x)

# #New Program
# x=5             #x address 1000
# print(id(x))
# x=7             #x address 2000
# print(id(x))

"""
Dynamic Memory Allocation: Every time
we assign a new value to a variable
using assignment operator then it will be
stored at a new address for all data types.
"""
# #New Program
# x=[1,2,3]
# print(id(x))
# x=[7,8,9]
# print(id(x))

"""
Mutable type data types: If we increase, decrease
or modify the elements, the base address of
data type don't change which represent about
mutable nature of data type.
"""

# #New Program
# L=[10,20,30]
# print(id(L))
# L[0]=90
# print(L)
# print(id(L))

"""
str, tuple, frozenset, if we try to modify
elements then we will get error.
"""

# #New Program
# s="CETPA"
# print(id(s))
# s[0]="M"    #Error
# print(s)
# print(id(s))

# #New Program
# s="CETPA"
# print(s,id(s))
# s="METPA"
# print(s,id(s))

# #New Program
# s="CETPA"
# print(s,id(s))
# s="M"+s[1:]
# print(s,id(s))

"""
Mutable: We can modify at same base address
Immutable: We can't modify at same address
"""

"""
x=[1,2,3] print(x,id(x)) 
y=[1,2,3] print(y,id(y)) 
sir isme address same kyu ni aara h

There is no negative marking: 
Object type question hai
Same or Different.

"""
# #New Program
# x="CETPA"       #x address 1000
# print(x,id(x))
# y="CETPA"       #y address 1000
# print(y,id(y))
# x="Hello"       #x address 2000
# print(y,id(y))
# print(x,id(x))

"""Devesh and Suraj"""
# #New Program
# L1=[1,2,3]      #Devesh, 1000
# print(L1,id(L1))
# L2=[1,2,3]      #Suraj, 2000
# print(L2,id(L2))

# #New Program
# L1=[1,2,3]  #L1 address 1000
# L2=L1       #L2 address 1000, reference
# L1[0]=10    #L1 address 1000, mutable
# print(L2)

# #New Program
# x=1000
# y=1000
# print(id(x),id(y))  #Indirect memory address

"""
str, tuple: immutable
list: mutable
"""
# #New Program
# t=(10,20,30)
# t[0]=90     #Error, immutable
# print(t)

# #New Program
# l=[10,20,30]
# l[0]=90
# print(l)

# #New Program
# L1=[10,20,30]
# L2=L1       #L2, L1 addresses 1000
# L1[0]=90    #L1 address 1000
# print(L2)

# #New Program
# L1=[10,20,30]   #L1 address 1000
# L2=L1.copy()    #L2 address 2000
# print(id(L1),id(L2))
# L1[0]=90
# print(L1)
# print(L2)

"""
Any doubts till now?

Functions: 
How to call a function:
Functions which are defined outside class.
function_name(arguments)

vs

Methods: Functions which are defined inside
class are generally called methods.
obj_name.method_name(arguments)

"""
# #New Program
# s="Cetpa"   #str
# r=s.upper()
# print(r)

# #New Program
# L=["a","b","c"]
# r=L.upper() #Error
# print(r)

"""
class: Collection of attributes
ie collection of variables and functions (methods)
"""
# #New Program
# L1=[10,20,30]   #L1 address 1000
# L2=L1.copy()    #L2 address 2000
# print(id(L1),id(L2))

# #New Program
# L=["ABC",20,30]
# print(id(L))
# L[0]="PQR"
# print(id(L))

# #New Program
# L=["ABC",20,30]
# print(L[0][1])
# print(type(L[0]))
# L[0][1]="M"     #Error

"""
List Methods:

list: mutable: If we call a method on list and
try to modify the list, then original list is 
modified
str: immutable: If we call a method on str and
try to modify the str, then original str is 
not modified and a new str is returned in the 
program
"""
# #New Program
# L1=[10,20,30]
# L2=L1.append(70)
# print(L2)
# print(L1)
# s1="Cetpa"
# s2=s1.upper()
# print(s1)
# print(s2)

# #New Program
# s="Cetpa"
# print(s.upper())
# L=[10,20,30]
# print(L.append(90))
# print(L)

# #New Program
# s="Cetpa"
# print(len(s))   #print(5)

# #New Program
# s="Cetpa"
# print(s.upper())   #print("CETPA")

# #New Program
# L=[10,20,30]
# print(L.append(90)) #print(None)
# print(L)

# #New Program
# s="Cetpa"
# r=s.upper()
# print(r,s)
# L=[10,20,30]
# x=L.append(90)
# print(x,L)

# #New Program
# L=[10,20,30]
# print(id(L))
# L.append(90)
# print(id(L))

# #New Program
# L=[10,20,30]
# L.extend([40,50])
# print(L)

# #New Program
# L=[10,20,30]
# L.append([40,50])
# print(L)
# L=[10,20,30]
# L.extend([40,50])
# print(L)

# #New Program
# L=[10,20,30]
# L.append("CETPA")
# print(L)
# L=[10,20,30]
# L.extend("CETPA")
# print(L)


# #New Program
# L=[10,20,30]
# L.append(25)    #argument passed can be non iterator or iterator
# print(L)
# L=[10,20,30]
# L.extend(25)    #argument passed must be an iterator
# print(L)

# #New Program
# L=[10,20,30]
# L.insert(1,90)
# print(L)

# #New Program
# L=[10,20,30]
# r=L.pop()   #Delete last element by default
# print(r)
# print(L)

# #New Program
# L=[10,20,30]
# r=L.pop(1)  #1 index element will be deleted
# print(r)
# print(L)

# #New Program
# L=[10,20,30]
# r=L.remove(20)
# print(r)
# print(L)

# #New Program
# L=[10,20,30]
# r=L.pop(1)
# print(L)
# print(r)

# #New Program
# L=[10,20,30]
# r=L.pop()
# print(L)
# print(r)

# #New Program
# L=[10,20,30]    #indices 0 to 2
# r=L.pop(20)     #Error
# print(L)
# print(r)

# #New Program
# L=[10,20,30]
# L.clear()
# print(L)

"""
M. D. Akil
Application of these methods:
CMS: 
id_list=[10,20,30]
name_list=["Vikas","Anil","Amit"]
age..
mob.

Program/Computer: Take the data from
user, process the data and generate the
otuputs.
Vikas
vikas
VIKAS 
"""
# s="CEtpa INFotech"
# r=s.lower()
# print(r)

# #New Program: To remove exact element
# L=[100,200,300,400,500]
# L.remove(300)
# print(L)

"""
CMS

kwargs
"""



