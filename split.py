''' 
split file lines randomly to divide the given data
into cross validation and training data

Usage:
split.py <input filename> <output filename 1> <output filename 2> <headers> [<probability that a line goes to output file 1, default = 0.9>]

input filename
output filename 1
output filename 2
headers = 1 implies the input data has headers in it.
probability a row randomly goes into the first output file, default = 0.9
'''

import csv
import sys
import random

try:
	P = float(sys.argv[5])
except IndexError:
	P = 0.9
else:
	pass
finally:
	pass

input_file = sys.argv[1]
output_file1 = sys.argv[2]
output_file2 = sys.argv[3]
headers = sys.argv[4]
input_handle = open(input_file)
output_1_handle = open(output_file1, 'wb')
output_2_handle = open(output_file2, 'wb')

reader = csv.reader(input_handle)
writer1 = csv.writer(output_1_handle)
writer2 = csv.writer(output_2_handle)

if headers == "1":
	columns = reader.next()

for line in reader:
	r = random.random()
	if r > P:
		writer2.writerow(line)
	else:
		writer1.writerow(line)