#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from decouple import config
import requests
from pandas import DataFrame as df
from ipyleaflet import Map, basemaps
#!jupyter labextension install @jupyter-widgets/jupyterlab-manager
#!jupyter labextension install jupyter-leaflet


# In[ ]:


base_url = "https://eonet.sci.gsfc.nasa.gov/api/v3/events?api_key="
API_KEY = config("API_KEY")


# In[ ]:


r = requests.get(base_url + API_KEY)


# In[ ]:


r_dict = r.json()
df.from_dict(r_dict)


# In[ ]:


center = [37.9889021,-122.0305244]
zoom = 10

m = Map(basemap=basemaps.OpenStreetMap.Mapnik, center=center, zoom=zoom)
display(m)

