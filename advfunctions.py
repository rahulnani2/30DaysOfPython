from functools import reduce
# lambda Map reduce and Filter functions in pyton

# Lambda Functions 
lambda num : num * 2 

multiply = lambda a, b: a * b
print(multiply(2,4))

# Using map and Lambda together
numbers = [1,2,3]
double = lambda a : a * 2 
result = map(double, numbers)
print("\n" , list(result) )

# The above lambda function can be written as 
numbers = [1,2,3,4]
result = map(lambda a : a*2 , numbers)
print("\n" , list(result))


# map(), filter() and reduce()

# map()
numbers = [1,2,3]

def double(a):
  return a * 2

result = map(double, numbers)
print("\n" , list(result) )

# fiter()
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def checkEven(a):
    return a % 2 == 0

result = filter(checkEven , numbers)
print("\n" , list(result))

# the above function can be written with lambda and filter 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result = filter(lambda a : a % 2 == 0 , numbers)
print("\n" , list(result))

# reduce() --> 
expenses = [("Dinner" , 80), ("Car Expenses" , 800)]
sum = reduce(lambda a ,b :a[1] + b[1], expenses)
print("\n" , sum )