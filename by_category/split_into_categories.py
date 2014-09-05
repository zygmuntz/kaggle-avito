#!/usr/bin/env python

"split a data file into separate files for each category"

import sys
import pandas as pd

input_file = sys.argv[1]

data = pd.read_csv( input_file, delimiter = '\t' )

for c, category in enumerate( sorted( data.category.unique())):
	print category
	i = data.category == category
	data[i].to_csv( "{:d}.csv".format( c ), index = False )
