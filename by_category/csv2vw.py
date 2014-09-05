#!/usr/bin/env python

"convert data to VW format"

import csv
import sys
import _csv
from construct_line import *

input_file = sys.argv[1]
output_file = sys.argv[2]

print_counter_every = 1e5

reader = csv.DictReader( open( input_file, 'rb' ))
o_f = open( output_file, 'wb' )

n = 0
while True:
	try:
		line = reader.next()
	except StopIteration:
		break
	except _csv.Error:
		continue
	
	new_line = construct_line( line )
	if not new_line:
		continue
	
	o_f.write( new_line )
	
	n += 1
	if n % print_counter_every == 0:
		print n	
	