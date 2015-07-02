#C:\Python27\Scripts\SUMMARYMEASURESOFHEALTH.csv
#C:\Python27\Scripts\DEMOGRAPHICS.csv
#C:\Python27\Scripts\ANALYTICS.csv
import csv
from collections import OrderedDict
# OPENS SUMMARYMEASURESOFHEALTH.csv FILE
with open('C:\Python27\Scripts\SUMMARYMEASURESOFHEALTH.csv', 'rb') as f:
    r = csv.reader(f)
    dict2 = {row[0]: row[1:] for row in r}
    
#OPENS C:\Python27\Scripts\DEMOGRAPHICS.csv FILE
with open('C:\Python27\Scripts\DEMOGRAPHICS.csv', 'rb') as f:
    r = csv.reader(f)
    dict1 = OrderedDict((row[0], row[1:]) for row in r)
    
#COMBINE DATA TO C:\Python27\Scripts\ANALYTICS.csv FILE
result = OrderedDict()
for d in (dict1, dict2):
    for key, value in d.iteritems():
        result.setdefault(key, []).extend(value)

with open('C:\Python27\Scripts\ANALYTICS.csv', 'wb') as f:
    w = csv.writer(f)
    for key, value in result.iteritems():
        w.writerow([key] + value)