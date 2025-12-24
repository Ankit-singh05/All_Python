"""
Write a program to check if no. is positive ,negative and zero.
"""
from copyreg import constructor

# n=int(input( " Enter any no.  "))
# if n>=1:
#     print("no. is positive")
# elif n<=-1:
#     print("no. is negative")
# else:
#     print("no. zero")

"""
write a program to check username and password from user
"""
# UId = "pramod123"
# Pass = "123456789"
# while True:
#  username = input("Enter Username: ")
#  password = input("Enter password: ")
#  if username==UId and password==Pass:
#     print("Welcome to tha website" + username + "!")
#     break
#  else:
#     print("Wrong username or password")

"""
To Check how many digit in input 
"""
# while True:
#  n = int(input("Enter Any No.:  "))
#  i = len(str(n))
#  if i>=0:
#     print(f"{i} total digit")
#     break

"""
To Check no. is smaller four digit or not 
"""
# while True:
#     n=int(input("Enter no.: "))
#     i = len(str(n))
#     if i <= 4:
#         print("Enter No. is Smaller or equal to four Digit")
#         break
#     else:
#         print("Enter No. is bigger than four Digit")

"""
To check which no. is bigger in three no.
"""
# n1 = int(input("Enter no. 1: "))
# n2 = int(input("Enter no. 2: "))
# n3 = int(input("Enter no. 3: "))
# if n1 > n2 and n1 > n3:
#     print("No. 1 is bigger")
# elif n2 > n1 and n2 > n3:
#     print("No. 2 is bigger")
# elif n3 > n1 and n3 > n2:
#     print(" No. 3 is bigger")

"""
To check Enter no. can mmake triangle
    hint:- in triangle two side sum is equal to third 
"""

# while True:
#   a = int(input("Enter side 1 no.: "))
#   b = int(input("Enter side 2 no.: "))
#   c = int(input("Enter side 3 no.: "))
#   if a+b>c or b+c>a or c+a>b:
#       print("It can be a triangle")
#       break
#   else:
#       print("It can't be a triangle")

"""
7.	write a python to check  Whether the triangle will be an obtuse-angle, or a right-angle or an acute-angle triangle.
HINT: 
In Right angle triangle the square of the length of the longest side of a triangle is equal to the sum of the squares of the other two sides 

In Obtuse Triangle  the sum of the squares of the two shorter sides of a triangle is smaller than the square of the longest side, the triangle is obtuse.

In Acute angle triangle the sum of the squares of the two shorter sides of a triangle is greater than the square of the longest side, the triangle is acute

"""
# while True:
#     a = int(input("Enter side 1: "))
#     b = int(input("Enter side 2: "))
#     c = int(input("Enter side 3: "))
#
#     # Step 1: Check if sides can form a triangle
#     if a + b <= c or a + c <= b or b + c <= a:
#         print("Not a triangle\n")
#         continue
#
#     # Step 2: Check for Right Angle Triangle
#     if a**2 + b**2 == c**2:
#         print(f"a² + b² = c²  → Right Angle Triangle\n")
#     elif a**2 + c**2 == b**2:
#         print(f"a² + c² = b²  → Right Angle Triangle\n")
#     elif b**2 + c**2 == a**2:
#         print(f"b² + c² = a²  → Right Angle Triangle\n")
#
#     # Step 3: Check for Obtuse Triangle
#     elif a**2 + b**2 < c**2:
#         print(f"a² + b² < c²  → Obtuse Triangle\n")
#     elif a**2 + c**2 < b**2:
#         print(f"a² + c² < b²  → Obtuse Triangle\n")
#     elif b**2 + c**2 < a**2:
#         print(f"b² + c² < a²  → Obtuse Triangle\n")
#
#     # Step 4: Check for Acute Triangle
#     elif a**2 + b**2 > c**2:
#         print(f"a² + b² > c²  → Acute Triangle\n")
#     elif a**2 + c**2 > b**2:
#         print(f"a² + c² > b²  → Acute Triangle\n")
#     elif b**2 + c**2 > a**2:
#         print(f"b² + c² > a²  → Acute Triangle\n")


"""
8.	Write a python program  to check the triangle , is equilateral, isosceles, or scalene.
HINT:
In Equilateral triangle all three sides are equal
In isosceles triangle any two side are equal
In scalene triangle all three side are unequal

"""

