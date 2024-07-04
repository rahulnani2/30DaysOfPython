#Day03 - 30DaysOfPython 

# Identity Operator 
i , j  = 10 , 20 
k =i  
print(i is not j )
print(i is k) 
#MemberShip Operator 
x = 24 
y = 20 
list = [10,20,30,40,50]
if (x not in list):
    print("x is not present in list")
else:
    print("x is present in list")
if (y in list):
    print("Y is present in list")
else:
    print("Y is not present in list ")

#Ternary Operator 
a = 10 ; b = 20 
max = a if a > b else b 
print(max)

#Write a script that prompts the user to enter base and height
# of the triangle and calculate an area of this triangle 
# (area = 0.5 x b x h).
def calculateTriangleArea(base,height):
    return 0.5 * base * height 
base = float(input("Enter base value  \n"))
height = float(input("Enter height value \n"))
area = calculateTriangleArea(base,height)
print(f"Area of a triangle is : {area}")

#Write a script that prompts the user to enter hours and 
# rate per hour. Calculate pay of the person?
def caluculatePay(hours, rate):
    return hours * rate
hours=int(input("Enter Hours : " )) 
pay=int(input("Enter pay : " ))
earning= caluculatePay(hours , pay)
print(f"Your weekly earning : {earning}") 

#Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
    
















