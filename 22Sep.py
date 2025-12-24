""
"""
Doubts: 

Topic of the day: 
"""
# #New Program
# def func1(*args):
#     print(args)
# func1(2,4,6,8)
# func1(2,4)
# func1(1,2,3,4,5,6,7,8,9)


# #Variable Length Keyword Argument Functions
# def func1(**kwargs):
#     print(kwargs)
# func1(a=2,b=3,c=4)
# func1(u=5)

"""
Topic: File Handling: To store the data permanently or
to access data stored from files. 
"""
# #New Program
# s="CETPA"
# r=len(s)
# print(r)
# print(type(r))

"""
To create variables: 
1. By assigning the value
2. class_name(arguments)
If we are not passing arguments then default variable
is created
int default value=0
float default value=0.0
string default value=""

x=str(25)

To create object of a predefined or user defined class
class_name(arguments)

"""
# #New Program
# s="CETPA"
# print(s,type(s))

# #New Program
# x=int()
# print(x,type(x))

# #New Program
# class MyClass:
#     pass
#
# a=MyClass() #a object of MyClass
# print(type(a))
# b=int()     #int class
# print(type(b))

# #New Program
# class MyClass:
#     pass
#
# def func1():
#     ob=MyClass()
#     return ob
#
# x=func1()
# print(type(x))

"""
To use file handling, firstly we create an object
of TextIOWrapper Class, generally in normal practice
we call this object as file type object.

Syntax:
open(file path,mode)
"""
# #New Program
# f=open("D://temp/file1.txt","w")
# print(type(f))
# f.write("Welcome to CETPA") #write is a method, made in TextIOWrapper class
# f.close()

# #New Program
# print("C\t\t\tETPA")
# print(r"C\t\t\tETPA")   #Raw String

# #New Program
# f=open(r"D:\Temp\file1.txt","r")
# data=f.read()
# print(data)
# f.close()


"""


"""
# #New Program
# f=open("file1.txt","w")
# f.write("Welcome to CETPA") #write is a method, made in TextIOWrapper class
# f.close()

# #New Program
# f=open("file1.txt","r")
# s=f.read()
# print(s)
# f.close()

"""
Suraj:
Chetan
Kripanshu


File Handling Modes: Data Access modes

String/Text Data
'w':    Write Mode: If file doesn't exist then file 
        will be created. If file exists then firstly
        data will be truncated and data will be written
        from starting of file.
'r':    Read Mode: If file doesn't exist then there will
        be error in the program. If file exists then data
        will be read from starting of file 
'a':    Append Mode: If file doesn't exist then a new
        file will be created and data will be written
        in starting of file. If file exist then existing
        data will be kept as it is and new data will be
        written at the end of file.
'w+':   Write and Read: Both write and read options are available. If file
        doesn't exist then new file will be created.
'r+':   Read and Write:  Both write and read options are available. If file
            doesn't exist then error.
'a+':   Append and Write

Binary Data/Byte Data:Binary Modes
wb:
rb:
ab:
wb+:
rb+:
ab+:
"""
# f=open("D://temp/cetpa video1.mp4","w")
# f=open("D://temp/ubi.pdf","w")

# #New Program
# f=open("D://temp/file1.txt","w")
# f.write("ABC")
# f.write("CDE")
# f.write("\t\t\tPQR")
# f.write("\nCETPA")
# f.close()

# #New Program
# f=open("D://temp/file1.txt","r")
# data=f.read()
# print(data)
# f.close()

# #New Program
# data=b"Cetpa"
# print(data)
# print(type(data))

# #New Program
# f=open("D:/temp/file2.txt","wb")
# f.write(b"Welcome to CETPA")
# f.close()

"""
Tarun and Suryansh
"""

# #New Program
# f1=open("D://temp/cetpa video.mp4","rb")
# f2=open("D://temp/cetpa video2.mp4","wb")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

# #New Program
# f=open("D://temp/file1.txt","r")
# s1=f.read(3)
# print(s1)
# s2=f.read(5)
# print(s2)
# f.close()

"""
Abstraction: You hide the unwanted info from the user.
"""


# #New Program
# f=open("D:/temp/file1.txt","a")
# f.write("Welcome to CETPA")
# f.write("\nABCDEFGHIJ")
# f.close()

# #New Program
# """0101"""

# #New Program
# f=open("D://temp/file4.txt","r")
# data=f.read()
# print(data)
# print("cetpa" in data)


# #New Program
# f=open("D://temp/file4.txt","r")
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# f.close()

"""
Iliyas
Devesh

To update the data.
"""
# #New Program
# f=open("D:/temp/file1.txt","r")
# data=f.read(3)
# print(data)
# print(f.tell())
# data=f.read(3)
# print(data)
# print(f.tell())
# f.close()

"""
seek() method: To intentionally takes the cursor
at some particular index position. This method
only works on byte mode.

seek(offset,whence)
whence:
0: Starting of file
1: Current Cursor position
2: End of file

offset: no of characters/bytes in file

"""
# #New Program
# f=open("D:/temp/file5.txt","rb")
# data=f.read(5)
# print(data,f.tell())
# f.seek(2,0)
# print(f.tell())
# data=f.read(3)
# print(data,f.tell())
# f.close()


# #New Program
# f=open("D:/temp/file5.txt","rb")
# data=f.read(5)
# print(data,f.tell())
# f.seek(-2,1)
# print(f.tell())
# data=f.read(3)
# print(data,f.tell())
# f.close()

# #New Program
# f=open("D:/temp/file5.txt","rb")
# data=f.read(5)
# print(data,f.tell())
# f.seek(-5,2)
# print(f.tell())
# data=f.read(3)
# print(data,f.tell())
# f.close()

"""
This is core file handling. We generally use it for
small amount of data storage.

I don't feel if there is any concept which is not
understandable. 
"""
"""
Tomorrow we will discuss about advanced file handling.

9212468020

"""



















