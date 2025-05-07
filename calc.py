# - this is a comment
# variables
name = "Yasir"   # variable storing a string
age = 20  # variable storing an integer
is_student = True   # variable storing a boolean
# data types
# string
name = "Yasir"
# integer
age = 20
# boolean
is_student = True
#float
height = 5.9 # variable storing a float
# list
fruits = ["apple", "banana", "cherry"] # variable storing a list
# printing to the terminal
print("Name:", name) # print the name
print("Age:", age) # print the age
print("Is Student:", is_student) # print the boolean value
print("Hello, World!") # print a greeting message

# name = input("What is your name? ")
# age = int(input("How old are you? "))

# print("Hello", name , "!")
# print("You are", age, "years old.")




# string
name = "Yasir"
# integer
age = 20
# boolean
is_student = True
# float
height = 5.9 
#list
members= ["Yasir", "Ali", "Ahmed"]
# dictionary
user_member ={
    "name":"Yasir",
    "age" : 20,
    "Location" : "Nairobi"
}
#None
reult = None
# tuple
coordinates = (10.0, 20.0)
# set       
unique_numbers = {1, 2, 3, 4, 5}
# printing to the terminal
print(type(name)) # print the type of the variable
print(type(age))
print(type(is_student))
print(type(height))
print(type(members))
print(type(user_member))
print(type(reult))
print(type(coordinates))
print(type(unique_numbers))


# functions
# first way to define a function
def greet():
    print("Hello, World!") # function to print a greeting message
greet() # call the function to print the greeting message
# second way to define a function
def add_num():
    num_1 = 5
    num_2 = 10
    result = num_1 + num_2
    print("The sum is:", result)
add_num() # call the function to add numbers
# third way to define a function
def add_numbers(num_1, num_2):
    result = num_1 + num_2
    return result
# call the function to add numbers
result = add_numbers(5, 10)
print("The sum is:", result) # print the result of the addition


# scope 
# global scope 
access = "every function has acces to me"

def global_scope():
    print(f"this is a global scope variable: {access}")

global_scope()


# local scope
def local_scope():
    access ="only this function has access to me"
    print(f"this is local scope:{access}")
local_scope()

# global keyword
change = "I am a global variable"
 
def global_keyword():
      global change
      change = "i am a global keyword variable"
      print(f"this is a global keyword variable: {change}")

global_keyword()



# comparison operators

x = 10
y = 5

print(x > y)  # Greater than
print(x != y) # Not equal to
print(x == y) # Equal to
print(x <= y) # Less than or equal to
print(x >= y) # Greater than or equal to
print(x < y)  # Less than 


# logical operators
# and operator - if both conditions are true
maths = 80
science = 75
print(maths > 70 and science  > 70) # true 
# or operator - if at least one condition is true
user_name = "Yasir"
password = "1234"
print(user_name == "Yasir" or password == "Yasir") # true
# not operator 
door_status = "locked"
print(not(door_status == "locked")) # false
# combined operators
age >= 18 
have_id = "Yes"
print(age >= 18 and have_id == "Yes") # true
# tricky not operator
light_status = "off"
print(not(light_status == "on")) # true



# conditional statements
# if statement,elif and else statement
age =13
if age <= 12:
    print("You are under 12 years old.")
elif age >= 12 and age <= 17:
    print("You are a teenager.")
else:
    print("You are an adult.")
# nested statements
age =18
citizen = "Kenyan"
if age >= 18:
    print("You are eligible to vote")
    if citizen == "Kenyan":
        print("You are a eligible to vote in Kenya")
    else:
        print("You are not eligible to vote in Kenya")
else:
    print("You are not eligible to vote yet")


membership_status ="Member"
age = 10
if age >= 60:
    print("You are eligible for senior citizen discount")
    if membership_status == "Member":
        print("You are eligible for member discount")
    else:
        print("You are eligible senior discount")
elif age >= 18 and age < 60:
    print("You are eligible for adult discount")
    if membership_status == "Member":
        print("You are eligible for adult member discount")
    else:
        print("You are eligible for regular adult discount")
else:
    print("YOU are young for any discount")


  
