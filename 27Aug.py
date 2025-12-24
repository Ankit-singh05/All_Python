""
"""
Doubts:

Functions in Python: 

There is no negative marking in our class.

Functions: Block of code, which is generally designed
to perform some specific tasks.

Why we create functions:
1. To make code reusable. 
2. Functions are responsible to make the code
readable. To reduce the code complexity. To make
the project scalable.
3. Functions are the basic building blocks of modular
approach of programming.
4. Functions are the basic building blocks of 
multi threading.
5. Functions are the basic building blocks of 
layered architecture.
 
Scalable: To easily make the changes in the program
and able to make the bigger projects or scale
the project. 

Popular Layers of Programming: 2 very popular layers.
1. Presentation Layer: Responsible for user interaction.
input and print function will be the part of PL.

2. Business Logic Layer: The functionality of the
project will be implemented in BLL. This functionality
of the project is called business logic of the project.

3. Data Access Layer: To interact with the database

Kasam No 3: Any program you will make, divide the
program in min 2 layers.




1 Lakh Line of Code: 1000 times database access.  

MySQL Database: 
Oracle: 

Python supports modular approach of programming: 
Divide your program into modules and then interface
all these modules.

ERP: Enterprise Resource Planning: When you divide 
your company/organization working into different
departments and make the software for these departments
and interface all these software then software is called
ERP: 
CRM: Customer Relationship Management
IMS: Inventory Management System
HRMS: Human Resource Management System
FICO: Finance Controlling

.
.


 

IT Companies are categorised into 2 parts:
Product Based: Amazon, Linkedin, Microsoft, Google, Paytm
Services Based: TCS, HCL, Infosys, Capegemini....





Answers from students:
Block of code
pre defined elements
piece of particular code
Not to write too much code: Ankit Singh

How to call a function: Syntax
function_name(comma separated arguments)

How to create your own functions:
def function_name(arguments):
    Indented set of statements: suite
    return optional

The functions which do not return anything they
return None in the program.
C Lang: To separate blocks of code: Curly braces
Python: To separate blocks of code: Indentation

suite: One block of code in python is called a suite.

Indentation: All the statements in a block will
be at same space wrto heading.

Heading: Is a statement in python which is having
some sub statements inside it ie having one suite
inside it.

"""
# #New Program
# x=print("CETPA")
# print(x)

# #New Program
# print("PQRS")
# def func1():        #Heading
#   print("CETPA")  #suite line no1
#   print("Welcome")#suite line no2
#   print("ABC")    #suite line no3
#
# print("ABCD")
# print(func1)
# print(type(func1))

"""
Factorial of 5: 5*4*3*2*1=120: fact(n)
fact(5)

"""


#New Program:
def func1():        #Heading
  print("CETPA")  #suite line no1
  print("Welcome")#suite line no2
  print("ABC")    #suite line no3
#
# func1()     #Function calling
# func1()

# #New Program
# import math
# r=math.log(100,10)
# print(r)

# #New Program
# import operator
# u,v=5,7
# r=operator.add(u,v)
# print(r)

# #New Program
# def add(a,b):   #Line No 1
#     r=a+b
#     return r
# r=add(5,7)
# print(r)

# #New Program
# r=add(5,7)      #Error
# print(r)
# def add(a,b):   #Line No 1
#     r=a+b
#     return r

# #New Program
# def add(a,b):   #Line No 1
#     r=a+b
#     return r
# r=add(5,7)
# print(r)
# r=add(10,20)
# print(r)


#New Program:
"""
WAP for addition of 2 numbers in CETPA's student
style, not a Tom Dick and Harry's institute student.
"""
# #Business Logic Layer
# def add(a,b):           #Line 1, Line 5
#   r=a+b                 #Line 6
#   return r              #Line 7
# #Presentation Layer
# no1=int(input("Enter First No:")) #Line 2
# no2=int(input("Enter Second No:"))  #Line 3
# res=add(no1,no2)                  #Line 4, Line 8
# print("Result:",res)              #Line 10

# #New Program
# def func1():
#   print("CETPA")
#
# print("HELLO")


"""
Coding Standards

Oath No1: Kasam No 1: Always use comments in the program
Oath No2: Kasam No 2: Use logical names for identifiers
Oath No2: Kasam No 3: Try to divide your program in
                      min 2 layers: PL and BLL

Identifiers: User defined words like variable name,
function name, class name....
Keywords: Predefined words: in, if, def, for.....

"""
# #New Program
# def func1():
#   pass
#
# print(func1)
# del func1
# print(func1)

# #New Program
# x=5
# print(x)
# del x
# print(x)

"""
How to delete an object in Python
del object_name
"""
# #New Program
# x="CETPA"   #x address 1000
# print(x)
# x=7         #x address 2000
# print(x)
# del x   #Garbage Collector
#

# #New Program
# x=5   #x address 1000: Garbage collector
# x=7   #x address 2000
# print(x)

"""
Doubts till now?

RAM occupy: Run time
"""
# #New Program
# def func1():
#   print("CETPA")
#   return
#
# r=func1()
# print(r)

"""
function define:
def func1(arguments): arguments: formal parameters

function call:
function_name(arguments): actual parameters

the names of formal and actual parameters can be
kept as same or different. 
"""
# #New Program
# def func1(a,b,c,d):
#   r1=a+b
#   r2=c-d
#   r3=r1*r2
#   return r3
# u,v,w,x=1,2,3,4
# res=func1(u,v,w,x)
# print(res)

# #New Program
# import Module1    #Current Directory: Current Project
# r1=Module1.add(10,20)
# r2=Module1.sub(5,9)
# print(r1,r2)

"""
Function topic is started.

"""
# def func1():
#   pass
#
# del func1   #function will be deleted

"""


"""


