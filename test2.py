# n = int(input("Enter Any Number: "))   # e.g., n = 5
# a = 1
# for i in range(10):
#     print(n * a)
#     a += 2

#new program
# n = int(input("enter a element: "))
# for i in range(1,10,2):
#     print(n*i)

"""
we want to create this
*
**
***
****
*****
"""
# n=int(input("enter no. of element: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

"""
now print 
1
12
123
1234
12345
"""
# n=int(input("enter any no.: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
"""
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
"""
# n=int(input("enter any no.: "))
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(j,end=" ")
#     print()


"""
now reverse the pattern
*****
****
***
**
*
"""
# n=int(input("enter any no.: "))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()
"""
to print no.  
12345
1234
123
12
1
"""
# n=int(input("enter any no.: "))
# for i in range(n,0,-1):
#     for j in range(1,i+1,1):
#         print(j,end=" ")
#     print()

"""
now with no.
54321
4321
321
21
1


"""
# n = int(input("Enter any number: "))
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()

"""
create same design 
"""
# n=int(input("take any no.: "))
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(j,end="")
#     print()


# n=int(input("enter any no.: "))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end="")
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
# n = int(input("enter any no.: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()

"""
let do this with no.
    1
   12
  123
 1234
12345

"""
# n=int(input("enter any no.:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     print()

"""
reverse the pattern 
    5
   45
  345
 2345
12345
"""
# n=int(input("Enter no.: "))
# for i in range(n,0,-1):
#     for j in range(i-1):
#         print(" ",end="")
#     for k in range(i,n+1):
#         print(k,end="")
#     print()



"""
reverse the pattern
54321
 4321
  321
   21
    1
"""
# n=int(input("Enter no.: "))
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         print(k,end="")
#     print()


"""
reverse the pattern 
    54321
   4321
  321
 21
1
"""
# n=int(input("Enter no.: "))
# for i in range(n,0,-1):
#     for j in range(i-1):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         print(k,end="")
#     print()


"""
reverse the pattern 
*        *
**      **
***    ***
****  ****
**********
"""
# n=int(input("Enter no.: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     for k in range(2*(n-i-1)):
#         print(" ",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()
#

"""
pattern with no.
we have to mix this two code to create 
# n=int(input("enter any no.: ")) 
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
 n=int(input("enter any no.:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     print()
output
1        1
12      12
123    123
1234  1234
1234512345

"""
# n=int(input("enter any no.:"))
# for i in range(1,n+1):
#     for j in range(1, i + 1):
#         print(j,end="")
#     for k in range(2*(n-i)):
#         print(" ",end="")
#     for l in range(1, i+1):
#         print(l,end="")
#     print()

# n=int(input("enter any no.: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(2*(n-i)):
#         print(" ",end="")
#     for l in range(i,0,-1):
#         print(l,end="")
#     print()

"""
now print it updown
1234554321
1234  4321
123    321
12      21
1        1
n=int(input("enter any no.: "))
for i in range(n,0,-1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
n=int(input("Enter no.: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end="")
    print()
"""
# n=int(input("enter any no.: "))
# for i in range(n,0,-1):
#     for j in range(1,i+1,1):
#         print(j,end="")
#     for k in range(2*(n-i)):
#         print(" ",end="")
#     for l in range(i,0,-1):
#         print(l,end="")
#     print()


"""
mix both of this pattern to create new one 
1234554321
1234  4321
123    321
12      21
1        1
1        1
12      21
123    321
1234  4321
1234554321

"""
# n=int(input("enter any no.: "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(2*(n-i)):
#         print(" ",end="")
#     for l in range(i,0,-1):
#         print(l,end="")
#     print()
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(2*(n-i)):
#         print(" ",end="")
#     for l in range(i,0,-1):
#         print(l,end="")
#     print()

# n=int(input("enter any no.: "))
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(j,end="")
#     for k in range(2*(n-i)):
#         print(" ",end="")
#     for l in range(i,n+1):
#         print(l,end="")
#     print()
# for i in range(1, n + 1):
#     for j in range(n,i-1,-1):
#         print(j,end="")
#     for k in range(2*(n-i)):
#         print(" ",end="")
#     for l in range(i,n+1):
#         print(l,end="")
#     print()

"""
5432112345
5432  2345
543    345
54      45
5        5
5        5
54      45
543    345
5432  2345
5432112345
"""
# n=int(input("enter any no.: "))
# for i in range(1, n + 1):
#     for j in range(n, i - 1, -1):  # Left side: n to i
#         print(j, end="")
#     for k in range(2 * (i - 1)):  # Spaces: decrease as i increases
#         print(" ", end="")
#     for l in range(i, n + 1):  # Right side: i to n
#         print(l, end="")
#     print()
# for i in range(n, 0, -1):
#     for j in range(n, i - 1, -1):  # Left side: n to i
#         print(j, end="")
#     for k in range(2 * (i - 1)):  # Spaces: increase as i decreases
#         print(" ", end="")
#     for l in range(i, n + 1):  # Right side: i to n
#         print(l, end="")
#     print()
"""
enter any no.: 5
 ******* 
  *****  
   ***   
    * 
"""
# n=int(input("enter any no.: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for k in range(1,2*(n-i)):
#         print("*",end="")
#     for l in range(1,i+1):
#         print(" ",end="")
#     print()


# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(65 + j), end=" ")
#     print()
# new program
# a
# bb
# ccc
# dddd
# eeeee
# ffffff

# n=int(input("enter any no.: "))
# for i in range(n):
#     ch = chr(97 + i)
#     for j in range(i+1):
#         print(ch, end="")
#     print()



