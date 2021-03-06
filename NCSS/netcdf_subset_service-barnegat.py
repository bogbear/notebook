# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Accessing the Unidata THREDDS NetCDF Subset Service
# Using the grid as point service, extracting a time series closest to a specified lon,lat location.  
# 
# At first we use the NetCDF Subset Web Form below to construct the query, but then reuse the URL generated by the form directly in the Python code below.  In this way different time periods, depths or variables may be extracted without returning to the form, and analyzed and visualized in Python without saving and loading CSV files. 
# <hr>
# <iframe src="http://geoport.whoi.edu/thredds/ncss/grid/bbleh/spring2012/pointDataset.html" width=1024 height=400></iframe>
# <hr>

# <codecell>

import pandas as pd
import time

# <codecell>

var = 'temp,salt'
lat = 39.93
lon = -74.12
#start = '2012-05-01T00:00:00Z'
start = '2012-03-01T00:30:00Z'
stop =  '2012-05-10T00:00:00Z'
level = 7

# <codecell>


# <codecell>

url='http://geoport.whoi.edu/thredds/ncss/grid/bbleh/spring2012?\
var=%s&latitude=%f&longitude=%f&time_start=%s&time_end=%s&\
vertCoord=%d&accept=csv' % (var,lat,lon,start,stop,level)
print(url)

# <codecell>

# Extract CSV data directly into Pandas DataFrame (and time how long it takes to extract the data)
time0=time.time()
df = pd.read_csv(url,index_col='date',parse_dates=True)  # skip the units row 
print('Elapsed time=%d seconds' % (time.time()-time0))

# <codecell>

# Make a new DataFrame with just the last two variables (temp & salt)
df2=df.ix[:,-2:]  

# <codecell>

# Plotting time series in Pandas is easy
df2.plot(figsize=(12,4));

# <codecell>

# take a look at the first few values
df2.head(5)

# <codecell>

# calculate the maximum
df2.max()

# <codecell>


