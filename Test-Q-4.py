#!/usr/bin/env python
# coding: utf-8

#  ** Write a python script for extracting the following attributes in a product url, for example https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438
#  
# - ProductName and Description
# - Size
# - Ingredients
# - Images (all image location hrefs)
# - Categories
# - Key Benefits
# - Brand (Manufacture)
# - Price (for each packaging size)
# 
# 

# In[3]:


pip install fake-useragent


# In[11]:


# Import Required Libraries
import requests      #send request to HTML page
import bs4
from bs4 import BeautifulSoup     #python library for extracting data

from fake_useragent import UserAgent

import pandas as pd                #Further Analysis of the extracted Data
import seaborn as sns
import matplotlib.pyplot as plt


# In[12]:


# Initialization of the lists to store the extracted data
# The data that we extract is unstructured data. So we’ll create empty lists to store them in a structured form,
count=0                  # Intialize search row count
products=[]              #List to store name of the product
#prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
#specifications = []     #List to store specifications of the product
ProductName_Description = []                 #List to store ProductName_Description sspecifications of the product
Size = []                 #List to store ssize specifications of the product
Ingredients= []                  #List to store Ingredients specifications of the product
Images = []                  #List to store images specifications of the product
Categories = []             #List to store Categories specifications of the product
Key_Benefits = []          #List to storeKey Benefits specifications of the product     
Brand  = []               #List to brand specifications of the product 
price = []                #List to price Categories specifications of the product
df=pd.DataFrame()        #Initialize Dataframe


# In[13]:


# Creating an User agent  pip insatll fake-useragent
# A User agent acts as a bridge between the user and the internet . 
# It gives the webserver necessary information about our browser, software, device type and etc.
# According to this information the web servers can display different webpages for us
# The web server uses this information to adapt the content to specific web browsers and different foods specifications 
# https://pypi.org/project/fake-useragent/    
# read here
 
user_agent = UserAgent() # Dummy User Agent
print(user_agent)


# In[14]:


# Set the product name. we are searching for laptops
# The extracted data will be related to that product.\ # Search for Laptops
product_name = 'AdultFood'


# In[15]:


#Find Elements by ID
#To extract data from multiple pages of the product listing we’re going to use a for loop.
# The range will specify the number of pages to be extracted

#url = "https://www.chewy.com/search?q={0}&page={1}" 
#print( url.format(products,1))           
url="https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438"
print(url.format(product_name,1))    #run and check this 


# In[ ]:


for i in range(1,3): # Limiting search to 3 pages due to multiple redirection issues for higher number of pages
    url = "https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438" # Scrape data from chewy.com
    url = url.format(product_name,i)
    print(url)
    
    ## Getting the reponse from the page using get method of requests module
    #page= requests.get(url, headers ={"User_agent": user_agent.chrome})
    page= requests.get(url)
    print(page)
    
    ## Storing the content of the page in a variable
    html=page.content
    print(html)
    
    # To Extract data from html file --- Creating BeautifulSoup object
    page_soup=bs4.BeautifulSoup(html, "html.parser")
    
    print(page_soup.prettify())     #will show as a nested html file
    #it gives the visual representation of the parse tree created from the raw HTML content.

    
    #Iterate over page_soup.find_all('p')   
    # this will iterate over all paras
    print(page_soup.find_all('p')[0].get_text())

    
    ## Decoding the tags
    #('a',{'class':'_cw-desktop'})

    for containers in page_soup.findAll('a',{'class':'alt-image dark-bg no-expand-thumbnails mz-thumb'}): 
       # <a href="#search-autocomplete" class="sfw-header__skip-link">Skip to search</a>
        #<a href="#search-autocomplete" class=>Skip to search</a>
        name=containers.find('div', attrs={'class':'img-wrap'})
        
        price=containers.find('div', attrs={'class':'js-tracked-promo dotcms-include brand-tiles'})
        
        rating=containers.find('nav', attrs={'class':'sfw-header_wrapper chirp-sfw'})
        
        specification = containers.find('div', attrs={'class':'cms-include'})
        
        ## Splitting integrated specification into individual CPU, RAM, OS, HDD and Display specifications
        for col in specification:
            col=col.find_all('a', attrs={'class':'cw-desktop'})
            ProductName_Description = col[0].text                 #List to store ProductName_Description sspecifications of the product
            Size =col[1].text                 #List to store ssize specifications of the product
            Ingredients=col[2].text                  #List to store Ingredients specifications of the product
            Images = col[3].text                  #List to store images specifications of the product
            Categories =col[4].text              #List to store Categories specifications of the product
            Key_Benefits = col[5].text          #List to storeKey Benefits specifications of the product     
            Brand  = col[6].text               #List to brand specifications of the product 
            price = col[7].text   
        
        products.append(Name.text) # Add product name to list
        
        prices.append(price.text) # Add price to list
        
        #specifications.append(specification.text) if type(specification) == bs4.element.Tag  else specifications.append('NaN')
        
        Prd,append(pde) # Add ProductName_Description specifications to list
        
        si.append(siz) # Add Size specifications to list
        
        ind.append(ing) # Add ingredients specifications to list
        
        im.append(img) # Add Images specifications to list
        
        cate.append(cte) # Add Categories to list
        
        kb.append(keb) # Add Key Benefits specifications to list
        
        br.append(brn) # Add brand specifications to list
        
        pr.append(pcr) # Add price specifications to list
        
        rat.append(rating.text) if type(rating) == bs4.element.Tag  else ratings.append('NaN') # Add Rating to list
        
        count=count+1 # Increment row count
    
    ## Create a dataframe with structured data from all searched rows
    df = pd.DataFrame({'product_name':products,'ProductName_Description':prd,'Size':si,'Ingredients':im,'Categories':cate,'Key Benefits':kb,'Brand':br,'Price':pr})

print('No. of rows searched',count)


# In[ ]:





# In[ ]:





# In[ ]:




