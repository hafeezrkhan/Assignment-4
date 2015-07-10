import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

s=pd.read_csv("C:\Python27\Scripts\MYANALYTICS.csv",parse_dates=['CHSI_State_Name'])
s.head()
s.describe()
s['CHSI_State_Name'].describe()
s.dtypes
c = s[['CHSI_State_Name','Population_Size','Poverty']]
c.head()
c_group = c.groupby('CHSI_State_Name')
c_group.size()
s_t = c_group.sum()
s_t.sort(columns='Poverty').head()
my_plot = s_t.plot(kind='bar')
