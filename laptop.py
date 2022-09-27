#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Flipkart Laptop Scrapping

# In[100]:


from  bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
URL = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'

# Requesting Flipkart URl
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')
containers = soup.findAll('div',{'class':'_2kHMtA'})

laptopList = list() # list which will contain each laptop name and details

for i in containers:
    product = i.find('div',{'class':'_4rR01T'})
    ProductName = product.text.split('-')[0].strip()
    
    star = i.find('div',{'class':'_3LWZlK'}) 
    try: Star = star.text
    except: Star = star
    
    
    try:
        Rating = i.find('span',{'class':'_2_R_DZ'})        
        Ratings = Rating.text.split('&')[0].replace(',','')
        Reviews = Rating.text.split('&')[1]
    except: Ratings = Reviews = ''

    Price = i.find('div',{'class':'_30jeq3 _1_WHN1'}).text.replace(',',' ').replace('₹','')
    
    info = i.findAll('li',{'class':'rgWa7D'})
    Proccesor = info[0].text
    RAM = info[1].text    
    Op_System = info[2].text
    SSD = info[3].text
    Display = info[4].text
    
    Image = i.img
    ImagesURL = Image.get('src')
    
    laptopList.append([ProductName,Star,Ratings,Reviews,Price,Proccesor,RAM,Op_System,SSD,Display,ImagesURL])
    
    
    
df = pd.DataFrame(laptopList, columns = ['ProductName','Star','Ratings','Reviews','Price','Proccesor','RAM','Op_System','SSD','Display','ImagesURL'])
df
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




