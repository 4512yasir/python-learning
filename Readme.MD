###  Python

python is an interprated object oriented programming language(OOP)

# key vocabularies
1. interpreter - is a program that executes other program 
2. python shell - is an interactive interpreter that can be accessed from command line
3. Data types - are specific kind of data 
4. Exception - is a type of error that can predict and handle without causing a crash 
5. scope - is a specific program where specific variable can be called



##  Variables 
variables are container used to store data types

# Rules of naming a variable
1. Start with a letter or an underscore(not a number)
2. No space in a variable 
    # NB: when writting a two word variable  (user name) we should use snake_case (user_name)
3. use descriptive name when naming a variable like (user_name ="yasir" rather than x = "yasir")

# syntax of variables
    
    variable_name = "variable_value"


# how to declare a variable
this is how variables are supposed to be declared 
   name = "yasir"
   age = 24



## DATA TYPES
Data types classify values stored in variables.

# Python has 9 core data types:

# 1. string (str)
string is a text data that is contained in a qoatation

# example of string 
name = "yasir"
# explanatation
name is a variable 
"yasir" is a string

# 2. interger (int)
interger are numbers that are whole.

# example of interger
age = 20
# explanatation
age is a variable 
20 is an interger

# 3. float (float)
Float is a number with decimal 

# example of float 
height = 5.11
# explanatation
height is a variable
5.11 is a float

# 4. Boolean (bool)
Boolean is true or false data type
this data type the output is always true/false

# example
is_kenyan = True
# explanation
is_kenyan is a variable
True is a boolean

# 5. Lists 
lists is ordered and changeable data of items
you can change data of Lists

# example
marks = [30,40,60,80]
# explanatation
marks is a variable 
[30,40,60,80] is lists 

#  6.Tuple (tuple)
tuple is a ordered and unchangable data items
you cannot change data of tuple 

# example
cooardinates = (10,20)
# explanatation
cooardinates is a variable
(10,20) is tuple

# 7. set
is a unique unordered list of data

# example

unique ={10,20,30,40,50}
# explanatation
unique is a  variable
{10,20,30,40,50} is a set

# 8. dictionary(dict)
dictionary is a key -value pair 

# example
user= {
    "name":"Yasir"
}
# explanatation
user is a variable
 {"name":"Yasir"}  is a dictionary
 name is a key
 yasir is a value

 # 9. None
 None is nothing

 # example
 result = None
 # expalanation
 result is a variable
 None is a None data type

# Data types abbreviation
1. string (str)
2. integer (int)
3. float (float)
4. boolean (bool)
5. Lists (list)
6. Tuple (tuple)
7. set (set)
8. Dictionary (dict)
9. None (None)

# Note 
type () is used to check the type of data type   


# Functions
a function is a block of organized, reusable code that performs a specific task
# syntax of a function
def function_Name():
    // logic here 

function_Name() // invoking the function

# example
# function with  arguments
def add(a,b):
    return a + b
    
add(3,7)

# function with default parameter
def add(a,b=3):
    return a + b
add(3,5)
add(4)

# function with no argument
def greet():
   print("Hello World!")
greet()



# Variable Scope
Scope refers to where a variable is accessible in your program.

# Types of scope
1. Global scope -> is any Variable created outside a function and can be used by any function
    # example
    name = "YAsir"
    def greet():
        print(f"Hello,{name}")
    greet()
2. Local scope -> is any variable created inside a function (including parameters) and can only be used to the function that is created inside.
     # example
     def greet():
        name = "YASIR"
        print(f"Hello,{name}")
    greet()


# Note
To change a global a value of a global variable/scope  from a local scope  we need to use  the global  keyword
   # example
   change ="Keyword"
   def global_keyword():
      global change
      change = "global keyword"
      print(f"this is a {change}")
    global_keyword() 


# What is Set
Set is an unordered collection of unique items

Set can be mutated but contains immutable (hashable) elements

# e.g
my_set = {1,2,3,4}

# key characteristics
1. No duplicate elements
      
   # e.g
   my_set = {1,2,2,3,4}

2. unordered list 

   # e.g
   my_set = {2,1,4,6,3}

3. Element must be immutable e.g numbers , strings and tuple
  
   # e.g
   my_set = {"YASIR","AHMED","MOHAMMED"}
   my_tuple = tuple(my_set)

# creating a set

1. using curly braces 
     set_1 ={1,2,3}
2. using set() constructor
     set_2 =set([1,2,3,4,5])
3. Empty set must have set() constructor
      set_3 =set()

     # set methods
     Rule to Remember:
     “Sets are objects, and methods are called with set.method()"

1. Adding element to the set

   s = {1,2,3}
   s.add(4)

2. Removing element
     1. error if not found
        
        s = {1,2,3}
        s.remove(2)
     2. no error if not found  
       
         s = {1,2,3}
         s.discard(3)
3. Remove all element
   
      s = {1,2,3}
      s.clear()

4. Shallow copy - creates a new set with the same elements.
 

     s ={1,2,3,4}
     duplicate = s.copy()

5. combining set
    
    s ={1,2,3,4}
    p = {3,4,5}
    q =s.union(p)

6. common element - filter common element in two sets
 
    s ={1,2,3,4}
    p = {3,4,5}
    q = s.intersection(p)

7. Subtract set - filter element that are not the same in two sets
 
     s ={1,2,3,4}
     p = {3,4,5}
     e = s.difference(p)

8. check if subset - A subset is a set whose all elements are also present in another set.

     A = {"YASIR", "AHMED"}
     B = {"YASIR", "AHMED", "MOHAMMED"}

     print(A.issubset(B))  # True
     print(B.issubset(A))  # False

9. check if superset - A superset is a set that contains all elements of another set.

        A = {"YASIR", "AHMED", "MOHAMMED"}
        B = {"YASIR", "AHMED"}

        print(A.issuperset(B))  # True
        print(B.issuperset(A))  # False
10. removing random element in a set
          s ={1,2,4,3}
          s.pop()  # removes random elemenent
11. add multiple elements in a set
  
       s.update([5, 6, 7])

# note 
subset and superset are not the same

Subset = “Is this set inside the other?”

Superset = “Does this set contain the other?”


# note 
In a set, the order of printed elements is random and can change each time you run the program.


       
  