# while True:
#     a = int(input("Enter Side 1 no.: "))
#     b = int(input("Enter Side 2 no.: "))
#     c = int(input("Enter Side 3 no.: "))
#
#     # first check it is triangle or not
#     if a+b<=c or a+c<=b or c+b<=a:
#         print("Not a triangle\n")
#         continue
#
#     #To check it is Equilateral Triangle
#     if a==b==c:
#         print("it is Equilateral triangle\n")
#     #To check it is isosceles Triangle
#     elif a==b or a==c or b==c:
#         print("it is isosceles triangle\n")
#     #To check it is scalene triangle
#     elif a!=b or a!=c or b!=c:
#         print("it is scalene triangle\n")

"""
9.	A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
    The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
    On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders
    for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery 
    based toys, key-based toys, and electrical charging based toys respectively. 
    Write a program that reads the product code and the order amount and prints out the net amount that the customer is
    required to pay after the discount  
"""
# bat_order = 100
# key_order = 20
# elec_order = 50
# Totaly = 0
#
# while True:
#     print("1.bat_order = 100\n2.key_order = 20\n3.elec_order = 50\n ")
#     code = input("Enter product code: ")
#
#     if code == "1":
#         print("Battery Based Toys\n ")
#         Total = int(input("Total no. of toy.:"))
#         Totaly = bat_order * Total
#         print(f"Total Amount of toy.:{Totaly}\n")
#         if Totaly >= 1000:
#             discount = Totaly * 0.10
#             print(f"Total amount to pay : {Totaly-discount}\n")
#
#     elif code == "2":
#             print("key Based Toys\n ")
#             Total = int(input("Total no. of toy.: \n"))
#             Totaly = key_order * Total
#             print(f"Total Amount of toy.:{Totaly}\n")
#             if Totaly >= 100:
#                 discount = Totaly * 0.05
#                 print(f"Total amount to pay : {Totaly-discount}\n")
#     elif code == "3":
#         print("Electrical Charging Based Toys\n ")
#         Total = int(input("Total Amount of toy.: \n"))
#         Totaly = elec_order * Total
#         print(f"total amount to pay : {Totaly}\n")
#         if Totaly >= 500:
#             discount = Totaly * 0.10
#             print(f"Total amount to pay : {Totaly-discount}\n")
#
"""
10.	 A function f is defined as follows :
        f(x)   =    ax3 – bx2 + cx –d,                  if x > k
        f(x)          =    0,                                   if x = k
        f(x)  =    -ax3 + bx2 – cx +d,                 if x <k 

"""
# k=0
# while True:
#     x = int(input("Enter no.:"))
#     if x>k:
#         print("If X > K Then")
#         print("f(x) = ax³ – bx² + cx –d")
#     elif x==k:
#         print("If X = K Then")
#         print("f(x) = 0")
#     elif x<k:
#         print("If X < K Then")
#         print("f(x) = -ax³ + bx² – cx +d")

"""
11. The Paschim Gujarat Vij Company Ltd. computes the electricity bill based on the following table:
Units Consumed	Charges
0-100	0.50 per unit
101-200	Rs. 50 plus Rs. 1 per unit over 100 units
201-300	Rs. 150 plus 1.50 per unit over 200 units
> 300	Rs. 300 plus Rs.2 per unit over 300 units
1.	Ask user to enter the Past meter reading and current meter reading.
2.	Find the units consumed.
3.	Compute the bill according to given matrix.

"""
# Price = 0
# Total = 0
# while True:
#   Past = int(input("Enter the Past meter reading: "))
#   Current = int(input("Enter the current meter reading: "))
#   Total = Current - Past
#   print("The total unit that the customer use.:", Total)
#   if Total==0 or Total<=100:
#       Price = Total*0.50
#       print("The meter reading Price is: Rs. " + str(Total+Price))
#   elif Total==101 or Total<=200:
#       Price = (Total*1)+50
#       print("The meter reading Price is: Rs. " + str(Total+Price))
#   elif Total==201 or Total<=300:
#       Price = (Total*1.50)+150
#       print("The meter reading Price is: Rs. " + str(Total+Price))
#   elif Total>=300:
#       Price = (Total*2)+300
#       print("The meter reading Price is: Rs. " + str(Total+Price))

