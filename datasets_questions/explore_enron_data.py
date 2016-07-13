#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "Number of Persons:", len(enron_data)
print "Number of Features:", len(enron_data["SKILLING JEFFREY K"])
total = 0
known_salaries = 0
known_mails = 0
unknown_total_payments = 0
unknown_total_payments_poi = 0
for key, value in enron_data.iteritems() :
    if value['poi'] == 1:
        total += 1
    if value['salary'] != 'NaN':
        known_salaries += 1
    if value['email_address'] != 'NaN':
        known_mails += 1
    if value['total_payments'] == 'NaN':
        unknown_total_payments += 1
    if value['total_payments'] == 'NaN' and value['poi'] == 'true':
        unknown_total_payments_poi += 1
print "Persons of Interest from poi_names:", sum(1 for line in open('../final_project/poi_names.txt')) - 2
print "Persons of Interest:", total
print "Known Salaries :", known_salaries
print "Known Emails:", known_mails
print "Unknown Total Payments:", unknown_total_payments * 100.0 / 146.0, "%"
print "Unknown POI Total Payments:", unknown_total_payments_poi * 100.0 / 146.0, "%"


