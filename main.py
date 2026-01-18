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
# a = 10; 
# sher = "Keshav"   #we can not do 2sher means number phele nhi use krne 
# # no use space between variables like (SHE R), dont use special character like @sher
# SheryiansSchool = "students" #pascal case
# sheryiansSchool = "students" #camel  case
# sheryians_school = "students" #snake case

#                  #DATATYPE
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

# # 01. accept two numbers and print the gratest btw them
# a = int(input("Enter first number: "))    
# b = int(input("Enter Second number: "))    

# if a>b:
#     print(f"{a} is grater than {b}")
# elif a<b:
#     print(f"{b} is grater than {a}")    
# else:
#     print(f"{b} is equals to {a}")   

# 02. accept the gender from the user as char and print the respective greeting message Ex- Good Morning Sir/Mam

# gen = input("Enter your gender as character(M or F): ")

# if gen == 'M' or gen == 'm':
#     print("Good Morning Sir")
# elif gen == 'F'or gen == 'f':
#       print("Good Morning Mam")   
# else:
#     print("Unidentified gender")   




#LOOPS
# for -> works on basis of numbers it needs number 10 baar print kro ya phir 100 baar, 
# while -> works on condition like do until number becomes 100, 
# do-while

#FOR Loop
# a = range(1, 20, 1)   #arnge(start, end, kine number chhodh chhodh ke)

# for i in a:
#     print(i)

     #AUR

# for i in range(1, 21, 1):
#     print(i)

#     #AUR

# for i in range(21):         #end dena jaruri hai
#     print(i)    

# reverse print from 16 to 1

for i in range(16, 0, -1):    #(start, end, kitna number peeche jaaye)
    print(i)















    



















