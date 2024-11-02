
#  Contains Basi Operations on Tuples , Dictionaries , Sets



# Tuples Tutorials
# Tuples are immutable DataStrcutures in Python
# Once created Tuples cannot be modified
# We cannot add or remove items in Tuples

# Creating a new Tuple
from typing import Union


print("\n Working with Tuples ")
names = ("Rahul", "Sanjay", "Gopi", "Uday")
#Navigating through tuples
names[-1]  #  access the last item of a tuple
names.index("Uday")
len(names)
print("Rahul" in names)
print(sorted(names))
newTuple = names + ("Naveen", "Amit")
print("\n")


# Dictionaries in python
# Key value pairs DataStrcuture

# Creating a new Dictionary

print("\n Working with Dictionaries ")
persons = {"name": "Rahul", "Age": 29, "color": "Red"}

persons["Age"] = 35

persons["favourite food"] = "Meat"

del persons["color"]

print(persons.get("name"))

print(persons.pop("name"))

print("color " in persons)

print(list(persons.keys()))

print(list(persons.values()))

print(list(persons.items()))


# Sets in python
# Sets are not ordered and are mutable
# Set cannot have duplicated items 
# creating a set

print("\n Working with sets ")

set1 = {"Rahul" , "Uday" , "Sanjay" , "Gopi" , "Naveen"}
set2 = {"Rahul"} 

# Intersection of two sets
intersect = set1 & set2 
print("Intersect of Sets : " , intersect)

# mod and union of two sets
uni = set1 | set2
print("Union of Sets : " , uni)

mod = set1 - set2
print("Mod of Sets : " , mod)

grt = set1 > set2
print("Greater of Sets : " , grt)

print(list(set1))
print("Rahul" in set1)
