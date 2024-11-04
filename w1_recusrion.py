# Recursion in Python
# A function calls itself is recursion 

def factorial(n):
  if n == 1: return 1 
  return n * factorial(n-1)
  
print(factorial(4))

# Decorators in Python 
# Decorators are declared just before the function definition 
# Decorators accepts functions as a parameter and performs its tasks

print("\nDecorators ")

def logTime(func):
    def wrapper():
        print("before")
        val = func()
        print("After")
        return val
    return wrapper


@logTime 
def hello():
   print("Hello !")

hello()


# DocStrings in Python 
# A Python docstring is a string used to document a Python module, class, function or method, so programmers can understand what it does without having to read the details of the implementation. Also, it is a common practice to generate online (html) documentation automatically from docstrings.

""" Alcohol Module 

This Module does .. list of beers and provides the following classes

-Beer

""" 

class Alcohol():
  """ A class representing a Alcohol"""
  def __init__(self, name, type):
      """Initialize a new alcohol type"""
      self.name = name 
      self.type = type

  def taste(self):
    """ Find the taste of the Alchohol """
    print(" Bitter ! ")

print(help(Alcohol))


# Annotations in Python 
# Python annotations provide additional information on variables or functions. In particular, they can be used to improve code readability, or to detect errors via an IDE or third-party libraries.


def increment(n: int) -> int:
    return n+1

count: int = 1 