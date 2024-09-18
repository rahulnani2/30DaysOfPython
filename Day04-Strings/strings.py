
# Lenght of the String 

name = "Rahul Dondeti"
print("Length of the name : " , len(name))

# Lower and Upper case
print("Upper case :" , name.upper())
print("Lower case :" , name.lower())

# Replace Fucntion
text = "Learning python programmin language"
print(text.replace("programmin", "programming"))

# Split Function 
arn = "arn:aws:iam:123456789012:user/johndoe"
print( arn.split("/")[1] )

# Strip Fucntion 
text2 = "  Some random spaces in text    "
print("Stripped text ", text2.strip())

# SUbstring function 
text3 = "Canada is a lonely country"
substring = "Lonely"
if substring in text3:
    print(substring, "found in the text")
else:
    print(substring, "Not found in the text")
