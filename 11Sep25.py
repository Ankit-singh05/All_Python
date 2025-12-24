""
"""
Doubts:

If new version comes, search in google,
the documentation of the new version.
"""
# print(22_22)
# print(2_9_8_7)
# print(56_29.87)
# print(int("34_67"))
# print(float("45_789"))

"""
Loops
Conditions
Indentation
Data types
Slicing
Indexing

Customer Management System:
CRM: Customer Relationship Management.

Customer Management System: First Project
As easy as possible, we will keep on changing
in the project.

Management System:
Database interact: Most important instructions
CRUD Operations
Create
Read
Update
Delete

How to add a new customer
How to search a customer
How to delete customer
How to modify a customer
Display all customers.

List: Collection of heterogeneous data types.
L=[10,99.0,True...]

function_name(arguments)

obj_name.method_name(arguments)

id's are generally called primary keys:
Unique and not null

"""
# #New Program
# id_list=[10,20,30]
# name_list=["Vikas","Anil","Amit"]
# name="Awadhesh"
# name_list.append(name)
# print(name_list)

# #New Program
# id_list=[10,20,30]
# i=id_list.index(30)
# print(i)
# print(id_list[1])
# print(id_list[2])
# print(id_list[i])



# #New Program
# id_list=[10,20,30]
# name_list=["Vikas","Anil","Amit"]
# age_list=[39,41,45]
# id=int(input("Enter the id to search cust:"))   #id=20
# i=id_list.index(id) #i=1
# print("Cust ID:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i])



"""
Delete a customer
"""
# #New Program
# id_list=[10,20,30]
# id_list.remove(20)
# print(id_list)

# #New Program
# id_list=[10,20,30]
# id_list.pop()
# print(id_list)

# #New Program
# id_list=[10,20,30]
# id_list.pop(1)
# print(id_list)

"""
There is no negative marking in our session

pop


"""
# #New Program
# id_list=[10,20,30]
# name_list=["Vikas","Anil","Amit"]
# age_list=[39,41,45]
# id=int(input("Enter the id to delete cust:"))   #id=20
# i=id_list.index(id) #i=1
# id_list.pop(i)
# name_list.pop(i)
# age_list.pop(i)
# print(id_list,name_list,age_list)

# #New Program
# a=5;b=7;r=a+b;print(r)

# #New Program
# L=[100,200,300]
# i=1
# L[i]=500
# print(L)



# #New Program
# id_list=[10,20,30]
# name_list=["Vikas","Anil","Amit"]
# age_list=[39,41,45]
# id=int(input("Enter the id to Modify cust:"))   #id=20
# name=input("Enter the updated name:")   #"Sameer
# age=input("Enter the updated age:")     #16
# i=id_list.index(id) #i=1
# name_list[i]=name
# age_list[i]=age
# print(id_list,name_list,age_list)

"""
Display All Customers
"""
# #New Program
# id_list=[10,20,30]
# name_list=["Vikas","Anil","Amit"]
# age_list=[39,41,45]
# for i in range(len(id_list)): #i=0,1,2
#     print("Cust ID:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i])

"""
Synopsys:
Purpose: 


Project Report:

Possible Modifications:
1. city, state,pin code, gender, address, email id.....
2. Modification for selected item: 
3. Login system: 
4. Validations: Mobile No, gender, pin code, .....
id must be unique.
if(id in id_list):
5. Multiple users add, extend
6. random id or sequential id which will be system
generated id
7. Search: if id not exist then warning message
8. Permanent Storage: File Handling, Database connectivity
9.


 
"""
# #New Program
# import random
# r=random.random()   #0 to 1
# print(r)

# #New Program
# import random
# r=random.randint(1,6)   #Upper bound won't be discarded
# print(r)

#New Program
# import random
# id=random.randint(100000,999999)   #Upper bound won't be discarded
# print(id)

# #New Program
# s="23*123"
# print(s.isdecimal())

# #New Program
# s="23123abc"
# print(s.isdecimal())

# #New Program
# s="23123"
# print(s.isdecimal())  #String method





# "CMS"
# #Business Logic Layer
# import random
# id_list=[]
# name_list=[]
# age_list=[]
# mob_list=[]
# def addCustomer(id,name,age,mob):
#     id_list.append(id)
#     name_list.append(name)
#     age_list.append(age)
#     mob_list.append(mob)
# def searchCustomer(id): #20
#     i=id_list.index(id)     #i=1
#     return i
# def deleteCustomer(id): #20
#     i=id_list.index(id) #i=1
#     id_list.pop(i)
#     name_list.pop(i)
#     age_list.pop(i)
#     mob_list.pop(i)
# def modifyCustomer(id,name,age,mob):    #id=20, name="Awadhesh
#     i=id_list.index(id) #i=1
#     name_list[i]=name
#     age_list[i]=age
#     mob_list[i]=mob
#
#
# #Presentation Layer
# "Welcome to Saloni's CMS"
# def getId():
#     while(1):
#         id=input("Enter Cust ID:")
#         if(id not in id_list):
#             return id
#         else:
#             print("Duplicate Id")
# def generateId():
#     while(1):
#         id=random.randint(100000,999999)
#         if(id not in id_list):
#             return id
# def getMob():
#     while(1):
#         mob=input("Enter Cust Mob:")    #"12345678**"
#         if(mob.isdecimal() and len(mob)==10):
#             return mob
#         else:
#             print("Incorrect mob no")
#
# while(1):
#     choice=input("Enter Choice: 1 Add Cust, 2 Search Cust,"
#                  "3 Delete Cust, 4 Modify Cust, 5 Display All, "
#                  "6 Exit:")
#     if(choice=="1"):    #Add new customer
#         # id=getId()  #10, 20
#         id=generateId()
#         name=input("Enter Cust Name:")  #Vikas, "Anil"
#         age=input("Enter Cust Age:")    #39, 41
#         mob=getMob()    #1234, 2345
#         addCustomer(id,name,age,mob)
#         print("Customer Added Successfully")
#     elif(choice=="2"):  #Search a Customer
#         id=input("Enter Cust Id to search:")    #20
#         i=searchCustomer(id)    #
#         print("Cust ID:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i],"Mob List:",mob_list[i])
#     elif(choice=="3"):  #Delete a Customer
#         id=input("Enter Cust Id to delete:")    #id=20
#         deleteCustomer(id)
#         print("Customer Deleted Successfully")
#     elif(choice=="4"):  #Modify a Customer
#         id=input("Enter Cust Id:")  #id=20
#         name=input("Enter Cust updated name:")  #Awadhesh
#         age=input("Enter Cust updated age:")    #16
#         mob=input("Enter Cust updated mob:")    #1234
#         modifyCustomer(id,name,age,mob)
#         print("Customer Modified Successfully")
#     elif(choice=="5"):  #Display All Customers
#         for i in range(len(id_list)):   #i=0,1,2
#             print("Cust ID:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i],"Cust Mob:",mob_list[i])
#     elif(choice=="6"):  #Exit
#         print("Thanks for using Saloni's CMS")
#         break
#     else:
#         print("Incorrect Choice")









