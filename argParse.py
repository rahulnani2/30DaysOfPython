# Accepting arguments from command line 
import sys
import argparse

parser = argparse.ArgumentParser(
    description = 'This program prints names of the beer'
)

parser.add_argument('-b' , '--beer', metavar='beer', required=True, choices={'Corona' , 'Molson' , 'Heinekin' , 'Budvieser' , 'RedTape'}, help ='the beer to search for' )

args = parser.parse_args()
print(args.beer)