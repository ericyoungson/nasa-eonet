#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from decouple import config
import requests
from ipyleaflet import Map, basemaps
get_ipython().system('jupyter labextension install @jupyter-widgets/jupyterlab-manager')
get_ipython().system('jupyter labextension install jupyter-leaflet')


# In[ ]:


base_url = "https://eonet.sci.gsfc.nasa.gov/api/v3/events?api_key="
API_KEY = config("API_KEY")


# In[ ]:


r = requests.get(base_url + API_KEY)


# In[ ]:


center = [37.9780, 122.0311]
zoom = 5

m = Map(basemap=basemaps.OpenStreetMap.Mapnik, center=center, zoom=zoom)
display(m)

