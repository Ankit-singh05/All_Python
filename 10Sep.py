"""
Doubts Please:

Lower to Upper Case
"""
# # #New Program
# x=input("Enter Any Number:")    #123
# v=0
# for i in x:
#     v+=int(i)
#     print(v)

"""
Lower to Upper Case

Abc*123 : ABC*123

A:  65      a:  97
B:  66      b:  98

Z:  90      z:  122

"""
# #BLL
# def myUpper(s):     #"Abc*123"
#     r=""
#     for e in s:     #e="A", e="b"
#         ele=ord(e)  #ele=65, 98
#         if(ele>=97 and ele<=122):
#             ele=ele-32  #ele-=32, ele=66
#         ch=chr(ele)    #ch="A", ch="B"
#         r=r+ch          #r="A"+"B"="AB"+"C"="ABC"+"*"
#     return r
# #PL
# s=input("Enter Any String:")
# res=myUpper(s)
# print("String in uppper case:",res)

# #New Program
# print(ord("0"))
# print(chr(48))
# print(chr(65))

# #New Program
# s1="ABC"
# s2="DEF"
# s3=""
# for i in range(len(s1)):    #i=0,1,2
#     s3=s3+s1[i]+s2[i]   #s3="AD", "ADBE"
# print(s3)

# #New Program
# s="1234"        #"1234"

# #New Program
# print(ord("A"))
# print(chr(23))

# #New Program
# L1=[10,20,30]
# L2=[100,200,300]
# L3=[]
# for i in range(len(L1)):    #i=0,1,2
#     ele=L1[i]+L2[i]
#     L3.append(ele)
# print(L3)


# #New Program
# s="Abc*123"
# print(s.upper())

# #New Program
# s="Abc*123"     #Upper Case
# r=""
# for e in s:
#     if(e=="a"):
#         e="A"
#     elif(e=="b"):
#         e="B"
#     elif(e=="c"):
#         e="C"
#     elif(e=="d"):
#         e="D"
#     r=r+e
# print(r)

"""
3. Take X as int input from user, print the 10 elements of following series: X, X3
x, x**3, x**5, x**7.....

, X5
, 
X
7……

1,3,5,7.......
"""
# n=int(input("Enter Any Number:"))   #n=5
# a=1
# for i in range(10):
#     print(n**a)
#     a+=2

"""
Nested Loops

Pattern Printing
*
**
***
****
*****
Table:
n   i   j
5   0   1
5   1   2
5   2   3
5   3   4
5   4   5
j=i+1

"""
# #New Program
# n=int(input("Enter no of lines:"))  #5
# for i in range(n):  #i=0,1,2,3,4
#     for j in range(i+1):
#         print("*",end="")
#     print()


"""
*****
****
***
**
*
n   i   j
5   0   5
5   1   4
5   2   3
5   3   2
5   4   1
j=n-i
"""
# #New Program
# n=int(input("Enter no of lines:"))  #n=5
# for i in range(n):  #i=0
#     for j in range(n-i):
#         print("*",end="")
#     print()

"""
    *
   **
  ***
 ****
*****
n   i   j   k
5   0   4   1   
5   1   3   2
5   2   2   3
5   3   1   4
5   4   0   5
j=n-i-1
k=i+1

"""
# n=int(input("Enter No. of Lines:")) #n=5
# for i in range(n):  #i=0
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()


"""
*        *
**      **
***    ***
****  ****
**********


"""
# #New Program
# n=int(input("Enter no. of lines:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     for k in range(2*(n-i-1)):
#         print(" ",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()

"""
Practice:
a
bb
ccc
dddd
eeeee
"""

"""
Find the biggest number in a list using loop.

L=[1,35,32,67,45,78,11]
"""
# #New Program
# L=[1,35,32,67,45,78,11]
# res=0
# for e in L:     #e=1
#     if(e>res):
#         res=e
# print("The biggest number is:",res)
#

# #New Program: Wrong output
# L=[-1,-35,-32,-67,-45,-78,-11]
# res=0
# for e in L:     #e=1
#     if(e>res):
#         res=e
# print("The biggest number is:",res)

# #New Program
# L=[-78,-1,-35,-32,-67,-45,-78,-11]
# res=L[0]        #res=-78
# for i in range(1,len(L)): #i=1,2,3,4,5,6
#     if(res<L[i]):
#         res=L[i]    #res=35
# print("The biggest number is:",res)


# #New Program
# L=[-78.234,-1.89,-35,-32,-67.89,-45,-78,-11,0.5]
# res=L[0]        #res=-78
# for i in range(1,len(L)): #i=1,2,3,4,5,6
#     if(res<L[i]):
#         res=L[i]    #res=35
# print("The biggest number is:",res)

# #New Program
# L=[1,35,32,67,45,78,11]
# res=0
# for e in L:     #e=1
#     if(e>res):
#         res=e
# print("The biggest number is:",res)

"""
*
**
***
****
*****
"""
# n=int(input("Enter no. of lines:"))
# for i in range(n):  #i=0,1,2,3,4
#     print("*"*(i+1))
#

"""
*        *
**      **
***    ***
****  ****
**********
"""
# #New Program
# n=int(input("Enter no of lines:"))
# for i in range(n):
#     print("*"*(i+1)," "*2*(n-i-1),"*"*(i+1),sep="")


# #New Program
# print("*"*6)
# print("Ram"*108)

"""
Customer Management System: First Project

Please revise all concepts specially list
methods, before joining tomorrow's class
"""



