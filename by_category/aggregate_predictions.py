#!/usr/bin/env python

'produce a solution file for kaggle from category predictions files'

import os
import sys
import numpy as np
from glob import glob

input_dir = sys.argv[1]
output_file = sys.argv[2]

print "loading predictions..."

os.chdir( input_dir )
files = glob( '*.txt' )

all_p = np.empty(( 0, 2 ))
for f in files:
	print f
	p = np.loadtxt( f )
	all_p = np.vstack(( all_p, p ))
	
# for category 3, a missing example prediction from p_kaggle_no_holdout	
all_p = np.vstack(( all_p, np.array(( -11.858253, 89655507 ))))	

assert( all_p.shape[0] == 1351242 )

# sort by prediction and reverse
i = np.argsort( all_p[:,0] )[::-1]

# ids of most certain predictions
p_ids = all_p[i,1].astype ( int )

print "writing..."

np.savetxt( output_file, p_ids, fmt = '%d', header = 'Id', comments = '' )


