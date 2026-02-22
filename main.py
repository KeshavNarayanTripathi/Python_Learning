#                # This is Our Fist Program
# print("Namaste VS Code , we are learning Python")


#                    # COMMENTS 
# # fOR SINGLE line comment we use Hastag(#) & Simply do (ctrl+/)
# '''for multiline comment 
# we can do single or double quoted 
# three times'''
#       # OR
# """for multiline comment 
# we can do single or double quoted 
# three times"""  #this is also used for doc string



#                   #VARIABLES
#                   # Variables 

# a = 10; 
# sher = "Keshav"   #we can not do 2sher means number phele nhi use krne 
# # no use space between variables like (SHE R), dont use special character like @sher
# SheryiansSchool = "students" #pascal case
# sheryiansSchool = "students" #camel  case
# sheryians_school = "students" #snake case


#                  #DATATYPE

#                  #DataType

# #1 Numbers 
# a =10;      # Integer 
# b =20.5;    #float
# c =20j;     #complex where we use iota

# #2 Strings

# st = 'bshuxbhsbxhsbyg7s67as88876'; 
# am = "hbusudc8uwed723ye23ueuhd"; 

# #3 Boolean 
# # gives answer in true or false

# x = True; 
# y = False; 



# #STRING INDEXING

# #String indexing


# she = "Romania"; 
# print(she[5]); #ans is 'i'
# print(she[-2]) #ans is 'i'



# #STRING SLICING

# kes = "Keshav Tripathi"
# print(kes[0 : 10 : 2]);  # isme btata hai ki [start : end : kitni chhodh chhodh ke likhe] main thing end point nhi aata


# #TYPE CONVERSION

# a = 12;
# print(type(a))

# a = str(a)
# print(type(a))

# print(bool(a))  #Every value change in boolean and its will be in TRUE Except 7Values -> False, 0, 0.0, "", [List], (Tuple), {Dict}

# #implicit jisme python khud se ek dattype se dusre me change krta hai like-> 12/3 answer will be 4.0 so integer to string
# #Explicit jisme user use kare function



# #INPUT AND OUTPUT

# name = "Keshav"
# age = input("Enter Your Age ")  #input

# print("My name is", name, "and my age is", age); #output
# print(f"My name is {name} and my age is {age}") #Formated output



# #OPERATORS
# a =10;
# b = 20;

# # Arithmetic Operators
# print(a+b)  
# print(a-b) 
# print(a*b)
# print(b/a) #default answer will be in float so we can use flow division (b//a) to ye integer dega point ke baad wali sab gayab kar dega
# print(b//a) #decimal ke baad wala sab hata dega
# print(5**2)
# print(32%5) #Remainder 
# #python follows BODMAS

# #Assignment Operators
# a = 10; # = is assignment
# a = a +10 
# a +=10 
# a -= 10
# a /= 10
# a *= 10
# a **=10
# a %= 10

# #Comparison Operators
# #!=
# #>
# #<
# # <=
# # >=
# # ==

# #Logical Operator
# # AND, OR, NOT

# print(5>2 and 6>3)
# print(5>8 or 8<9)
# print(not True)



# #CONDITIONAL STATEMENT
# # if, else-if, if-elif-else

# a = 13;
# if a > 10:
#     print("Hello")
# else:
#     print(" Wrong")

# #Example
# money = int(input("Please provide me the money: ")) 
# if money <= 10:
#     print("I will have a chocoBar")
# elif money <= 20:
#     print("I will have a mango bite")    
# else:
#     print("I will have a cone")    


#     #QUESTIONS

#  #01. accept two numbers and print the gratest btw them
# a = int(input("Enter first number: "))    
# b = int(input("Enter Second number: "))    

# if a>b:
#     print(f"{a} is grater than {b}")
# elif a<b:
#     print(f"{b} is grater than {a}")    
# else:
#     print(f"{b} is equals to {a}")   

#   #02. accept the gender from the user as char and print the respective greeting message Ex- Good Morning Sir/Mam

# gen = input("Enter your gender as character(M or F): ")

# if gen == 'M' or gen == 'm':
#     print("Good Morning Sir")
# elif gen == 'F'or gen == 'f':
#       print("Good Morning Mam")   
# else:
#     print("Unidentified gender")   




# #LOOPS
# # for -> works on basis of numbers it needs number 10 baar print kro ya phir 100 baar, 
# # while -> works on condition like do until number becomes 100, 


# #FOR Loop
# a = range(1, 20, 1)   #arnge(start, end, kine number chhodh chhodh ke)

# for i in a:
#     print(i)

#      #AUR

# for i in range(1, 21, 1):
#    print(i)

# #     #AUR

# for i in range(21):
#              #end dena jaruri hai
#     print(i)    

# # reverse print from 16 to 1

# for i in range(16, 0, -1):    #(start, end, kitna number peeche)
#     print(i)


#FOR Loop in STRINGS

# a = "SHERYIANS"

# for i in range(9):
#     print(a[i])

# a = "Keshav Narayan Tripathi"

# for i in range(len(a)):
#     print(a[i])

# a = "SHERYIANS IS COOL"

# for i in a:
#     print(i)


  

             #BREAK & CONTINUE

# BREAK : in break ek point pe ja kar ruk gye aage nhi badhe
# for i in range(1,21):
#     if i == 15:
#         break
#     else:
#         print(i)

# CONTINUE : jo digit htani ho woh hta ke aage badhega 
# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i)




#OUESTIONS 
#1
# a = int(input("Enter any no. : "))

# for i in range(a):
#     print("Hello")

