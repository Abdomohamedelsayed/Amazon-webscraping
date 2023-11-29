#!/usr/bin/env python
# coding: utf-8

# In[16]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


<table class="wikitable sortable jquery-tablesorter">
<caption>


# In[6]:


table = soup.find_all('table')[1]


# In[7]:


print(table)


# In[11]:


world_titles = table.find_all('th')


# In[13]:


table_world_titles = [titel.text.strip() for titel in world_titles]


# In[23]:


df = pd.DataFrame(columns = table_world_titles)


# In[27]:


column_data = table.find_all('tr')


# In[31]:


column_data


# In[33]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[29]:


df


# In[30]:


df.to_csv(r'C:\Users\asus\OneDrive\سطح المكتب\Portfolioproject\companies.csv', index = False)


# In[ ]:




