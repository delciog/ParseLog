import sys
import re

infile = sys.argv[1]

with open(infile) as inf:
    for line in inf:
        result = re.findall('id\=\w+[^\s]+', line) # get id
        result += " " # separator space
        result += re.findall('"([^"]*)"', line) # get string between quotes
        if len(result) > 1: # if it's not just the separtator space, then print it
            print(result)
