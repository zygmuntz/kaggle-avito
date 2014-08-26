kaggle-avito
============

	construct_line.py - a helper module used by tsv2vw.py
	load_attribs.py - a demo of how to load attribs
	predict.py - produce a solution file for Kaggle from VW predictions
	score.py - get validation scores
	tsv2vw.py - convert data to VW format
	
How to use
----------

	python tsv2vw.py train.tsv train.vw
	python tsv2vw.py test.tsv test.vw
	
	vw -b 29 --loss_function logistic -c --passes 20 train.vw -P 1e5
	
If you don't have enough memory for `-b 29`, try smaller values. Output:

	number of examples per pass = 3596240
	passes used = 14
	weighted example sum = 5.03474e+07
	weighted label sum = -4.34148e+07
	average loss = 0.0395241 h
	best constant = -0.862306
	total feature number = 2567343892

Now disable validation mode with `--holdout_off` and run 14 passes:

	vw -b 29 --loss_function logistic -c --passes 14 -d train.vw -P 1e5 --holdout_off -f model
	vw -t -i model -d test.vw -p predicshuns.txt
	
	python predict.py predicshuns.txt predicshuns_for_kaggle.txt
	
That's it. If you're doing validation, here's how to get scores:

	python score.py test_v.vw p_v.txt
	