#!/usr/bin/env python
# coding: utf-8

# # Data Analytics Project 
# 

# #IMPORTING THE LIBRARIES
# 

# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# In[2]:


#IMPORTING THE DATASET
sales = pd.read_csv('F:\Project4/Salesstore.csv')


# In[3]:


sales.head(10)


# In[4]:


#NAMES OF ALL THE COLUMNS
sales.columns


# In[6]:


sales.Order_ID


# In[8]:


sales.shape


# In[9]:


len(sales['Order_ID'].unique())


# In[10]:


len(sales['Product_Name'].unique())


# In[11]:


sales=sales.drop(columns='Order_ID')
sales=sales.drop(columns='Product_Name')


# In[12]:


sales.columns


# In[13]:


sales.info()


# In[14]:


#To get Stastical Information :
sales.describe()


# In[15]:


sns.countplot(sales.Ship_Mode)
sales.Ship_Mode.value_counts()


# # CUSTOMER SEGMENT

# In[17]:


plt.figure(figsize = (5,5))
corp = sales.loc[sales['Customer_Segment'] == 'Corporate'].count()[0]
cons = sales.loc[sales['Customer_Segment'] == 'Consumer'].count()[0]
hoff = sales.loc[sales['Customer_Segment'] == 'Home Office'].count()[0]
sbiz = sales.loc[sales['Customer_Segment'] == 'Small Business'].count()[0]
explode = (0.1, 0.1, 0.1, 0.1)
labels = ['Corporate', 'Consumer', 'Home Office', 'Small Business']
plt.pie([corp, cons, hoff, sbiz], labels = labels, autopct = '%.2f %%', explode = explode)
plt.title("Customer Segment")
plt.show()

sales.Customer_Segment.value_counts()


# # PRODUCT CATEGORY

# In[18]:


sns.countplot(sales.Product_Category)
sales.Product_Category.value_counts()


# PRODUCT CONTAINER

# In[19]:


sns.countplot(sales.Product_Container)
sales.Product_Container.value_counts()


# # ORDER QUANTITY

# In[20]:


sns.boxplot(sales['Order_Quantity'])


# In[21]:


sales.Profit.describe()


# In[22]:


sales.Sales.describe()


# # PROFIT VS SALES

# In[23]:


sns.relplot('Sales', 'Profit', data = sales)


# For most of the purchases, the profit is increasing with increasing sales. Hence, there is a positive correlation between sales nd profit. Most sales lie between 0 and 10000.

# In[24]:


sns.relplot('Sales', 'Profit', data = sales, hue = 'Ship_Mode')


# In[25]:


sns.relplot('Sales', 'Profit', data = sales, kind = 'line')


# # PROFIT VS PRODUCT CATEGORY

# In[26]:


sns.catplot(x = 'Product_Category', y = 'Profit', data = sales, kind = 'box', height = 6)


# # PROFIT FROM DIFFERENT REGIONS

# In[27]:


sns.catplot(x = 'Region', y = 'Profit', data = sales, kind = 'bar', aspect= 10/5)


# # DISTRIBUTION PLOT FOR PROFIT

# In[30]:


sns.distplot(sales.Profit)


# Highest density of profit lies between -77 to 180

# # SALES VS CUSTOMER SEGMENT

# In[31]:


sns.relplot('Customer_Segment', 'Sales', data = sales, kind = 'line')


# Though the highest number of purchases are from Corporate Sector, the highest sales are from Home Office Segment.

# # PROFIT VS PRODUCT CATEGORY

# In[33]:


sns.relplot('Product_Category', 'Profit', data = sales, kind = 'line')


# As observed, highest sales and profit are from Technology products.

# In[34]:


sns.pairplot(sales)


# In[ ]:




