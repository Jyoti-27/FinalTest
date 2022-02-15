#!/usr/bin/env python
# coding: utf-8

# * How do you extract categories of dog food from the page (https://www.chewy.com/b/dog-288). Explain and write a python script.
# 
# * write a python script to get each product url in for dog food , wet-food category (https://www.chewy.com/b/dog-288)
# 
# * write a function to detect how many pages of products in a category. So given the category url the function should output the number of pages

# In[1]:


pip install fake-useragent


# In[7]:


# Import Required Libraries
import requests      #send request to HTML page
import bs4
from bs4 import BeautifulSoup     #python library for extracting data

from fake_useragent import UserAgent

import pandas as pd                #Further Analysis of the extracted Data
import seaborn as sns
import matplotlib.pyplot as plt


# In[8]:


# Initialization of the lists to store the extracted data
# The data that we extract is unstructured data. So we’ll create empty lists to store them in a structured form,
count=0                  # Intialize search row count
products=[]              #List to store name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
#specifications = []     #List to store specifications of the product
buscuits_cookies_crunchyTreats = []                 #List to store buscuits_cookies_crunchyTreatsspecifications of the product
soft_chewyTreats = []                 #List to store soft_chewyTreats  specifications of the product
dentalTreats = []                  #List to store dentalTreats specifications of the product
jerkytteats = []                  #List to store jerkytteats specifications of the product
bones_bullySticks_naturalChews = []             #List to store bones_bullySticks_naturalChewsspecifications of the product
df=pd.DataFrame()        #Initialize Dataframe


# In[9]:


# Creating an User agent  pip insatll fake-useragent
# A User agent acts as a bridge between the user and the internet . 
# It gives the webserver necessary information about our browser, software, device type and etc.
# According to this information the web servers can display different webpages for us
# The web server uses this information to adapt the content to specific web browsers and different foods specifications 
# https://pypi.org/project/fake-useragent/    
# read here
 
user_agent = UserAgent() # Dummy User Agent
print(user_agent)


# In[10]:


# Set the product name. we are searching for laptops
# The extracted data will be related to that product.\ # Search for Laptops
product_name = 'DogFood'


# In[11]:


# Find Elements by ID
#To extract data from multiple pages of the product listing we’re going to use a for loop.
# The range will specify the number of pages to be extracted

#url = "https://www.chewy.com/search?q={0}&page={1}" 
#print( url.format(products,1))           
url="https://www.chewy.com/b/dog-288"
print(url.format(product_name,1))    #run and check this 


# In[ ]:


for i in range(1,3): # Limiting search to 3 pages due to multiple redirection issues for higher number of pages
    url = "https://www.chewy.com/b/dog-288" # Scrape data from chewy.com
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

    for containers in page_soup.findAll('a',{'class':'_sfw-header__skip-link'}): 
       # <a href="#search-autocomplete" class="sfw-header__skip-link">Skip to search</a>
        #<a href="#search-autocomplete" class=>Skip to search</a>
        name=containers.find('div', attrs={'class':'department'})
        
        price=containers.find('div', attrs={'class':'bx-wrapper'})
        
        rating=containers.find('nav', attrs={'class':'sfw-header_wrapper chirp-sfw'})
        
        specification = containers.find('div', attrs={'class':'cms-include'})
        
        ## Splitting integrated specification into individual CPU, RAM, OS, HDD and Display specifications
        for col in specification:
            col=col.find_all('a', attrs={'class':'cw-desktop'})
            buscuits_cookies_crunchyTreats = col[0].text                #List to store buscuits_cookies_crunchyTreatsspecifications of the product
            soft_chewyTreats =col[1].text              #List to store soft_chewyTreats  specifications of the product
            dentalTreats = col[2].text                  #List to store dentalTreats specifications of the product
            jerkytteats = col[3].text                  #List to store jerkytteats specifications of the product
            bones_bullySticks_naturalChews = col[4].text            #List to store bones_bullySticks_naturalChewsspecifications of the product
            
            
        
        products.append(Name.text) # Add product name to list
        
        prices.append(price.text) # Add price to list
        
        #specifications.append(specification.text) if type(specification) == bs4.element.Tag  else specifications.append('NaN')
        
        bsc.append(bis) # Add buscuits_cookies_crunchyTreats specifications to list
        
        sct.append(che) # Add soft_chewyTreats specifications to list
        
        det.append(den) # Add dentalTreats specifications to list
        
        jet.append(jer) # Add jerkytteatsspecifications to list
        
        bls.append(bul) # Add bones_bullySticks_naturalChewsspecifications to list
        
        rat.append(rating.text) if type(rating) == bs4.element.Tag  else ratings.append('NaN') # Add Rating to list
        
        count=count+1 # Increment row count
    
    ## Create a dataframe with structured data from all searched rows
    df = pd.DataFrame({'product_name':products,'buscuits_cookies_crunchyTreats':bsc,'soft_chewyTreats':sct,'dentalTreats':det,'jerkytteats':jet,'bones_bullySticks_naturalChews':bls,'Price':prices,'ratings':rat,})

print('No. of rows searched',count)


# In[ ]:


For extracting data from soup we need to specify the html tags we want to retrieve the data from.
#We could use inspect element on the webpage.


# In[ ]:


#### Recap of the html tags
*p - A paragraph of text

*h1- A top-level heading

*h2, h3 - A lower-level heading

*li- An item in a list

*img - An image

*tr- A row in a table

*td - A cell in a table

*a - A link

*div - A block of space on the page (generic)

*span - A portion of text on the page (generic)

*meta - Information about the page that is not shown


# In[ ]:


### find() and find_all() function in Beautiful Soup
* To extract a single tag, we can instead use the find_all method, which will find all the instances of a tag on a page
* soup.find_all('p')    # this iwll iterate over all paras* soup.find_all('p')[0].get_text()
 
* Classes and ids are used by CSS to determine which HTML elements to apply certain styles to.
* We can also use them when scraping to specify specific elements we want to scrape. 


# In[ ]:


print(df.shape)
df.head() # Preview dataframe


# In[ ]:


df.tail() # Preview dataframe


# In[ ]:


df.isnull().sum() # Check for null values


# In[ ]:


df.isna().sum() # Check for 'NaN' values


# In[ ]:


df.info() # Dataframe Information


# In[ ]:


df.describe() # Describe Data before cleaning and dtype conversion


# In[ ]:


df.dtypes # Check data types of columns


# In[ ]:


df.shape


# In[ ]:


# Format Price column to remove ₹ and delimiter ',' used for the thousandth place 
df['Price'] = df['Price'].str.lstrip('₹')
df['Price'] = df['Price'].replace({',' : ''}, regex=True)
df.head() # Check if formatting is correct


# In[ ]:


df['Product Name'] = 'DogFood'
df.head()


# In[ ]:


df.head()
df.describe() # Describe Data after cleaning and dtype conversion


# In[ ]:


df.dtypes


# In[ ]:


df=df.drop(a, axis=1) # Drop rows with wrongly positioned data elements 


# In[ ]:


df.shape


# In[ ]:


# Format Price column to remove ₹ and delimiter ',' used for the thousandth place 
df['Price'] = df['Price'].str.lstrip('₹')
df['Price'] = df['Price'].replace({',' : ''}, regex=True)
df.head() # Check if formatting is correct


# In[ ]:


# Convert numeric columns in string format to float for mathematical and graphic operations
#for i in range(6,8,1):
#df.iloc[:,i]= df.iloc[:,i].astype(float).copy()

df.iloc[:,6]= df.iloc[:,6].astype(float)
df.iloc[:,7]= df.iloc[:,7].astype(float)


# In[ ]:


df.dtypes # Check data types of columns


# In[ ]:




