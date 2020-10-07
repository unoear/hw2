# Antonio Alvarez
#1796498
import csv

inputfile = input()
count = {}

with open(inputfile, 'r') as csvfile:
 csvfile = csv.reader(csvfile)
 for line in csvfile:
   for words in line:
     if words not in count.keys():
       count[words] = 1
     else:
         count[words] + 1
   print(count)
