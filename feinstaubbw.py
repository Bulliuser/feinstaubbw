#!/usr/bin/env python
# coding: utf-8

# In[133]:


import pandas as pd
import datetime as dt
import os

# In[134]:


df=pd.read_csv("https://www.umweltbundesamt.de/api/air_data/v2/airquality/csv?date_from=2022-08-25&time_from=24&date_to=2022-12-01&time_to=1&station=254&lang=de", sep=';')


# In[135]:


df


# In[136]:


df['Feinstaub (PM₁₀) stündlich gleitendes Tagesmittel in µg/m³'] = pd.to_numeric(df['Feinstaub (PM₁₀) stündlich gleitendes Tagesmittel in µg/m³'])


# In[138]:


df['datetime'] = (pd.to_datetime(df['Datum'].str.split(' ').str[0], dayfirst=True) 
                  + pd.to_timedelta(df['Datum'].str.split(' ').str[1] + ':00'))


# In[139]:


df


# In[140]:


df=df.drop(columns='Datum')
df.head()


# In[141]:


df.columns=[
    "station",
    "feinstaubbelastung",
    "ozonbelastung",
    "stickstoffoxid",
    "luftqualität",
    "datum"
]
df.head()


# In[142]:


df.dtypes


# In[143]:


df = df[['station', 'datum', 'feinstaubbelastung','ozonbelastung','stickstoffoxid','luftqualität']]


# In[144]:


df


# In[145]:


df.index=df['datum']


# In[151]:


df['feinstaubbelastung'].rolling(30).mean()


# In[152]:


df.to_csv('feinstaubbiberach.csv')

