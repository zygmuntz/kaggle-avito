#!/usr/bin/env python

'produce a solution file for kaggle'

import sys
import numpy as np

p_file = sys.argv[1]
output_file = sys.argv[2]

# load and prepare predictions

print "loading predictions..."

p = np.loadtxt( p_file )

# sort by prediction and reverse
i = np.argsort( p[:,0] )[::-1]

# ids of most certain predictions
p_ids = p[i,1].astype (int )

print "writing..."

np.savetxt( output_file, p_ids, fmt = '%d', header = 'Id', comments = '' )


