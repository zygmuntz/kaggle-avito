Training a separate model for each category
===========================================

...results in a better score (.978 instead of .971).

	aggregate_predictions.py - produce a solution file from predictions by category
	csv2vw.py - convert CSV to VW (needs construct_line.py from the parent folder)
	split_into_categories.py - split train/test into separate CSV file for each category

When converting test, there will be one point missing (id 89655507). `aggregate_predictions.py` will insert a prediction for this point.

Workflow
--------

1. split train and test into categories
2. convert from CSV to VW
3. train a separate VW model for each category
4. make predictions for each category
5. aggregate predictions
