#!/usr/bin/env python

'compute metrics for VW test file and VW predictions file'

import sys
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score as AUC
from scipy.special import expit as sigmoid

y_file = sys.argv[1]
p_file = sys.argv[2]

try:
	k = int( sys.argv[3] )
except IndexError:
	k = 20000

# load and prepare predictions

print "loading p..."

p = np.loadtxt( p_file )

y_predicted = np.ones(( p.shape[0] ))
y_predicted[sigmoid( p[:,0] ) < 0.5] = -1

# sort by prediction and reverse
i = np.argsort( p[:,0] )[::-1]

# ids of most certain predictions
p_ids = p[i,1].astype(int)[:k]

# load positive examples from test

print "loading y..."

y = np.loadtxt( y_file, usecols= [0, 2], converters = { 2: lambda x: x.split( '|' )[0] } )
y_true = y[:,0]
pos_ids = y[y[:,0] == 1][:,1].astype( int )

# calculate precision

print "calculating AP@{}...".format( k )

# this snippet is from Kaggle code
countRelevants = 0
listOfPrecisions = list()
for i, p_id in enumerate(p_ids):
	currentk = i + 1.0
	if p_id in pos_ids:
		countRelevants += 1
	precisionAtK = countRelevants / currentk 
	listOfPrecisions.append(precisionAtK)

print sum( listOfPrecisions ) / k 

print
print "confusion matrix:"
print confusion_matrix( y_true, y_predicted )

print
print "AUC:", AUC( y_true, p[:,0] )


