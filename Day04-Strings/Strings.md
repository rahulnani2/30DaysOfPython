Day04-30DaysOfPython 

Strings 
Data under single,double or triple quote are strings. There are different string methods and built-in functions to deal with string data types.

letter = 'P'                # A string could be a single character or a bunch of texts
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"

Multiline string is created by using triple single (''') or triple double ("""). See the example below 
multiline_string= ''' Day04 of the 30 days python challenge
                      Day04 is for learning strings '''
multiline_string= """ Day04 of the 30 days python challenge
                      Day04 is for learning strings """
print(multiline_string)

String Concatenation 
Two or more strings can be concatenated by using + operator in Python 
first_name = "Peter"
last_name = "Parker"
space = " "
full_name = first_name + space + last_name

Escape Sequence in Python 
In python \ followed by a character is an escape character in escape sequence 
> \n : new line
> \t : tab (8 spaces)
> \\ : Back Slash
> \' : Single quote(')
> \" : Double Quote (")

print('This is a backslash symbol (\\)') --> This is a backslash symbol (\)
print('In every programming language it starts with \" Hello World ! \" ') -> In every programming language it starts with " Hello World !" 

























