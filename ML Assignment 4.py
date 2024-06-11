#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#Reading the data present in the csv file and storing it in a variable named data
df=pd.read_csv('data.csv')
df


# In[2]:


#describing the basic statistical description about the data
df.describe()


# In[3]:


#checking null values in data
print(df.isnull().any())
#replacing null values using mean
df.fillna(df.mean(),inplace=True)
#checking null values after replacing
print("\nData after replacing null with mean value:\n{}".format(df.isnull().any()))


# In[4]:


#Selecting the two columns duration and calories and aggregating them with the computation values of min,max,count,and mean for its respective columns
df.agg({'Duration':['min','max','count','mean'],'Calories':['min','max','count','mean']})


# In[5]:


df[(df['Calories']>=500) & (df['Calories']<=1000)]


# In[6]:


df[(df['Calories']>500) & (df['Pulse']<100)]


# In[7]:


df_modified=df.drop("Maxpulse",axis=1)
df_modified


# In[8]:


df=df.drop("Maxpulse",axis=1)
df


# In[9]:


print("Datatype of the Calories column before changing it to int:",df['Calories'].dtypes)
df['Calories']=df['Calories'].astype(int)
print("Datatype of the Calories column after changing it to int:",df['Calories'].dtypes)


# In[ ]:




