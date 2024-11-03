# Loops
# While and For Loops
count = 1
while count <= 10 :
  print("Value of count = ", count)
  count = count + 1 

# For Loop 
print("\n For loop ") 
items = [1,2,3,4,5,6,7,8]
for index, item in enumerate(items):
  print(index,item)

# Break and Continue Key words 
print("\n Break and Continue Key words")
items=["Budvieser", "Heinken" , "Molson" , "RedTape" , "Corona"] 
for item in items:
  if item == "Molson":
    continue 
  print(item)

print("\n")
items=["Budvieser", "Heinken" , "Molson" , "RedTape" , "Corona"] 
for item in items:
  if item == "Molson":
    break 
  print(item)