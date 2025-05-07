# creating basic set
my_set = {1, 2, 3, 4, 5}
# printing to the terminal
print(my_set) 


# adding elements to a set
# method 1
# adding an element using add() method
my_set.add(7)


#method 2
# adding multiple elements using update() method
my_set.update([8, 9, 10])

print(my_set)





# removing elements from a set
#method 1
# removing an element using remove() method
my_set.remove(2)
# Note: If the element is not found, remove() will raise a KeyError


# method 2

# removing an element using discard() method
my_set.discard(3)
# Note: If the element is not found, discard() will not raise an error


# method 3
# removing an element using pop() method (removing a random element)
my_set.pop()

# method 4
# removing an element using clear() method (removing all elements)
my_set.clear()

print(my_set)

# subset and superset
A = {1, 2}
B = {1, 2, 3}

# Subset: Is A inside B?
print(A.issubset(B))  # True

# Superset: Does B contain A?
print(B.issuperset(A))  # True

# set with different data types
mixed_set = {1, "hello", 3.14, True, (2, 3)}
print(mixed_set)

# creating a shallow copy of a set
s ={1, 2, 3}
s.copy()  # creates a shallow copy of the set

# set operations
# union
A = {1, 2, 3}
B = {3, 4, 5}
# union of A and B
C = A.union(B)
print("Union:", C)  

# intersection
# intersection of A and B
D = A.intersection(B)
print("Intersection:", D)

# difference    
s ={1,2,3,4}
p = {3,4,5}
e = s.difference(p)
print("Difference:", e)  


# symmetric difference
# symmetric difference of A and B
F = A.symmetric_difference(B)
print("Symmetric Difference:", F)
# symmetric difference update
A.symmetric_difference_update(B)
print("Symmetric Difference Update:", A)  # A is now {1, 2, 4, 5}
# set comprehension
# creating a set of squares of numbers from 1 to 5
squares = {x**2 for x in range(1, 6)}   
print("Set Comprehension:", squares)  # {1, 4, 9, 16, 25}
# frozen set
# creating a frozen set
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen Set:", frozen_set)  # frozenset({1, 2, 3, 4, 5})
# frozen set with different data types
frozen_set_mixed = frozenset([1, "hello", 3.14, True, (2, 3)])
print("Frozen Set with Mixed Data Types:", frozen_set_mixed)  # frozenset({1, 'hello', 3.14, True, (2, 3)})

#len()
#len of a set -
s = {1, 2, 3, 4, 5}
print("Length of set:", len(s))  # 5