""
"""
Doubts Please:

Loops:
"""
# #New Program
# s="Cat"
# for e in s:
#     print(e)

# #New Program
# s="Cat"
# for i in range(len(s)): #range(3):0,1,2
#     print(s[i])

# #New Program: "4597": Multiply of Digits
# n=input("Enter Any Number:") #n="4597"
# r=1
# for e in n:
#    r=r * int(e)
# print(r)

"""
When we use generally following syntax:
for i in range(len(iterator)...
1. When we have to access selected elements: alternate
elements, or skip few elements in between
2. When we have more than one iterator and we
want to access the elements
3. When we want to access more than one element
in one iteration.

No Practice means No Learning:
"""
# #New Program
# id_list=[10,20,30]      #i=0,1,2
# name_list=["Vikas","Anil","Amit"] #i=0,1,2
# age_list=[39,41,45] #i=0,1,2
# for i in range(len(id_list)):   #i=0,1,2
#     print("Cust Id:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i])

"""

"""
# #New Program
# L=[10,20,30,40]     #3 times
# for i in range(len(L)-1):   #range(3): 0,1,2
#     e=L[i]+L[i+1]
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
#
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

# #New Program
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
#Business Logic Layer
def checkPrime(n):  #n=25
    for i in range(2,n):    #2,3,4,...24
        if(n%i==0):
            return "Not Prime"
    return "Prime"

#Presentation Layer
n=int(input("Enter Any Number:"))   #n=25
res=checkPrime(n)
print("The entered number is",res)

# #New Program
# n=int(input("Enter Any Number:"))   #n=25
# for i in range(2,n):    #i=2,3,4,5....24
#     if(n%i==0):
#         print("The entered number is not prime")
#         break
# else:
#     print("The entered number is prime")

# #New Program
# n=int(input("Enter Any Number:"))   #n=5
# if(n%2==0):
#     print("The entered number is even")
# else:
#     print("The entered number is odd")

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
# #New Program
# for i in range(2,10,3):
#     print(i)
#
# i=2
# while(i<10):    #i=2,i=5, i=8, i=11
#     print(i)
#     i+=3        #i=5, 8, 11

# #New Program
# s="CETPA"
# i=0
# while(i<len(s)):    #i=0,1,2,3,4
#     print(s[i])
#     i+=1

"""
while loop is generally used for
1. infinite loops
2. for floating point type bounds and step_size

range(arguments): arguments must be of int type only


while(condition): 
Till the time condition is True, while loop will
execute.
"""
# for i in range(2,3.5,0.5):
#     print(i)

# #New Program
# i=2
# while(i<3.5):
#     print(i)
#     i+=0.5

# #New Program
# while(1):
#     print("CETPA")

"""
Kuch baccho ko, I can see and feel that 
loops samajh me nahi aaye hai, because they
are learning it first time and not doing 
any practice at home.

At-least course khatam hone ke baad bhee
1 month tak loops kee practice karte rehna.

Programming will improve your logical skills
and analytical skills as well.

I5, 8 GB RAM, 500 GB SSD: More than sufficient:
My computer configuration

Entrepreneurship Skills:

Travel+Education Business

Nested Loops: Loop inside loop
If we have two loop, one inside another.
Outer loop n times run
Inner loop m times run
Then statements inside inner loop will run nxm times
"""
# #New Program
# for i in range(3):      #i=0,1,2
#     for j in range(4):  #j=0,1,2,3
#         print(i,j)


# #New Program
# for i in range(3):      #i=0,1,2
#     print("Outer Loop")
#     for j in range(4):  #j=0,1,2,3
#         print("Inner Loop")
# print("Outside Loop")


# #New Program
# for i in range(3):      #i=0,1,2
#     print(i,"Outer Loop")
#     for j in range(4):  #j=0,1,2,3
#         print(i,j,"Inner Loop")
# print("Outside Loop")

# #New Program
# L1=[[10,20],[30,40],[50,60]]
# for e in L1:
#     print(e)

# #New Program
# L1=[[10,20],[30,40],[50,60]]
# print(L1)
# for e in L1:    #e=[10,20]
#     print(e)
#     for a in e: #a=10,20
#         print(a)


"""WAP to check all Prime nos in a given range
10 to 30

One of the best example of nested loops
"""
# #New Program
# lower=int(input("Enter Lower range value:")) #10
# upper=int(input("Enter Upper range value:")) #30
# for n in range(lower,upper+1):    #n=10,11,12...30
#     for i in range(2,n):    #i=2,3,4,5....24
#         if(n%i==0):
#             # print("The entered number is not prime")
#             break
#     else:
#         print(n,"is prime")

# #New Program
# L=[]
# lower=int(input("Enter Lower range value:")) #5
# upper=int(input("Enter Upper range value:")) #35
# for n in range(lower,upper+1):    #n=5,6,7....35
#     for i in range(2,n):    #i=2,3,4,5....24
#         if(n%i==0):
#             # print("The entered number is not prime")
#             break
#     else:
#         L.append(n)
# print("All Prime Nos in given range:",L)

# #New Program: 5 to 35
# for n in range(5,36): #n=5,6,7....35
#     print(n)

"""
Please revise all loops concepts and programs
and will do more practise tomorrow.

"""









