import math
from math import sqrt 
import os
import random 
import json
# Classes in Python 

class Alcohol:
    def sense(self):
        print("Gives kick.....")
      
class Beer(Alcohol):
  # Constructor for the class Beer 
    def __init__(self, name, make):
      self.name = name
      self.make = make

    def taste(self):
       return "Bitter !" 

corona = Beer("Corona" , "Spirits")
print(corona.name)
print(corona.make)
print(corona.taste())
corona.sense()


# Modules in Python 
# Every python file is Module 
# Python Standard Library 
# math for math utilities 
# re for regular expressions 
# json to work with json 
# datetime to work with dates
# sqlite3 to use SQLite
# os fro Operating system utilites
# random for random number generations 
# statisitcs for statistics utilites
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLS 