#2
# a = int(input("Which table do u want: "))

# for i in range(1, 11):
#     print(f"{a} * {i} = {a*i}")


#3
# a = int(input("Give any number: "))
# print(f"SUM of first {a} number is : ")

# sum = 0;
# for i in range(1, a+1):
#     sum = sum + i

# print(sum)    


#4
# a = int(input("Enter any number: "))

# sum = 0
# for i in range(1, a):
#     if a % i == 0:
#         sum = sum + i

# if sum == a:
#     print("Your number is perfect")
# else:
#     print("Your number is not perfect")


#5
# a = int(input("Enter any number: "))

# count = 0
# for i in range(1, a+1):
#     if a%i == 0:
#         count = count + 1

# if count == 2:
#     print("Number is Prime")  
# else:
#     print("Not Prime")            
        

#6
# a = "Keshav"

# b = ""
# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]

# print(b) 



#7
# a = "naman"

# b = ""
# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]

# if a == b:
#     print("It's Palindrome") 
# else:
#     print("Not palindrome")    

#8
# a =  "abcdef@#$%^&*562314"

# char = 0
# spchr = 0
# dig = 0

# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spchr += 1

# print(f"Digit is {dig}\nChar are {char}\nSpecial character {spchr}")



#WHILE LOOP : ye codition pe kaam krta hai, jab tak number 500 na ban jaaye tab tak ye 5 5 kar ke badhta rhe

# a = 1

# while a<= 30:
#     print(a)
#     a += 1


#GAME BNAO WITH WHILE LOOP


#Reverse Number
# a = int (input("Enter your number")) 
# rev  = 0
# while a>0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# print(rev)

#paindrome
# a = int(input("Enter your number "))

# copy = a
# rev = 0

# while a>0:
#     rev = rev*10 + a%10 
#     a = a//10

# if copy == rev:
#     print("It's Palindrome")    
# else:
#     print("Not Palindrome75")

#Guessing Number GAME
# import random 
# num = random.randint(1, 10)
# tries = 0
# while True:
#     guess = int(input("Enter your number between 1 to 10: "))
#     if num == guess:
#        tries +=1
#        print(f"Your are Right, you Guessed the number in {tries} tries")
#        break

#     elif num < guess:
#        tries +=1
#        print("Go a Little lower")

#     elif num > guess:
#        tries +=1
#        print("Go a Little Higher")     
#     else:
#        tries +=1
#        print("Sorry, You are wrong")
# 
#



#DATA STRUCTURES


#LIST
# 
# a = [12, 13, 14, 15, 16, 34.5, True, print()]  

# print(a[0:5])


#LIST TRAVERSING: its value can be change
# l = [1, 3, 4, 5, 6]

# l.append(7)
# l.insert(1, 2) #isme insert karenge 1 index par 2 number
# print(l)


# l = [12, 567, 43, 235, 347, 568, 45, 7]

# index = 0
# largest = l[0]

# for i in range(len(l)):
#     if l[i]>largest:
#         largest = l[i]
#         index = i

# print(f"Your largest number is {largest} of index {index}")      
# 
#   

# a = [13, 12, 14, 15, 16]    

# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break

# else:
#     print("Your list is sorted")    

# a = [-14, -12, 45, 58, 89]

# for i in a:
#     if i>0:
#         print(f"Postive numbers are {i}")
#     elif i<0:
#         print(f"Negative numbers are {i}")




#TUPLES

# a = (1, 2, 3, 4, 5)

# print(type(a))  #tuple and square brackets hote toh List ban jata

# NOTE: LIST value assign kar skta tha nayi nayi jaise 0 index pe agar 1 hai toh 12 kar do but but TUPLE me nhi kar skte


# a = (1, 2, 3, 4, 5, 5)

# index = a.index(5)

# print(index)

# count = a.count(5)

# print(count)


#SETS

# s = {1, 2, 3, 4, 5}

# print(type(s))
# print(s[0]) ISKE ANDAR HUM INDEX SE ACCESS NHI KAR SKTE AND SETS ME DUPLICATE VALUES NHI HOTI

# a = {1,2,3,4}
# b = {3,4,5,6}

# # s = a.union(b) #OR we can write it a|b
# # s = a|b #UNION
# # s = a&b #INTERSECTION


# print(s)

#DICTIONARY : Isme hum log key and value dete hai

# d = {10:100, 20:200, 30:300, 40:400}

# jaise humlogo ne ek list bnaya

# a = [1,2,3,4]

# b = a #to isme a me bhi same hoga and isko bolte hai deep copy
# # isiliye hum log karenge copyright

# b=a.copy() #isko bolte hai shallow copy
# b[0] = 100

# print(a) 


# same cheez jab dic me karte hai 

# d = {10:100, 20:200, 30:300, 40:400}

# # d2 = d.copy()

# # help(dict) for more methods to learn

# print(d.items())

# d1 = {10:100, 20:200, 40:400, 40:400}
# d2 = {40:300, 60:600, 70:700, 80:800}


# for i in d2:
#     d1[i] = d2[i]

# print(d1)    


# a = [1,1,1,1,2,2,3,3,3,3,3,4,4,5,5,5,6,7,8]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)        
# 
# 
#     FILE HANDLING

# p = open('main.py')

# print(p.read())

# r = open('soperman.txt', 'w')

# r.write("Hello this is Keshav and i am writing inside this file")

# r.close()



#   OOPS
# object oriented programming language

# class Factory:
#     a = 12 #attribute

#     def hello(self):
#         print("How are yiy??")

#     print("hi")    

# obj = Factory()

# print(obj.a)
