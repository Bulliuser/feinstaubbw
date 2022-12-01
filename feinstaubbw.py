#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime as dt
import requests
import json
from pandas import json_normalize


# In[74]:


df=pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/airquality/csv?date_from=2022-08-25&time_from=24&date_to=2022-12-01&time_to=1&station=254&lang=de", sep=';')


# In[75]:


df


# In[76]:


df['Feinstaub (PM₁₀) stündlich gleitendes Tagesmittel in µg/m³'] = pd.to_numeric(df['Feinstaub (PM₁₀) stündlich gleitendes Tagesmittel in µg/m³'])


# In[77]:


df['datetime'] = (pd.to_datetime(df['Datum'].str.split(' ').str[0], dayfirst=True) 
                  + pd.to_timedelta(df['Datum'].str.split(' ').str[1] + ':00'))


# In[78]:


df


# In[79]:


df=df.drop(columns='Datum')
df.head()


# In[80]:


df.columns=[
    "station",
    "feinstaubbelastung",
    "ozonbelastung",
    "stickstoffoxid",
    "luftqualität",
    "datum"
]
df.head()


# In[81]:


df.dtypes


# In[82]:


df = df[['station', 'datum', 'feinstaubbelastung','ozonbelastung','stickstoffoxid','luftqualität']]


# In[83]:


df


# In[92]:


df.index=df['datum']


# In[93]:


df.resample(rule="3h").sum().plot.line() 


# In[95]:


df.rolling(30).mean().plot.line()


# In[88]:


df.to_csv('feinstaubbiberach.csv')

