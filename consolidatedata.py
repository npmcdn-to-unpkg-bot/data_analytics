import pandas as pd
import psycopg2
import os
import subprocess as sbp
import pdb


## Chicago crime data
# fname='chicago crime/Crimes_-_2001_to_present.csv'
# fnamepath=os.path.join(os.getcwd(),fname.replace('.csv','.h5'))
# if os.path.isfile(fnamepath):
#     sbp.call(['rm',fnamepath])
    
# cols={
# 'Beat' :                     'int64',
# 'District'     :             'int64',
# 'Ward'         :           'float64',
# 'Community Area' :         'float64',
# 'X Coordinate'     :       'float64',
# 'Y Coordinate'     :       'float64',
# 'Year'              :      'float64',
# 'Latitude'           :     'float64',
# 'Longitude'           :    'float64',
#      }

# reader=pd.read_csv(fname,chunksize=50000)
# k=1
# for df in reader:
#     print k
#     for cc in cols.keys():
#     	df[cc]=df[cc].astype(cols[cc])
#     try:
#         df.to_hdf(fname.replace('.csv','.h5'),'chicago_crime', format='table',append=True)
#     except:
#         pdb.set_trace()
#     k=k+1

# divvy    
fname='divvy_set_1/Divvy_historical.csv'
fnamepath=os.path.join(os.getcwd(),fname.replace('.csv','.h5'))
if os.path.isfile(fnamepath):
    sbp.call(['rm',fnamepath])
    
cols={
'ID'                :    'int64',
'Total Docks'       :    'int64',
'Docks in Service' :     'int64',
'Available Docks'   :    'int64',
'Available Bikes'  :     'int64',
'Percent Full'     :     'int64',
'Latitude'         :   'float64',
'Longitude'        :   'float64',
'Record'           :     'int64',
     }

reader=pd.read_csv(fname,chunksize=50000)
k=1
for df in reader:
    print k
    for cc in cols.keys():
    	try:
    		df[cc]=df[cc].fillna(value=0)
    		df[cc]=df[cc].astype(cols[cc])
    	except:
    		pdb.set_trace()
    try:
    	df.to_hdf(fname.replace('.csv','.h5'),'divvy', format='table',append=True)
    except:
    	pdb.set_trace()
    dfp=df.copy()
    k=k+1

