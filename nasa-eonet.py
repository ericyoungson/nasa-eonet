#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from decouple import config
import requests


# In[ ]:


base_url = "https://eonet.sci.gsfc.nasa.gov/api/v3/events?api_key="
API_KEY = config("API_KEY")


# In[ ]:


r = requests.get(base_url + API_KEY)


# In[ ]:


r.json()

