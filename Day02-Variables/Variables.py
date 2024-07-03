#  An Integer Assignment
age = 40 
# A floating point 
salary = 112.5
# String assignment 
name= "Daemon"
print( name , age, salary)

# Assign values to multiple variables 
a=b=c=10
print(a,b,c)

# assign Different values to multiple variables 
a,b,c= 10,20.5,"language"
print(a,b,c)

#Python + operator
# add a value if it is a number 
# Concatenate if it is a string 
a = 10 
b = 30 
print(a+b)
a = 'number'
b = 'one' 
print(a + b)

# DataTypeCasting
#INT to Float 
numsInt = 10 
numFloat = float(numsInt)
print(numFloat)

#Float to int 
numsFloat = 10.12
numsInt = int(numFloat)
print(numsInt)

#int to STR 
numsInt = 10 
valString= str(numsInt)
print(valString)

#String to List
strlist = 'Python language'
listval = list(strlist)
print(listval)



# Global and local Variables 
def f():
    s = "Python is a Interpreted language"
    print(s)
f()    

def l():
    print(s)
#global scope 
s="Day02 of python"
l()   
#Global KeyWord
x = 15 
def change():
    global x  
    x = x+5
    print("Value of x inside a function : ", x)
change()
print("Value of x outside a function : " , x)

#Creating Objects in Python 
class CSStudent:
    #Class variable
    stream='cse'
    # The init method or contructor 
    def __init__(self,roll):
        #Instance variable 
        self.roll = roll 
# Objects of Student Class 
a=CSStudent(47)
b=CSStudent(48)
print(a.stream , a.roll) 
print(b.stream , b.roll)

# Class variables can be accessed using Class name also 
print(CSStudent.stream)









