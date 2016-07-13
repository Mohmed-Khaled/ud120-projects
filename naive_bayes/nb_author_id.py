#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time


sys.path.append("../tools/")
# noinspection PyUnresolvedReferences
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing data sets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#########################################################
# your code goes here
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print "Training Time:", round(time()-t0, 3), "s"
t1 = time()
predictions = clf.predict(features_test)
print "Prediction Time:", round(time()-t1, 3), "s"
accuracy = accuracy_score(predictions, labels_test)
print "Accuracy:", accuracy
total = len(predictions)
chris = 0
for prediction in predictions:
    if prediction == 1:
        chris += 1
sara = total - chris
print "Out of %d emails, Chris' emails are %d and Sara's emails are %d" % (total, chris, sara)
#########################################################
