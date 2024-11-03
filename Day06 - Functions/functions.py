#Python Function Tutorials

#  Function 1
print("\n Function1 ")


def hello(name, age):
  print(" Hello ! " + name + " You are " + str(age) + " old")


hello(" Rahul", 29)

# Function 2
# Chagnes made inside the function, The scope of the value variable is within
#function
print("\n Function2 ")


def change(value):
  value = 2


value = 1
change(value)
print(value)

# Function 3
# If we change a value of a mutable variables like dictoinary the change is visible outside the function
print("\n Function3 ")


def changevar(value1):
  value1["name"] = "Sid"


value1 = {"name": "milky"}
changevar(value1)
print(value1)

# Function 4
# Return statements in Functions
print("\n Function4 ")


def hello(name):
  if not name:
    return
  print("Hello ! " + name)


hello("Rahul")

# Function 5
# Variable Scope
print("\n Function5 ")
age = 8  # Global Variable


def test():
  ageValue = 10  # local variable Scope is within the function


# Function 6
# Nested Functions - A function within a fucntion,
# Nested function is Visible only to its  parent function
print("\n Function6 ")
def talk(phrase):
  def say(word):
      print(word)
  
  words = phrase.split(' ') 
  for word in words:
    say(word)

talk("I am going to buy chicken")

#Fucntion 7
# nonlocal key word
print("\n Function7 ")

def count():
    count =0 

    def increment():
        nonlocal count 
        count = count + 1
        print(count)

    increment()
count()


#Fucntion 8
# Closures in python , We can call the nested function eventhough the execution of main funciton is ended 

print("/n Function 8 ")
def counter():
    count = 0 

    def increment():
      nonlocal count
      count = count + 1 
      return count
    return increment


increment = counter()
print(increment()) # 1
print(increment()) # 2
print(increment()) # 3 