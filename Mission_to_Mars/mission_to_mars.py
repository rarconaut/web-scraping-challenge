#!/usr/bin/env python
# coding: utf-8

# In[70]:


# Dependencies
import requests
from bs4 import BeautifulSoup


# In[71]:


# Import Splinter and set the chromedriver path
from splinter import Browser


# In[ ]:


# Success - the page content is being loaded by javascript, so we have to wait for that before we can actually scrape
# the page. If you use splinter to scrape the page, you can use:
browser.is_element_visible_by_css('<element css>', wait_time=10)
# Before using:
html=browser.html
# The ten second buffer seems to be enough for the page to load all the way before using beautiful soup to scrape it.


# # NASA Mars News
# https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

# In[72]:


# Initialize browser
executable_path = {"executable_path": "/Users/tahoe/.wdm/drivers/chromedriver/win32/86.0.4240.22/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

# Visit the following URL
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)

# We have to wait for the page to load before we can scrape it. If you use splinter to scrape, you can use:
browser.is_element_visible_by_css('<element css>', wait_time=3)

# Scrape the browser into soup and use soup to find the latest News Title and Paragraph Text. 
# Assign the text and image to variables that you can reference later.
# Save the image url to a variable called `img_url`
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

img_url = "https://mars.nasa.gov" + soup.find("div", class_="list_image").contents[0]["src"]
news_date = soup.find("div", class_="list_date").get_text()
news_title = soup.find("div", class_="content_title").get_text()
news_p = soup.find("div", class_="article_teaser_body").get_text()

browser.quit

print(f'Date: {news_date}, Title: {news_title}, Subtitle: {news_p}, {img_url}')


# # JPL Mars Space Images - Featured Image
# https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

# In[85]:


# Initialize browser
executable_path = {"executable_path": "/Users/tahoe/.wdm/drivers/chromedriver/win32/86.0.4240.22/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

# Visit the JPL Mars Space Images URL
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)

# We have to wait for the page to load before we can scrape it. If you use splinter to scrape, you can use:
browser.is_element_visible_by_css('<element css>', wait_time=3)

# Design an XPATH selector to grab the Featured Image 'FUlL IMAGE' button
xpath = '//footer//a'

# Use splinter to Click the 'more info' button
# to bring up the full resolution image
results = browser.find_by_xpath(xpath)
img = results[0]
img.click()

# Use splinter to Click the 'more info' button
# to bring up the full resolution image
results = browser.links.find_by_partial_text('more info')
img = results[0]
img.click()


# Use splinter to navigate the site and find the image url for the current Featured Mars Image 
# and assign the url string to a variable called featured_image_url
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

featured_image_url = "https://www.jpl.nasa.gov" + soup.find("img", class_="main_image").attrs['src']

browser.quit

print(xpath, featured_image_url)


# # Mars Facts
# https://space-facts.com/mars/

# In[37]:


# Scrape table with Pandas read_html
import pandas as pd


url = "https://space-facts.com/mars/"
mars_table = pd.read_html(url)
mars_table


# In[38]:


type(mars_table)


# In[39]:


mars_table1_df = mars_table[0]
mars_table2_df = mars_table[1]
mars_table1_df 
mars_table2_df


# In[40]:


# Use Pandas to_html method to generate HTML tables from DataFrames
html_mars_table1 = mars_table1_df.to_html()
html_mars_table2 = mars_table2_df.to_html()
html_mars_table1


# In[88]:


html_mars_table1.replace('\n', '')
html_mars_table2.replace('\n', '')
html_mars_table2


# # Mars Hemispheres
# https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

# In[ ]:


# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]


# In[96]:


# Initialize browser
executable_path = {"executable_path": "/Users/tahoe/.wdm/drivers/chromedriver/win32/86.0.4240.22/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

# Visit the JPL Mars Space Images URL
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
# browser.window.is_current = True     # set this window to be current window

# We have to wait for the page to load before we can scrape it. If you use splinter to scrape, you can use:
browser.is_element_visible_by_css('<element css>', wait_time=3)

# Save both the image url for the full resolution hemisphere image, and the title containing the hemisphere name. 
# Use a Python dictionary to store the data using the keys img_url and title
hemisphere_image_urls = []
links = [0,1,2,3]
for link in links:

    # Use splinter to Click the "Mars in natural color in 2007" image 
    # to bring up the full resolution image
    results = browser.links.find_by_partial_text('Hemisphere Enhanced')
    img = results[link]
    hemi_title = img['h3']
    img.click()

    # Use splinter to navigate the site and find the image url for the current Featured Mars Image 
    # and assign the url string to a variable called featured_image_url
    browser.is_element_visible_by_css('<element css>', wait_time=2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemi_url = soup.find("a", text="Original").attrs['href']
     
    
    hemisphere_image_urls.append({"title": hemi_title, "img_url": hemi_url})
    
    
    
    browser.back()
    
# window.close()    

browser.quit

hemisphere_image_urls


# In[ ]:




