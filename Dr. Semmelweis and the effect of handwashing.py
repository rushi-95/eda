#!/usr/bin/env python
# coding: utf-8

# ### Steps:
# #### 1- Import necessary libraries
# #### 2- Read the yearly deaths dataset
# #### 3- Explore the dataset
# #### 4- Read and explore the monthly deaths dataset
# #### 5- Investigate the number of deaths from 1841 to 1846

# ### I- Yearly data

# In[40]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Read the yearly dataset
yearly_df = pd.read_csv("yearly_deaths_by_clinic.csv")

yearly_df


# In[2]:


yearly_df.shape


# In[3]:


yearly_df.info()


# In[4]:


yearly_df.groupby("clinic") ["deaths"].sum()


# #### The above results shows us the number of births and deaths in 2 clinics from the year 1841 till 1846. It's obvious that the number of deaths in clinic 1 is higher than that of clinic 2. 

# In[5]:


#To make the analysis easier, we can calculate the proportion of deaths.
yearly_df["Proportion of Deaths"] = yearly_df["deaths"] / yearly_df["births"]
yearly_df


# In[6]:


#Separate the dataset into 2 datasets, one for each clinic
clinic_1 = yearly_df[yearly_df["clinic"] == "clinic 1"]
clinic_2 = yearly_df[yearly_df["clinic"] == "clinic 2"]


# In[7]:


clinic_1


# In[8]:


clinic_2


# In[9]:


#Visualize the Number of deaths every year in clinic 1
fig,ax = plt.subplots(figsize = (10,4))
plt.bar(clinic_1.year, clinic_1.deaths, width= 0.6, color= "red")
plt.title("Clinic 1: Number of Deaths per Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Deaths", fontsize=14)


# In[10]:


#Visualize the Number of deaths every year in clinic 2
fig,ax = plt.subplots(figsize = (10,4))
plt.bar(clinic_2.year, clinic_2.deaths, width= 0.6, color= "green")
plt.title("Clinic 2: Number of Deaths per Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Deaths", fontsize=14)


# #### It seems that 1842 was a pretty hectic year in both clinic 1 & 2 where the numbers of deaths were 518 and 202 respectively

# #### Plot the proportion of deaths in clinic 1 and 2

# In[41]:


ax= clinic_1.plot(x= "year", y= "Proportion of Deaths", label= "clinic_1", color="red")
clinic_2.plot(x= "year", y= "Proportion of Deaths", label= "clinic_2", ax=ax, ylabel= "Proportion of Deaths", color="green")


# #### By looking further into why this happened, Dr Semmelweis realized that many medical students worked at clinic 1 who also as a part of their study, spend a lot of time in the autopsy room. So, he realized that dealing with corpses spread bacteria that would be transferred to the women giving birth, infecting them with the deadly childbed fever, which was the main reason for the high mortality rates. 
# 

# ### II- Monthly data

# In[12]:


# Read the monthly dataset
monthly_df = pd.read_csv("monthly_deaths.csv")
monthly_df.head(5)


# In[14]:


monthly_df.info()


# In[13]:


#Calculate the proportion of deaths per month
monthly_df["Proportion of Deaths"]= monthly_df["deaths"] / monthly_df["births"]
monthly_df.head(5)


# #### Dr Semmelweis ordered the doctors to wash their hands and made it obligatory in the summer of 1847 to see if that will affect the number of deaths, and since we have the monthly data now, we can trace the number of deaths before and after the handwashing started. 

# In[17]:


#Change the data type of "date" column from string to datatime
monthly_df.dtypes
monthly_df['date'] =  pd.to_datetime(monthly_df['date'])


# In[25]:


# Label the date at which handwashing started to "start_handwashing"
start_handwashing = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly_df[monthly_df["date"] < start_handwashing]
after_washing = monthly_df[monthly_df["date"] >= start_handwashing]


# ### Before Handwashing

# In[27]:


fig,ax = plt.subplots(figsize = (10,4))
x= before_washing["date"]
y= before_washing["Proportion of Deaths"]
plt.plot(x, y, color= "orange")
plt.title("Before Handwashing", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Proportion of Deaths", fontsize=14)


# ### After Handwashing

# In[30]:


fig,ax = plt.subplots(figsize = (10,4))
x= after_washing["date"]
y= after_washing["Proportion of Deaths"]
plt.plot(x, y, color= "green")
plt.title("After Handwashing", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Proportion of Deaths", fontsize=14)


# #### To see the difference clearly, let's combine the 2 plots in one chart.

# In[34]:


ax= before_washing.plot(x= "date", y= "Proportion of Deaths", label= "Before Handwashing", color="orange")
after_washing.plot(x= "date", y= "Proportion of Deaths", label= "After Handwashing", ax=ax, ylabel= "Proportion deaths", color="green") 


# #### The difference is pretty clear! the proportion of deaths dramatically decreased after handwashing was made obligatory.

# #### Let's calculate exactly how much did handwashing decreased the proportion of deaths on average.

# In[37]:


before_proportion = before_washing["Proportion of Deaths"]
after_proportion = after_washing["Proportion of Deaths"]
before_proportion.mean()


# In[38]:


after_proportion.mean()


# In[42]:


# Calculate the difference between both proportions
mean_diff = after_proportion.mean() - before_proportion.mean()
mean_diff


# #### The minus sign indicate that there is a decrease. So handwashing decreased the proportion of deaths from 10% to 2% i.e, by approximately 8%.

# In[ ]:




