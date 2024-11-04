# Exceptions in python 
# Syntax for TRY and EXCEPT in Python 

#try:
  # Some lines of code 
#except EOFError:
  # Handler <Error1 >
#except TypeError:
  # Handler <Error 2>
#else:
  # No exceptions were raised, the code ran successfully 
#finally:
 # Do somethin in any case

try:
  result = 2/0
except ZeroDivisionError: 
  print("Cannot be divided by zero")
finally:
  result = 1

print("\n",result)

# Raise an Exception 

try:
  raise Exception("Stack OverFlow Error")
except Exception as error:
  print("\n",error)


class NameNotFoundException(Exception):
    print("\n Beer Name not found")
    pass 

try:
  raise NameNotFoundException()
except NameNotFoundException:
  print("\n Name not found !")


