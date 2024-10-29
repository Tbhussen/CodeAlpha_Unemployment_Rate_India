#!/usr/bin/env python
# coding: utf-8

# # Unemployment Rate During Covid-19 Pandemic

# ## by Tamim Hussein

# ## Data Science Internship Task
# 

# In[44]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In the year 2019, one of the world's greatest widespread pandemics started. A microscopic virus called Corona Virus lead to the closure of companies, shifts in stock market, and putting debts on global economies.
# 
# 
# In this report, we are going to analyze the unemployment rate in India during the Covid-19 pandemic. More specifically, we will dive into the study of unemployment rate in Rural vs Urban cities, across indian cities, and the trend of unemployment rate in the country. 

# In[45]:


# Loading dataset 
# Change the direction to use the following report...

df = pd.read_csv("C:\\Users\\ji160\\OneDrive\\Desktop\\Unemployment in India.csv")
df.head()


# --------------------------------------------------------------------------------------------------------------------------

# ## Exploring Dataset

# In[46]:


# Removing any extra Spaces in the dataset column names

df.columns = df.columns.str.strip()
df.columns


# In[47]:


# Getting information about dataset

df.info()


# In[48]:


print(f"This dataset has {df.shape[0]} rows and {df.shape[1]} columns")


# In[49]:


# Calculate null values number

df.isnull().sum()


# In[50]:


# Removing rows containing null values

df = df.dropna()
df.isnull().sum()


# In[51]:


# Discribe the dataset

df.describe()


# In[52]:


print("Mean Unemployment Rate : ", df["Estimated Unemployment Rate (%)"].mean())
print("Median Unemployment Rate : ", df["Estimated Unemployment Rate (%)"].median())
print("Standard deviation Unemployment Rate : ", df["Estimated Unemployment Rate (%)"].std())


# In[53]:


# Track the records vs dates

plt.figure(figsize=(8, 6))
plt.scatter(df["Date"], df["Region"])
plt.xticks(rotation = "vertical")
plt.show()


# ---------------------------------------------------------------------------------------------------------------------
# 

# ## Analysis and Visualization

# Let us start by observing the trend of Unemployment Rate Over Time 

# In[54]:


# Convert the Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group by 'Date' and calculate the mean unemployment rate
unemployment_rate_over_time = df.groupby('Date')["Estimated Unemployment Rate (%)"].mean()

# Visualize the Unemployment rate over time
plt.figure(figsize=(10, 6))
plt.plot(unemployment_rate_over_time.index, unemployment_rate_over_time.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Unemployment Rate Over Time')
plt.grid(True)

# Importing Warnings library
import warnings

# Ignoring unwanted warnings
warnings.filterwarnings("ignore")

plt.show()


# Based on the `Unemployment Rate Over Time` shown in the figure above, June of 2020 showed the most unemployment rate during the covid-19 pandemic in India. After that, the unemployment rate tended to decrease rapidly. 
# 
# Let's observe the distribution of `unemployment rate across the indian cities` in June, 2020 as compared to June, 2019; at the beginning of the pandemic.

# In[55]:


df["Date"].unique()


# In[56]:


region_data = df["Region"].unique()
print("The Indian cities are:", end = " ")
for i in region_data[:-2]:
    print(i, end = " - ")
print(region_data[-1], ".", sep = "")


# In[57]:


# Filter data to 06-2019:
strt_date_data = df[df["Date"] == '2019-05-31 00:00:00']

MIN_unemployment_rate = strt_date_data.groupby('Region')["Estimated Unemployment Rate (%)"].mean()

# Filter data to 06-2020:
strt_date_data = df[df["Date"] == '2020-05-31 00:00:00']

MAX_unemployment_rate = strt_date_data.groupby('Region')["Estimated Unemployment Rate (%)"].mean()

# Combine the data into a DataFrame for easier plotting
unemployment_df = pd.DataFrame({
    '2019-05-31': MIN_unemployment_rate,
    '2020-05-31': MAX_unemployment_rate
})

# Plot a bar chart
plt.figure(figsize=(10, 6))
unemployment_df.plot(kind='bar', width=0.7)
plt.xlabel('Region')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Unemployment Rate by Region (2019 vs 2020)')
plt.xticks(rotation="vertical")
plt.legend(title='Date')
plt.grid(axis='y')

plt.tight_layout()
plt.show()


# The unemployment rate for the two specific cities: **Delhi** and **Puduchery**. Delhi is the capital of India, thus observing the unemployment rate in this city is important indicator of the overall trend in the country. The other city, Puduchery, recorded the greatest change in the unemployment rate during the covid-19 pandemic in India, from **less than 5%** at the beginning of the crisis to **more than 70%** after a year, in May - June 2020.

# In[58]:


# Filter the DataFrame for a specific region,'Delhi'
region_df = df[df['Region'] == 'Delhi']

# Group by Date and calculate the mean unemployment rate for the specified region
unemployment_rate_over_time = region_df.groupby('Date')["Estimated Unemployment Rate (%)"].mean()

# Plot the bar chart
import matplotlib.pyplot as plt

# Visualize the Unemployment rate over time
plt.figure(figsize=(10, 6))
plt.plot(unemployment_rate_over_time.index, unemployment_rate_over_time.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Unemployment Rate Over Time for Delhi')

plt.grid(True)

plt.show()


# In[59]:


# Filter the DataFrame for a specific region,'Puducherry'
region_df = df[df['Region'] == 'Puducherry']

# Group by Date and calculate the mean unemployment rate for the specified region
unemployment_rate_over_time = region_df.groupby('Date')["Estimated Unemployment Rate (%)"].mean()

# Plot the bar chart
import matplotlib.pyplot as plt

# Visualize the Unemployment rate over time
plt.figure(figsize=(10, 6))
plt.plot(unemployment_rate_over_time.index, unemployment_rate_over_time.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Unemployment Rate Over Time for Puducherry')
plt.grid(True)

plt.show()


# Another level of analysis on unemployment rate is the variation of `unemployment rate as function of the Area (Rural vs Urban)`. The Urban curve showed greater unemployment rate than the Rural curve over the whole period of the Covid-19 pandemic. 
# 
# This could be due to differences between urban and rural cities in terms of lifestyle of the people, type of economic activities, and the ability of the government to have control over the lockdown policies in each areas.

# In[60]:


# filter on Rural
rural_data = df[df["Area"] == 'Rural']
# Group by Date and calculate the mean unemployment rate for the specified Area
rural_rate_over_time = rural_data.groupby('Date')["Estimated Unemployment Rate (%)"].mean()

# filter on Urban
urban_data = df[df["Area"] == 'Urban']
# Group by Date and calculate the mean unemployment rate for the specified Area
urban_rate_over_time = urban_data.groupby('Date')["Estimated Unemployment Rate (%)"].mean()

# Combine the data into a DataFrame for easier plotting
unemployment_df = pd.DataFrame({
    'Urban': urban_rate_over_time,
    'Rural': rural_rate_over_time
})

# Visualize the Unemployment rate over time by Area
plt.figure(figsize=(10, 6))
plt.plot(unemployment_df.index, unemployment_df['Urban'], marker='o', label='Urban')
plt.plot(unemployment_df.index, unemployment_df['Rural'], marker='o', label='Rural')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Unemployment Rate over time by Area (Rural vs Urban)')
plt.legend(title='Area')
plt.grid(True)

plt.show()

