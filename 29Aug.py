""
"""
Doubts Please

Functions Continue.
"""
# #New Program
# def func1(a,b,c):
#     r=a+b+c
#     return r
# s=func1(5,7,9)
# print(s)

"""
In every programming langauge, when we call a
function, actual parameters are assigned to
formal parameters.

All variables in Python are of reference type.
When we assign one variable to another variable
then address of RHS variable is assigned to LHS 
variable
"""
# #New Program
# a=5
# print(id(a))
# b=a
# print(a,b)
# print(id(a),id(b))



# #New Program
# def func1(a,b,c):
#     print(id(a))
#     r=a+b+c
#     return r
# u,v,w=5,7,9
# print(id(u))
# s=func1(u,v,w)  #a=u,b=v,c=w
# print(s)

"""
The variables defined inside functions are called
local variables. The variables defined outside
functions are called global variables.

Global variables can be accessed both inside
functions and outside functions. The scope of
global variables is available through out
the program and global variables are destroyed
the moment program is stopped.

Local variables can only be accessed inside
functions but not outside functions. The scope/life
of local variables exist only till the function
is executing, the moment function is complete,
local variables are destroyed ie the moment we
come out of functions local variables are
destroyed.

Everytime we call a function, everytime
new local variables are created.
"""
# #New Program
# def func1():
#     print(a)
#
# a=5

# #New Program
# def func1():
#     print(a)
#
# a=5             #Global variable
# func1()
# print(a)

# #New Program
# def func1():
#     a = 5  # Local variable
#     print(a)
# func1()
# print(a)        #Error


# #New Program
# def add(a,b): #a,b are local variabels
#     r=a+b     #r address 5000
#     print(id(r))
#     return r
# u,v,w,x=1,2,3,4 #u 1000, v 2000, w 3000 x 4000
# s1=add(u,v)     #a=u, b=v, a 1000, b 2000
# s2=add(w,x)     #a=w, b=x, a 3000 b 4000
# print(id(s1),id(s2))
# print(s1,s2)

# #New Program: Option 1
# def add():
#     r=a+b
#     return r
# a,b=5,7     #Global Variables
# s=add()
# print(s)

# #New Program: Option 2
# def add(a,b):
#     r=a+b
#     return r
# a,b=5,7     #Global Variables
# s=add(a,b)
# print(s)


# #New Program: Option 1
# def add():
#     r=a+b
#     return r
# a,b,c,d=5,7,9,11     #Global Variables
# s=add()
# print(s)

# #New Program: Option 2
# def add(a,b):   #1, 4, 9
#     r=a+b       #5, 10,
#     return r    #6, 11
# a,b,c,d=5,7,9,11     #Global Variables #2
# s1=add(a,b) #3, 7
# s2=add(c,d) #8, 12
# print(s1,s2) #13

"""
If we have variables with same name both 
inside functions and outside functions ie
we have local variables and global variables
with same name, then global variables will 
be accessed outside functions and local 
variables will be accessed inside functions
by default.

Means, Global variables can be accessed both inside
as well outside functions but can't be modified
inside functions, why? Because the moment, we
try to modify global variables inside function,
immediately new local variables are created
inside functions why because in Python every
time we assign a new value to a variable, new
variables are created.

If we don't want to create new local variables
inside functions and want to modify global 
variables only, then we need to use global
keyword with variable name.
"""
# #New Program
# def func1():
#     # a=5         #Local variable
#     print(a)
# a=7         #Global variable
# func1()
# print(a)

# #New Program
# def func1():
#     a=5         #Local variable
#     print(a)
# a=7         #Global variable
# func1()
# print(a)

# #New Program
# def func1():
#     global a
#     a=5         #global variable, a address 2000
#     print(a)
# a=7         #Global variable, a address 1000
# func1()
# print(a)

"""
In Python, every time we assign a new value
to a variable then it is stored at a new
address ie called dynamic memory allocation.
"""
# #New Program
# x=5
# print(id(x))
# x=7
# print(id(x))
#

"""
In functions by default variables are created
as local variables if we want to make global
variables inside functions then firstly we 
need to define the variables as global variables
using global keyword.
"""
# def func1():
#     a=5     #Local Variable
#     print(a)
#
# func1()
# print(a)

# #New Program
# def func1():
#     global a
#     a=5     #Global Variable
#     print(a)
# func1()
# print(a)

"""
Vikas Banti: One Identity, one soul, two names
Banti: Local
Vikas: Global
"""
# def func1(banti): #banti local variable
#     print(banti)
#     print(vikas)
#
# vikas=5     #global variable, address 1000
# func1(vikas)    #banti=vikas, banti address 1000
# print(vikas)

# #New Program
# def func1(x):   #x local variable
#     print(x)
#     print(a)
#
# a=5     #global variable, address 1000
# func1(a)    #x=a, x address 1000
# print(a)

# #New Program
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
#
# r1=add(5,7)
# r2=add(10,20)
# r3=sub(10,20)
# r4=mul(2,4)
# print(r1,r2,r3,r4)

# #New Program
# x=5     #object int class, address 1000
# x=7     #object int class, address 2000
# print(x)

# #New Program
# def func1(a,b): #func1 address 1000
#     return a+b
# def func1(a,b): #func1 address 2000
#     return a-b
# r=func1(5,7)
# print(r)
#

"""
All user defined functions are the object
of function class.
"""
# #New Program
# def func1(a,b): #func1 address 1000
#     x=a+b
#     return x
# def func1(a,b): #func1 address 2000
#     x=a-b
#     return x
# r=func1(5,7)
# print(r)

# #New Program
# def func1():
#     pass
# print(type(func1))
# print(func1)
# x=5
# print(x,type(x))
#


# #New Program
# s="CETPA"
# print(len(s))

# #New Program
# def add(a,b):
#     return a+b
#
# print(add(5,7))
# print(add)
# print(id(add))

"""
id means indirect representation of address
with a unique int number.

function object ko print karne pe address
aata hai. 

C Lang: Call by address

Call by value: C Lang
Call by address: C Lang
Call by reference: Python

1000: account no id
1002: account no pwd

reference:

x=5
5 is stored at 1000 address

x is referring 8000 address. At 8000
address 1000 is stored.

x=7
7 is stored at 2000 address

x is still referring 8000 address. At 8000
address now 2000 will be stored
"""
# #New Program
# def func1():
#     def func2():
#         print("CETPA")
#
# func2()     #Error: func2 is not defined because
                #func1 body is not executed ie
                #func1 is not called


# #New Program
# def func1():    #func1 address 1000
#     def func2():    #func2 address 2000: local object
#         print("CETPA")
# func1()
# func2()     #Error, func2 is local object of func1

# #New Program
# def func1():    #func1 address 1000
#     def func2():    #func2 address 2000: local object
#         print("CETPA")
#     func2()
# func1()


# #New Program
# def func1():    #func1 address 1000
#     global func2
#     def func2():    #func2 address 2000: local object
#         print("CETPA")
#
# func1()
# func2()

"""
Tomorrow class should be at same time:
10 AM onwards.


"""