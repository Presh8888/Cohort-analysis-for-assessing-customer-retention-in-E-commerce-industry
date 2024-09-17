#!/usr/bin/env python
# coding: utf-8

# # Import libraries

# In[ ]:


import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For data visualization
from datetime import datetime # For date and time manipulation
import datetime as dt


# # Load dataset

# In[136]:


data = pd.read_csv(r"C:\Users\presh\Downloads\Dataset_ecommerce.csv")

# Display the first 5 rows of the dataset
data.head(5)


# In[6]:


# Descriptive_stats
data.describe(include='all')


# In[7]:


# Check for missing values 
data.isnull().sum()


# In[9]:


# drop missing values
data.dropna(inplace = True)


# In[10]:


# check for info on dataframe
data.info()


# In[11]:


# convert to datetime format
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])


# # Exploratory data analysis

# In[35]:


# Analysis by country
quantity_by_country = data.groupby(["Country"])["Quantity"].sum().reset_index()

quantity_by_country = quantity_by_country.sort_values("Quantity", ascending = False).reset_index()
quantity_by_country.head(3)


# In[33]:


#visualize top 10 countries where most products are sold
top_10_country = quantity_by_country.head(10)

plt.figure(figsize=(20, 8))
ax = sns.barplot(x="Country", y="Quantity", data = top_10_country)

plt.title("Bar chart of top 10 countries with highest purchase")
plt.xlabel("Countries")
plt.ylabel("Quantity of product")
plt.show()


# In[42]:


#visualize last 10 countries where least number of products are sold
least_10_country = quantity_by_country.tail(10)

plt.figure(figsize=(20, 8))
ax = sns.barplot(x="Country", y="Quantity", data = least_10_country)

plt.title("Bar chart of bottom 10 countries with highest purchase")
plt.xlabel("Countries")
plt.ylabel("Quantity of product")
plt.show()


# In[49]:


# Analysis of countries and number of customers

Country_to_customer = data.groupby(["Country"])["CustomerID"].nunique().reset_index()
Country_to_customer = Country_to_customer.sort_values("CustomerID", ascending = False).reset_index()
Country_to_customer.head(3)


# In[55]:


# Draw a plot of top 10 countries with most numbers of customers
top_countries_to_customer = Country_to_customer.head(10)

plt.figure(figsize=(20, 8))
sns.barplot(x="Country", y="CustomerID", data=top_countries_to_customer)

plt.title("Bar chart of top 10 countries with most number of customers")
plt.xlabel("Countries")
plt.ylabel("Total number of customers")
plt.show()


# In[59]:


# sales trend visualization

monthly_sales = data.groupby(data["InvoiceDate"].dt.to_period("M"))["Quantity"].sum()
monthly_sales


# In[62]:


# Create a line plot
plt.figure(figsize=(20, 10))
plt.plot(monthly_sales.index.strftime("%y-%m"), monthly_sales.values, marker='o', linestyle='-')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.grid(True)
plt.show()


# # Cohort Analysis

# In[63]:


data.head()


# In[78]:


def get_month(x):
    return dt.datetime(x.year, x.month, 1)
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data["InvoiceDate"] = data["InvoiceDate"].apply(get_month)
data.head()


# In[92]:


def get_cohort_date(data):
    # Calculate the first purchase date for each customer
    data["cohort date"] = data.groupby("CustomerID")["InvoiceDate"].transform("min")
    return data

# Apply the function to get the cohort date
data = get_cohort_date(data)
data


# # Cohort index

# In[95]:


def get_year_and_month(data, col):
    
    month = data[col].dt.month
    year = data[col].dt.year
    return month, year
    


# In[98]:


first_month, first_year = get_year_and_month(data, "cohort date")
first_month


# In[99]:


first_year


# In[100]:


latest_month, latest_year = get_year_and_month(data, "InvoiceDate")
latest_month


# In[101]:


latest_year


# # Cohort index

# In[114]:


ddef create_cohort_index(first_month, first_year, latest_month, latest_year):
    year_diff = latest_year - first_year  # Calculate the difference in years
    month_diff = latest_month - first_month  # Calculate the difference in months
    index = year_diff * 12 + month_diff + 1  # Compute the cohort index
    return index  # Return the computed index


# In[116]:


data["cohort_index"] = create_cohort_index(first_month, first_year, latest_month, latest_year)
data


# # Cohort table

# In[117]:


cohort_info = data.groupby(["cohort date", "cohort_index"])["CustomerID"].nunique().reset_index()
cohort_info.rename(columns ={"CustomerID" : "Number of customers"}, inplace = True)
cohort_info


# In[119]:


cohort_table = cohort_info.pivot(index = "cohort date", columns = ["cohort_index"], values = "Number of customers")
cohort_table.index =cohort_table.index.strftime("%B %Y")
cohort_table


# In[122]:


plt.figure(figsize =(20,10))
sns.heatmap(cohort_table, annot = True,cmap = "Dark2_r", fmt = ".2f")


# In[124]:


new_cohort_table = cohort_table.divide(cohort_table.iloc[:,0], axis = 0)
new_cohort_table


# In[125]:


plt.figure(figsize =(20,10))
sns.heatmap(new_cohort_table, annot = True,cmap = "Dark2_r", fmt = ".0%")


# In[ ]:





# **Quantity bought**

# In[133]:


quantity_bought =data.groupby(["cohort date", "cohort_index"])["Quantity"].mean().reset_index()
quantity_bought


# In[134]:


quantity_table = quantity_bought.pivot(index = "cohort date", columns = ["cohort_index"], values = "Quantity")
quantity_table.index = quantity_table.index.strftime("%B %Y")
quantity_table


# In[135]:


plt.figure(figsize =(20,10))
sns.heatmap(quantity_table, annot = True,cmap = "Dark2_r", fmt = ".3f")

