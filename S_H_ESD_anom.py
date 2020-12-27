# -*- coding:utf-8 -*-

import pyculiarity.detect_ts as detect_ts_func
import pandas as pd

n_file = 'machine_temperature_system_failure'
timeS_DF = pd.read_csv('./data/%s.csv'% n_file, usecols = ['timestamp', 'value'])
# print(timeS_DF)

""" detect_ts grouped by only_last / longterm / resample_period """
# PARAM > max_anoms : S-H-ESD에서 감지 할 수 있는 최대 수치(%, 0.5 이하), direction: 방향(pos, neg, both), only_last : 관심 기간(day, hr, None), resample_period : resampling period
# PARAM > threshold: Only report positive going anoms above the threshold specified. Options are: (None | 'med_max' | 'p95' | 'p99')
# machine_temperature_system_failure
results = detect_ts_func(timeS_DF, max_anoms=0.01, direction='both', only_last= None, resample_period='H')
#print(results)

""" Plotting """
# reformat the index and columns
timeS_DF = timeS_DF.set_index('timestamp')

anomsDF = results['anoms']
anomsDF.drop(['timestamp'], axis = 1, inplace = True)
anomsDF['is_anom'] = True
# anomsDF.columns = ['anom_value','is_anom']

merged_DF = pd.merge(left = timeS_DF, right= anomsDF, left_index=True, right_index=True, how = 'left')
# merged_DF.drop('anom_value',axis = 1,inplace=True)

""" Deliverables """
print ('>>> the number of anomaly: ', len(results['anoms']))
print (results['anoms'].head())