"""
For Loop 

1. iterate : it's means to extracting the character 
2. Python have two type of Loop 
   1.For Loop
   2.While Loop
  
#1.For Loop: 
    1.when i want to extract the Character from given sequence
    2.when we want to do task n number of times we use "for" loop 
"""
    # simple for loop
# n = "Ankit"
#
# for i in n:
#     print(i)

# Simple For loop with example
# n = "Ankit"
#
# for i in n:
#     print(i)
#     print(n)
#
# print("bye")

# Take User Input to check
# n = input("ENTER Any thing: ")
# for i in n:
#     print(i)
# print("Ankit")

# To Count total no. of loop
# n = "Ankit"
# C = 0
# for i in n:
#     C = C+1
# print(C)

#list
# l = [1,2,3,4,5,6,7,8,9]
# for i in l:
#     print(i)
"""
shopping_list = ["eggs", "milk", "bread", "cheese"]

# Your turn: Write a for loop here to print each item
# Hint: Use a temporary variable name like 'item'
"""
# shopping_list = ["eggs", "milk", "bread", "cheese"]
#
# for item in shopping_list:
#     print(item)

"""
 l = [1,2,3,4,5,6,7,8,9]
 calculate the sum of all items in l
"""
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum = 0
# for i in l:
#     sum += i
# print(sum)

"""
l = [1,2,3,4,5,6,7,8,9]
calculate the avg of list 
"""
# l = [1,2,3,4,5,6,7,8,9]
# sum = 0
# count = 0
# for i in l:
#     sum += i
#     count += 1
# print(sum/count)

"""
l = [1,2,3,4,5,6,7,8,9]
calculate the product or multiply of all item in l
"""
# l = [1,2,3,4,5,6,7,8,9]
# product = 1
# for i in l:
#     product *= i
# print(product)

"""
l = [1,2,3,4,5,6,7,8,9]
sum of Square of every element in l
"""
# l = [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in l:
#     sum += i**2
#     print(sum)
# print(sum)

"""
l = [1,2,3,4,5,6,7,8,9]
Count no. of even and no. of odd no. from l
"""
# l = [1,2,3,4,5,6,7,8,9]
# e = 0
# o = 0
# for i in l:
#     if i % 2 == 0:
#         # print(f"{i} even no")
#         e += 1
#     elif i % 2 == 1:
#         # print(f"{i} odd no.")
#         o += 1
# print(f"total no. of even no.:{e} and Total odd no.:{o}")

"""
take input in list then do loop in it
"""
# l = list(input("Enter the elements separated by space: ").split())
# print(l)
# sum = 0
# for i in l:
#     sum += int(i)
# print(sum)

"""
we can use single line of code to get list 
"""
# num = []
# for i in range(1,11):
#     num.append(i)
# print(num)

# num = [x for x in range(1,11)]
# print(num)

"""
create a pyramid using while and if loop
1
12
123
1234
12345

"""
# rows = int(input("Enter rows: "))
# i = 1
#
# while i <= rows:
#     if True:  # this controls one row, allowed
#         spaces = rows - i
#         stars = 2 * i - 1
#         print(" " * spaces + "*" * stars)
#
#     i += 1

"""
create a pyramid using for loop

1
12
123
1234
12345

"""
# n = int(input("Enter any NO.:  "))
#
# for i in range(1,n+1):
#
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#

"""
Take a number from user. Check if it is positive, negative, or zero.
"""

# while True:
#
#   num = int(input("Enter a number: "))
#   if num<0:
#     print("Sorry, that's not a positive number")
#   elif num==0:
#     print("No. is Zero")
#   elif num>0:
#     print("No. is positive")

"""
1.Input age. Print if user is adult (18+) or minor.
2.Input two numbers and print which one is greater.
3.Input a number. Check if it is even or odd.
4.Input marks. Print:
Pass if marks ≥ 40
Fail otherwise
5.Take a letter and check if it is vowel or consonant.
6.Input temperature and check:
30 → "Hot"
15–30 → "Warm"
<15 → "Cold"
"""
#1# while True:
#     age = int(input("Enter Age"))
#     if age < 18:
#         print("teen Girl")
#     elif age > 18:
#         print("big Girl")

"""
1.Input 3 numbers and print the largest.
2.Check if a given year is a leap year.
3.Check if a number is divisible by 5 AND 11.
4.Take two numbers and a string operator (+ - * /).
5.Perform the correct operation.
 Input triangle sides. Print if triangle is valid.
 Input triangle angles. Print if triangle is valid (sum = 180).
 Input month number (1–12). Print number of days.

6.Check if input character is:
 Alphabet
 Digit
 Special symbol

"""
#1
# while True:
#     n1 = int(input("Enter a number: "))
#     n2 = int(input("Enter another number: "))
#     n3 = int(input("Enter a third number: "))
#     if n1 > n2 and n1 > n3:
#         print(f"The number {n1} is greater ")
#     elif n2 > n1 and n2 > n3:
#         print(f"The number {n2} is greater ")
#     elif n3 > n1 and n3 > n2:
#         print(f"The number {n3} is greater ")

#2
# while True:
#     year = int(input("Enter year: "))
#     if year % 4 == 0:
#         print("Yes")

#3
# while True:
#     n = int(input("Enter a number: "))
#     if n % 5 ==0 and n % 11 == 0:
#         print("The number is valid.")
#     else:
#         print("The number is invalid.")

#4
# while True:
#   n1 = int(input("Enter a number: "))
#   n2 = int(input("Enter another number: "))
#   o1 = input("Enter operator (+ - * /).: ")
#
#   if o1 == "+":
#       c=n1+n2
#       print(c)
#   elif o1 == "-":
#       c=n1-n2
#       print(c)
#   elif o1 == "*":
#       c=n1*n2
#       print(c)
#   elif o1 == "/":
#       c=n1/n2
#       print(c)
#   else:
#       print("Invalid operator")

#5
# while True:
#     s1 = int(input("Enter side1: "))
#     s2 = int(input("Enter side2: "))
#     s3 = int(input("Enter side3: "))
#     if s1+s2>s3 or s1+s3>s2 or s2+s3>s1:
#         print("Tringle is valid")
#     else:
#         print("Tringle is invalid")
#         continue
#     a1= int(input("Enter angle: "))
#     a2= int(input("Enter angle: "))
#     a3= int(input("Enter angle: "))
#     if a1+a2+a3 == 180:
#         print("Tringle is valid")
#     else:
#         print("Tringle is invalid")
#         continue
#     m = int(input("Enter month: "))
#     if m == 1 or m == 3 or m == 5 or m == 7 or m == 8:
#         print("Month have 31 days in it ")
#     elif m == 2 :
#         print("Month have 28 or 29 days in it ")
#     elif m==4 or m == 6 or m == 9 or m == 11:
#         print("Month have 30 days in it ")

#6
# while True:
#  c = input("Enter Any Thing: ")
#  if c.isalpha():
#     print("Alphabet")
#  elif c.isdigit():
#     print("Number")
#  else:
#      print("Special symbol")

"""
1.Input 3 sides and determine triangle type:
 Equilateral
 Isosceles
 Scalene
 Classify a triangle as:

Right angled

Acute

Obtuse

Input salary and calculate tax using:

salary < 2.5L → no tax
2.5L–5L → 5%
5L–10L → 20%
>10L → 30%


Input time in 24-hour format, print greeting:

5–12 → Good Morning

12–17 → Good Afternoon

17–21 → Good Evening

else → Good Night

Input username + password, allow user 3 attempts.
After 3 wrong tries, lock account.

Grade system:

90–100 → A
80–89  → B
70–79  → C
60–69  → D
<60    → Fail


Ask for 4 subjects marks.
Print:

Total

Percentage

Grade using if-else
"""

"""
Find the largest of 4 numbers using only if–else (no max() function).

Input a number.
 Print if it is prime or not prime using if-else logic.

 Simulate a simple ATM machine:
  If balance >= withdrawal → deduct
  Else → print insufficient balance
  
 Input day number (1–7). Print today + tomorrow using if-else only.

Menu-driven program:

1 = Area of circle

2 = Area of square

3 = Area of triangle

Else = Invalid choice
"""

#Input a number.
#Print if it is prime or not prime using if-else logic.
while True:
    n1 = int(input("Enter Any no.: "))
    if  n1%2==1 and n1%n1==0:
        print(f" no. is Prime {n1}")

    else:
        print(f" no. is not Prime {n1}")