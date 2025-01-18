# print("Aman Gautam\n")
# print("Invertis University\n")
# print("BC2024218\n")
# print(30+20)
# print("\n")

# name = "aman gautam"
# age = 20
#  = False
# aa = None
# marks = 79.22

# print("my name is :",name)
# print("my age is :",age)
# print("my marks is :",marks)
# print(type(name))
# print(type(age))
# print(type(marks))
# print(type(aa))
# print(type(old))

# print("\n")


# a = 10
# b = 20
# sum = a+b
# sub = a-b
# mul = a*b
# div = a/b
# print(sum, sub, mul, div)
# print("\t")
# print("ENter the first number :")


# a = 2
# b = 3
# c = 2.0
# print(a+b*c)

# name = input("what is your name :- ")   #(input) is a using for entered only string value from user  
# print("your name is :- ",name)         #output result for enterd value from users

# age = int(input("what is your age:- " ))     #(int) is using for enter only integer value from users
# print("your age are :-",age)                  #output result for enterd value from users

# marks = float(input("what is your marks :- "))         #(float) is using for enter only floating value from users
# print("your marks is:-",marks)                         #output result for enterd value from users

# print("\n")                   # it is using for line break;

# print("your name is :- ",name)
# print("your age are :-",age)
# print("your marks is:-",marks)

# first = int(input("Enter the first number :-"))

# sec = int(input("Enter the second number :-"))

# sum = first + sec 
# sub = first - sec
# mul = first * sec

# print("Total Sum :- ", sum)
# print("Total substraction :-\n ", sub)
# print("Total multiplication :- \n", mul)
# print(" THANK YOUHH! \n")

# print("HELLO WORLD!")

# light = input("Enter any light colour :- ")
# if(light == "red"):
#     print("STOP 🔴 ")

# elif(light == "yellow"):
#     print("LOOK AHEAD 🟡 ")

# elif(light == "green"):
#     print("GO 🟢 ")

# else:
#     print("the light is broken")

# print("THANK YOUHH!")



""" student grade marks """

# marks = int(input("Enter your marks :- "))
# if(marks >=90):
#     print("Grade 'A'")

# elif(marks >= 80 and marks<=70):
#     print("Grade 'B'")

# elif(marks >= 70 and marks <= 60):
#     print("Grade 'C'")

# else:
#     print("Grade 'D'")

# print("THANK YOUHH!")




""" here this is single line condiional statement """

# food = input("Enter food :- ")
# print("woww sweet") if food == "cake" and food == "laddu" or food == "jalebi" else print("no sweet")


"""HERE CEVER IF TERNARY OPERATOR"""

# age = int(input("your age :- "))
# vote = ("yes","no") [age<18]
# print(vote)


""" type conversion"""

# a = 5
# b = 3.25
# sum = a + b
# print(sum)


""" type casting"""

# a = 5.14
# a = str(a)
# print(type(a))

# name = input()
# print("Welcome : ",name)

# age = int(input("Enter the age :- "))
# print("your age ",age)

""" practice question create CALCULATOR """

# first = int(input("Enter the first number :- "))
# sec = int(input("Enter the second number :- "))
# total = first + sec
# print("total sum = ", total)

""" practice quesion to write a programm to input sideos a square & print its area"""

# size = int(input("Enter the area size :- "))
# area = size * size 
# print("the area aqaure is :" , area)

"""practice questions WAP to int 2 floating point number & print their average """

# first = float(input("Enter the first number :- " ))
# second = float(input("Enter the second number :- "))
# average = (first + second) / 2
# print("the average is : ",average)

"""WAP greter thean equal too"""

# a = int(input("Enter the num1 :- " ))
# b = int(input("Enter the num2 :- " ))

# if(a>=b):
#     print("true")

# else:
#     print("false")


                              #or
                            
# a = 10
# b = 20
# print(a>=b)

"""Addition STRING amd count lenghth"""

# str = "aman"
# str1 = "gautam"
# total = str + str1
# print(total)
# print(len(total))

"""WAP to inputuserfirst name and frint its lenghth """

# name = input("Enter the your name :- ")
# print(len(name))

""" nesting (if) statement """

# age = int(input("Enter your age :-" ))
# if(age >= 18):
#     if(age >= 80):
#         print("you can not drive")
#     else:
#         print("you can drive")
# else:
#     print("you can not drive")

""" WAP to check if a number by enterd user is odd or even """
# num = int(input("Enter the number :- "))
# if(num % 2 == 0):
#     print("the number is even")

# else:
#     print("the number is odd")

""" WAP to find largest number in which 3 number """

# num1 = int(input("Enter the first number :-"))
# num2 = int(input("Enter the second number :- "))
# num3 = int(input("Enter the third number :- "))

# if(num1 >= num2 and num1 >= num3):
#     print("the first number is greater ",num1)

# elif(num2 >= num3):
#     print("the second number is greater",num2)

# else:
#     print("the third number is greater",num3)

"""WAP to check multiple of 7 or not"""

# table = int(input("Enter the number :- "))
# if(table % 7 == 0):
#     print("it is divisible by 7")

# else:
#     print("it is not divisible by 7")

"""WAP to ask the user to enter names of thier 3 fav movies & stores them in the list"""

# str1 = input("Enter the first movie name :- ")
# str2 = input("Enter the second movie name :- ")
# str3 = input("Enter the thirs movie name :- ")

# list = [str1 , str2 , str3]
# print(list)

#                                       Or

# movies = []

# mov1 = input("Enter the first movies name :- ")
# mov2 = input("Enter the second movies name :- ")
# mov3 = input("Enter the third movies name :- ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

"""WAP to find meter square"""

# print("WELCOME!!")
# lenghth1 = float(input("Enter lenght :- "))
# lenghth2 = float(input("Enter sec lenght :- "))
# width1 = float(input("ENter width :- "))
# width2 = float(input("Enter width sec side :- "))

# area1 = lenghth1 * width1
# area2 = width2 * lenghth2

# total = area1 + area2

# print("The meter square are :- ",total)

# print("THANK YOUHH !")

"""WAP to find grade "A" with the help of tuple""" 

# grade = 'A','B','C','A','A','B'
# print(grade.count('A'))

"""store word meaning in a python"""

# meaning = {
#     "table" : ["a peace of furniture" , "list of factor and figure"],
#     "cat" : "a small animal"
# }
# print(meaning)

"""you are given list of subject for student, asssume one classroom is required for 1 subject. 
how many classroom are needed by all student"""

# subject = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(subject.union())
# print(len(subject.union()))

"""WAP to enter marks of 3 subject from the user and store them in a dictionary. start with anempty dictionary & add one by one.
use subject name as key & marks as value"""

# marks = {

# }
# phy = int(input("Enter the marks of physics :- "))
# che = int(input("Enter the marks of chemistry:- "))
# bio = int(input("Enter the marks of biology :- "))

# marks.update({"physics" : phy })
# marks.update({"chemistry" : che })
# marks.update({"biology" : bio})
# print(marks)




"""Figure out a way store 9 & 9.0 as seprate valuein the sets you can take built in data - types"""
# value = {
#    ("int" , 9),
#     ("float" , 9.0)
# }
# print(value)




""" About while loops """

i =1
while i <= 5:
    print("hello")
    i +=1


