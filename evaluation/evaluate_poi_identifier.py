#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
from time import time
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.cross_validation import train_test_split

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


def true_positives(predicted, actual):
    count = 0
    for i in range(0,len(predicted)):
        if predicted[i] == actual[i] == 1:
            count += 1
    return count


def true_negatives(predicted, actual):
    count = 0
    for i in range(0, len(predicted)):
        if predicted[i] == actual[i] == 0:
            count += 1
    return count


def false_positives(predicted, actual):
    count = 0
    for i in range(0,len(predicted)):
        if predicted[i] == 1 and actual[i] == 0:
            count += 1
    return count


def false_negatives(predicted, actual):
    count = 0
    for i in range(0, len(predicted)):
        if predicted[i] == 0 and actual[i] == 1:
            count += 1
    return count


data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!
features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print "Training Time:", round(time()-t0, 3), "s"
t1 = time()
predictions = clf.predict(features_test)
print "Prediction Time:", round(time()-t1, 3), "s"
accuracy = accuracy_score(labels_test, predictions)
precision = precision_score(labels_test, predictions)
recall = recall_score(labels_test, predictions)
f1 = f1_score(labels_test, predictions)
print "Accuracy:", accuracy
print "Precision:", precision
print "Recall:", recall
print "F1 Score:", f1
total = len(predictions)
poi = 0
for prediction in predictions:
    if prediction == 1:
        poi += 1
not_poi = total - poi
print "Out of %d persons, %d are poi and %d are not." % (total, poi, not_poi)
print "True Positives: %d" % true_positives(predictions,labels_test)
print "True Negatives: %d" % true_negatives(predictions,labels_test)
print "False Positives: %d" % false_positives(predictions,labels_test)
print "False Negatives: %d" % false_negatives(predictions,labels_test)
