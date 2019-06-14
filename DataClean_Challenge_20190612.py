#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
laptops = pd.read_csv("laptops_v1.csv")


# # First 3 chanllenge Questions
# 
# 1. Convert the price_euros column to a numeric dtype

# In[2]:


# Explore the data in the column
laptops.info()


# In[3]:


laptops["price_euros"].unique()


# In[4]:


# Change comma "," to peroid "."
laptops["price_euros"] = laptops["price_euros"].str.replace(",",".")
print(laptops["price_euros"].head())


# In[5]:


# Convert to numeric dtype
laptops["price_euros"] = laptops["price_euros"].astype(float)
print(laptops["price_euros"].dtype)


# In[6]:


laptops.dtypes


# 2. Extract the screen resolution from the screen column

# In[7]:


laptops["screen"].head()


# In[8]:


laptops["screen"].unique()


# In[9]:


laptops["screen_resolution"] = laptops["screen"].str.split().str[-1]


# In[10]:


print(laptops["screen_resolution"].value_counts())


# In[11]:


laptops.dtypes


# 3. Extract the processor speed from the cpu column

# In[12]:


laptops["cpu"].unique()


# In[13]:


laptops["cpu_speed_GHz"] = laptops["cpu"].str.split().str[-1]


# In[14]:


print(laptops["cpu_speed_GHz"].value_counts())


# In[15]:


laptops["cpu_speed_GHz"] = laptops["cpu_speed_GHz"].str.replace("GHz","")
print(laptops["cpu_speed_GHz"].value_counts())


# In[16]:


laptops.dtypes


# In[17]:


laptops["cpu_speed_GHz"] = laptops["cpu_speed_GHz"].astype(float)
print(laptops.dtypes)


# In[18]:


laptops.to_csv("laptops_v2.csv", index = False)


# # Last 3 Challenge Questions
# 
# 1. Are laptops made by Apple more expensive than those made by other manufacturers?

# In[19]:


laptops_compare = laptops[["manufacturer","price_euros"]]
#laptops_compare


# In[20]:


price_compare = {}

for brand in laptops_compare["manufacturer"]:
    brand_only = laptops_compare[laptops_compare["manufacturer"] == brand]
    mean_price = brand_only["price_euros"].mean()
    price_compare[brand] = int(mean_price)

price_compare


# ## ANS:
# Of all the laptops manufacture, Apple's laptops are not more expensive than others.
# 
# - MSI, Microsoft, Razer, Google and LG laptops are more expensive than Apple.
# - Fujitsu, Meiacom, Vero, Chuwi and Acer are less expensive.

# 2. What is the best value laptop with a screen size of 15" or more?

# In[ ]:





# 3. Which laptop has the most storage space?

# In[21]:


laptops["storage"].unique()


# In[22]:


laptops.to_csv("laptops_v3.csv", index = False)


# In[23]:


top_storage_by_model_name = {}
model_name = laptops["model_name"].unique()
for i in model_name:
    selected_rows = laptops[laptops["model_name"] == i]
    sorted_rows = selected_rows.sort_values(by = "storage", ascending = False)
    top_storage = sorted_rows.iloc[0]
    storage = top_storage["storage"]
    top_storage_by_model_name[storage] = i


# In[24]:


top_storage_by_model_name


# In[25]:


print(top_storage_by_model_name["512GB SSD +  2TB HDD"])


# In[26]:


model_bool = laptops["model_name"] == "Q534UX-BHI7T19 (i7-7500U/16GB/2TB"
model_manufacturer = laptops.loc[model_bool, "manufacturer"]
model_manufacturer


# ## ANS:
# 
# The Q534UX-BHI7T19 (i7-7500U/16GB/2TB) model from Asus has the most storage space.
