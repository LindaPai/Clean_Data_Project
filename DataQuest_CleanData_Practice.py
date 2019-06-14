#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# utf-8 can't encoding
laptops = pd.read_csv("laptops.csv", encoding = "Latin-1")
laptops.info()


# In[3]:


laptops.columns


# In[4]:


# Remove whitespaces from the column names -> "Storage" have space infront
new_columns = []
for x in laptops.columns:
    clean = x.strip()
    new_columns.append(clean)
# new_columns = laptops.columns -> nothing happend
laptops.columns = new_columns
new_columns 


# # Finish cleaning column labels by:
# 1. Replacing spaces with underscores.
# 2. Removing special characters.
# 3. Making all labels lowercase.
# 4. Shortening any long column names.

# In[5]:


def clean_col(col):
    col = col.strip() # remove whitespaces
    col = col.replace("Operating System","os")
    col = col.replace(" ","_") # replace spaces to _
    col = col.replace("(","") # remove parentheses
    col = col.replace(")","")
    col = col.lower() # make string lowercase
    return col

new_columns_1 = []
for y in laptops.columns:
    clean_1 = clean_col(y)
    new_columns_1.append(clean_1)
    
laptops.columns = new_columns_1 # save result in df.columns
new_columns_1


# In[6]:


laptops.columns


# # Convert columns to numeric

# ![convert%20to%20numeric%20work%20flow.JPG](attachment:convert%20to%20numeric%20work%20flow.JPG)

# In[7]:


# Explore and Identify
unique_screen_size = laptops["screen_size"].unique()
unique_screen_size


# In[8]:


unique_ram = laptops["ram"].unique()
unique_ram


# In[9]:


# Remove non_digit characters
# remove " of 13.3"
laptops["screen_size"] = laptops["screen_size"].str.replace('"',"")
print(laptops["screen_size"].unique())


# In[10]:


# remove GB of 8GB
laptops["ram"] = laptops["ram"].str.replace("GB","")
laptops["ram"].unique()


# In[11]:


# Convert the column to a numeric dtype
laptops["screen_size"] = laptops["screen_size"].astype(float)
print("screen_size dtype = ",laptops["screen_size"].dtype)
print("screen_size unique = ", laptops["screen_size"].unique())

laptops["ram"] = laptops["ram"].astype(int)
print("ram dtype = ", laptops["ram"].dtype)
print("ram unique = ", laptops["ram"].unique())


# In[12]:


# Rename column if required
laptops.rename({"screen_size": "screen_size_inches"}, axis =1, inplace = True)

laptops.rename({"ram" : "ram_gb"}, axis =1, inplace = True)
print(laptops.dtypes)


# # Extracting values from String
# 1. Find the most common manufacturer of "cpu" column

# In[13]:


print(laptops["gpu"].head())


# In[14]:


# str[0] to locate the first element of string
laptops["gpu_manufacturer"] = (laptops["gpu"].str.split().str[0])
gpu_manufacturer_counts = laptops["gpu_manufacturer"].value_counts()
print(gpu_manufacturer_counts)


# In[15]:


laptops["cpu_manufacturer"] = (laptops["cpu"].str.split().str[0])
cpu_manufacturer_counts = laptops["cpu_manufacturer"].value_counts()
print(cpu_manufacturer_counts)


# # Replacing Values Using A Mapping Dictionary
# 1. Series.map() method is ideal when we want to change multiple values in a column.

# In[16]:


print(laptops["os"].value_counts())


# In[17]:


mapping_dict = {"Android" : "Android", 'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'}
laptops["os"] = laptops["os"].map(mapping_dict)
print(laptops["os"].value_counts())


# # Dropping Missing Values
# There are a few options for handling missing values:
# 1. Remove any rows that have missing values.
# 2. Remove any columns that have missing values.
# 3. Fill the missing values with some other value.
# 4. Leave the missing values as is.
# 
# ## althoguh use dropna, but original DataFrame itself didn't change
# If want DataFrame itself to change, add inplace=True parameter

# In[18]:


print(laptops.isnull().sum())


# In[19]:


# remove rows and columns of laptops
laptops_no_null_rows = laptops.dropna(axis = 0)
laptops_no_null_cols = laptops.dropna(axis = 1)
print(laptops_no_null_rows.head(3))


# ## Removing a disproportionate amount of one manufacturer's laptops could change our analysis
# 
# It's GOOD idea to explore the missing values in the os_version column before making decision.
# 
# 1. Set the dropna parameter to False, the result INCLUDES null values.
# 
# 2. Also explore the os column, since it's closely related to the os_version column.
# 
# 3. Fill the missing values to make our data more correct.
# 
# 4. For the rest of the values, it's probably best to leave them as missing so we don't remove important values.

# In[20]:


print(laptops["os_version"].value_counts(dropna = False))


# In[21]:


print(laptops["os"].value_counts(dropna = False))


# In[22]:


# Find the rows which the os_version is missing
os_with_null_v = laptops.loc[laptops["os_version"].isnull(), "os"]
print(os_with_null_v.value_counts())


# In[23]:


# SEE the difference of BEFORE and AFTER
value_counts_before = laptops.loc[laptops["os_version"].isnull(),"os"].value_counts()

laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"
laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"

value_counts_after = laptops.loc[laptops["os_version"].isnull(),"os"].value_counts()

print("BEFORE: ", value_counts_before)

print("AFTER: ", value_counts_after)


# In[24]:


print(laptops["weight"].head())


# In[25]:


print(laptops["weight"].unique())


# In[26]:


# Remove "kg" & "kgs" from weight column
#laptops["weight"] = laptops["weight"].str.replace("kgs","").str.replace("kg","").astype(float)

laptops["weight"] = laptops["weight"].str.replace("kgs","")
laptops["weight"] = laptops["weight"].str.replace("kg","")

#print(laptops["weight"].unique())

laptops["weight"] = laptops["weight"].astype(float)
laptops.rename({"weight" : "weight_kg"}, axis =1, inplace = True)
laptops.dtypes


# In[27]:


# Save the data to a CSV file without index labels
laptops.to_csv("laptops_v1.csv",index = False)

