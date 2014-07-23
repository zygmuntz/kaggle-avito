#!/usr/bin/env python

"a demo of how to load attribs"

import sys
import csv
import json

input_file = sys.argv[1]

reader = csv.DictReader( open( input_file, 'rb' ), delimiter = '\t' )

for line in reader:	
	if line['attrs'] != '':
		try:	
			attrs = json.loads( line['attrs'] )
			# you might need to .encode( 'utf-8' )
		except ValueError:	
			try:
				attrs = json.loads( line['attrs'].replace( '/"', r'\"' ))
				# you might need to .encode( 'utf-8' )
			except ValueError:
				print "trying eval()..."
				try: 
					attrs = eval( line['attrs'] )
					# no need to encode( 'utf-8' )
				except ValueError:
					print line['attrs']
					
					