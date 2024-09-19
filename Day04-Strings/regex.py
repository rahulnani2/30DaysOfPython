import re 

text = "apple, banana, orange, grape"
pattern = r","
split_result = re.split(pattern,text)
print("Split result : ", split_result)

text1 = "The quick brown fox"
pattern1 = r"brown"

match = re.match(pattern1, text)
if match:
    print("Match Found : ", match.group())
else:
    print("No Match")    

text2 = "Python is a Interpreter language"
pattern2 = r"Python"
search = re.search(pattern2,text2)
if search:
    print("Pattern found :" , search.group())
else :
    print("Match Not found")

text3 = "The quick brown fox jumps over lazy black dog "
patter3= r"black"
replacement = "white"
new_text = re.sub(patter3, replacement, text3)
print("modified text :" , new_text)