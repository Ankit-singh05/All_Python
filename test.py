# def mylistfunc(l):
#     l.clear()
# l1=[1,2,3]
# r=l1
# print(l1)
# print(r)
# print(f"result:{res}")
# Id = input("inter user Id")
# Pass= input("inter user password")
#
# if (Id != "Bond" or Pass != "007"):
#     print("id and Password are not correct")
# else:
#     print("id and password are correct")
#
# no1=float(input("Enter the first number: "))
# no2=float(input("Enter the second number: "))
# ch=input("Enter the choice +,-,*,/: ")
#
# no1=int(input("Enter no1"))
# no2=int(input("Enter no2"))
# if no1>no2:
#     print("no1 is greater than no2")
# else:
#     print("no2 is greater than no1")
#
# no1=int(input("enter no1"))
# no2=int(input("enter no2"))
# no3=int(input("enter no3"))
# if no1>no2 and no1>no3:
#     print("no1 is greater")
# if no2>no1 and no2>no3:
#     print("no2 is greater")
# if no3>no1 and no3>no2:
#     print("no3 is greater")
#
# a = [[0]] * 5
# a[0][0]=1
# print(a)
#

# loop iteration : Any data type which can
# for i in range(10):
#     print(i)
# s="vikas"
# for i in range(len(s)):
#     print(s[i])

# char=input("enter any word to continue:")
# for i in range(0,len(char),2):
#     print(char[i])


# char=input("enter any word to continue:")
# for i in range(-1,-len(char)-1,-1):
#     print(char[i])
# r=0
# for i in range(3,31,3):
#     r=r+i
# print(r)

# s=list(map(int, input("Enter numbers separated by space: ").split()))
# r=0
# for i in range(0,len(s),2):
#     r=r+s[i]
# print(r)

# sum of any number when they are not in list
# n=input("enter any number : ")
# r=0
# for i in n :
#     r=r+int(i)
# print(r)

# Multiply of digit
# n=input("enter number:")
# r=1
# for i in n :
#     r=r*int(i)
# print(r)

"""
2. When we have more than one iterator and we
 want to access the elements
"""

# Id_List=[10,20,30]
# names_List=["Ankit","Prince","Shiva"]
# Age_List=[40,60,70]
# for i in range(len(Id_List)):
#     print("Cust Id:",Id_List[i],"Name:",names_List[i],"Age:",Age_List[i])
#

"""
3. When we want to access more than one element
in one iteration.
"""
# l=[20,30,40,50,60]    #4 time
# for i in range(len(l)-1):  # range(4):0,1,2,3
#     e=l[i]+l[i+1]
#     print(e)

"""
Loop keywords:
for
break: To exit from the loop 
continue: To skip some particular iteration
else: Will run if loop will complete without 
    break in between.
"""

# "2sq,3sq,4sq,7sq,8sq,9sq print"
# for i in range(2,10):   #i=2,3,4,5,6,7,8,9
#     if(i==5 or i==6):
#         continue
#     print(i**2)

"""
# break keyword: stop
"""
# for i in range(10):
#     break
#     print("CETPA")

# #New Program
# for i in range(10):
#     if(i==5):
#         break
#     print("CETPA")
#
# New Program
# for i in range(10): #i=0,1,2,...9
#     if(i==5):
#         break
#     print("CETPA")
# else:
#     print("Loop is Complete")

#New Program

# for i in range(10): #i=0,1,2,...9
#     print("CETPA")
# else:
#     print("Loop is Complete")


"""
WAP to check if a number is Prime No or not.
7: Divide by 2, 3,4....6
"""
# #Business Logic Layer
# def checkPrime(n):  #n=25
#     for i in range(2,n):    #2,3,4,...24
#         if(n%i==0):
#             return "Not Prime"
#     return "Prime"
#
# #Presentation Layer
# n=int(input("Enter Any Number:"))   #n=25
# res=checkPrime(n)
# print("The entered number is",res)
#

# test pdf
"""
question 1 
L=[2,4,5,7,8,9,10,22]
for i in range(len(L)):
    print(L[i]**2)
    
# Print Odd numbers between 1 to 100.
question 2 
for i in range(1,101,2):
    print(i)

# question 3
 Take X as int input from user, print the 10 element of following series:
 X, X3,, X5, X7……….

X=int(input("Enter any number: "))
for i in range(10):
    p=2*i+1      #odd number=2(n)+1
    print(X**p)

# question 4
# To design your own count function. Find the number of times an element is
# present in a list [2,3,4,5,6,2,3,4,2,3,4,2]. Take the element as input from the
# user. Don’t use predefined methods, use loop and give the answer.
l=[2,3,4,5,6,2,3,4,2,3,4,2]
print("[2,3,4,5,6,2,3,4,2,3,4,2]")
n=int(input("Enter any no. from list: "))
count=0
for i in l:
    if i==n:
        count=count+1

print(f"There are {count} numbers in total.")



"""


"""
for i in range(lower_bound,upper_bound,step_size):
    set of statements
a. Firstly value of i=lower_bound
b. It will be checked everytime that value is less than
upper_bound
c. Every time value of i will be incremented by
step_size
Ex: 2 to 9 loop run with step size 3
for i in range(2,10,3):
    set of statements 

while loop:
i=lower_bound
while(i<upper_bound):
    set of statements
    i+=step_size    #i=i+step_size

Ex: 2 to 9 loop run with step size 3
i=2
while(i<10):        #while(i<=9)
    set of statements
    i+=3

"""
# #To Excess all element in a string
# a="cetpa"
# for e in a:
#     print(e)
#

# a=input("enter any string:")
# for i range(2, 3):
#     print(i)
#     print(a)


def count(n):
    if n==1:
        return 1
    return n*count(n-1) 
num = int(input("Enter any no. from list: "))
print(count(num))



