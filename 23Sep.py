""
"""
Doubts:
"""
#New Program
# f=open("D://temp/file1.txt","w")
# obj=f.write("CETPA")    #obj=5
# print(obj)
# obj=f.write("Welcome")    #obj=7
# print(obj)
# f.close()

"""
Serialization: Conversion of Program data/objects
into some standard format. 
Standard format examples: JSON, Pickle, XML...
Why we convert standard formats: For data exchange.
Pickle format: used to exchange data between python
program to python program only
JSON: World's most popular data exchange format for data
exchange between one langauge to another language. 

Deserialization


Pickling in Python.

Pickling: Conversion of Python objects into binary format
pickling is sometimes called a partially encrypted data.

dump method: converts data into pickle format along
with save this pickle format data to file
"""
# #New Program
# import pickle
# f=open("D://temp/file6.txt","wb")
# data=[10,True,99.5,"CETPA"]
# pickle.dump(data,f)
# f.close()

# #New Program
# import pickle
# f=open("D://temp/file6.txt","rb")
# data=pickle.load(f)
# print(data)
# f.close()

# #New Program
# def func1():
#     global x
#     x=7     #global variable
#     print(x)
#
# x=5     #Global variable
# func1()
# print(x)


"""
Aaj ka lecture un baccho ko boring lag raha hoga, jinhone
file handline and cms kee practise nahi kee hai.

No Practice means No Learning.

Tomorrow m traveling to Bangalore, so there won't be
any class tomorrow. On Thursday morning we will have
the class at same time

Please again request kar raha hoo, Life me kuch karna hai
to ya to 3 baje sona shuru karo ya 3 baje jagna.

"""

# #New Program
# import pickle
# f=open("D://temp/file7.txt","wb")
# data={10:100,20:200,30:300}
# pickle.dump(data,f)
# f.close()

"""
Still if students are facing problems then please
start writing small programs.
"""

"""
There is nooooooo negative marking in our session.

Exception Handling: Handle exceptions in python is 
exception handling.
How to handle errors at the run time.

Professional software: In Live projects, if some error
is generated then generally the project doesn't stop, why
because of exception handling used in the program

Khalid
Arvaz
Shubham
"""
# #New Program
# id_list=[10,20,30]
# id=40
# i=id_list.index(40) #ValueError: 40 is not in list
# print(i)

"""
ValueError
IndexError
SyntaxError
IndentationError:
ModuleNotFoundError
TypeError
ZeroDivisionError
FileNotFoundError


Identifiers: 3 types: user defined words
variable name
function name
class name

Keywords: predefined words, 
ex: global, if, import, def, break,else,continue.....
 
Guidelines to make the code readable.
Kasam No1: Try to use maximum comments in the program
Kasam No2: Give logical names to identifiers

There are some guidelines for identifiers. 
Variable name: should be in complete small letters with
underscore as separator in between words
cus_id, cus_name
Function name: should be in camel case: 
first word complete small, and rest whereever there
is stress, should start with capital letter
addCustomer()
addNewCustomer()
savetoPickle()
Class Names: Should be in extended camel nomenclature or
also called Pascal Case.
ie all words should start with Capital Letter
Ex:
MyClass
Customer
NewEmployeeClass:

Wherever needed use underscore as separator.

Exception Handling: how to handle exceptions:
To handle exceptions in python, we are given a few keywords
try
except
finally
raise

Kasam No 3: Try to Divide your program in min 2 layers
ie PL and BLL

Kasam No n: Always use exception handling in your
program
"""
#
# if():
# "CETPA"     #Error

# #New Program
# print(type(IndexError))

"""
After 5 years of your course from CETPA,
you will work in a BPO or
a mechanical company
or E grade IT company
or D grade or C or B or A grade company
like MAAMA comapnies, all depends on how much efforts
you put in the class today.
After 5 years, you will have your annual salary in
6 figures: 999999
7 figures
or 8 figures
or 9 figures or more like 
all depends how much efforts you put in your class today.
"""

# #New Program
# try:
#     a=int(input("Enter First No:"))
#     b=int(input("Enter Second No:"))
#     r=a/b
#     print(r)
# except:
#     print("Some Error in the Program")

"""
In python, we have multiple predefined Error classes
like

IndexError
ZeroDivisionError
.
.
There is one class ie Exception class which is the parent
of all error classes.

"""



# #New Program
# try:
#     a=int(input("Enter First No:"))
#     b=int(input("Enter Second No:"))
#     r=a/b
#     print(r)
# except Exception:
#     print("Some Error in the Program")

# #New Program
# while(1):
#     try:
#         a=int(input("Enter First No:"))
#         b=int(input("Enter Second No:"))
#         r=a/b
#         print(r)
#         break
#     except Exception:
#         print("Some Error in the Program")

# #New Program
# int("a")


# #New Program
# while(1):
#     try:
#         a=int(input("Enter First No:"))
#         b=int(input("Enter Second No:"))
#         r=a/b
#         print(r)
#         break
#     except Exception as err:    #err will the object of relevent Error class
#         print("Error!",err)
#         print(type(err))


# #New Program
# try:
#     import cetpa
# except Exception as err:
#     print("Error!",err)
