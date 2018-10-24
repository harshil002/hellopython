
# coding: utf-8

# In[36]:

from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver/chromedriver') #I actually used the chromedriver and did not test firefox, but it should work.
profile_link="https://www.linkedin.com/in/johnsmith1"
driver.get(profile_link)
html=driver.page_source
soup=BeautifulSoup(html) #specify parser or it will auto-select for you
summary=soup.find('section', { "id" : "summary" })
print(summary.getText())


# In[64]:

Client_ID = '78r005pxsjy8y6'     # This is api_key
Client_SECRET = 'GhS3B6qcmRLJdaER'   # This is secret_key

# USER_TOKEN = '27138ae8-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXb'   # This is oauth_token
# USER_SECRET = 'ca103e23-XXXXXXXXXXXXXXXXXXXXXXXX7bba512625e'   # This is oauth_secret
RETURN_URL = 'http://localhost:8000'

from linkedin import *
from oauthlib import *

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

# Instantiate the developer authentication class

authentication = linkedin.LinkedinAPI(Client_ID, Client_SECRET, RETURN_URL)

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

g = application.get_profile()
print(g)


# In[70]:

import inspect
# for name, obj in inspect.getmembers(linkedin):
#     if inspect.isclass(obj):
#         print(obj)

for name, obj in inspect.getmembers(LinkedinAPI):
    if inspect.isattribute(obj):
        print(obj)


# In[19]:

get_ipython().system('pip3 install python3-linkedin')


# In[35]:

import linkedin
from linkedin import *

Client_ID = '78r005pxsjy8y6'     
Client_SECRET = 'GhS3B6qcmRLJdaER'

g = linkedin.LinkedinAPI( "Client_ID", "Client_SECRET")
A=g.get_profile()
print(A.getText())


# In[76]:

import linkedin
from linkedin import *
import bs4 as bs
from bs4 import BeautifulSoup

A="https://www.linkedin.com/in/johnsmith1"

soup=BeautifulSoup(profile_link)

Client_ID = '78r005pxsjy8y6'     
Client_SECRET = 'GhS3B6qcmRLJdaER'
g = linkedin.LinkedinAPI( "Client_ID", "Client_SECRET")

B="https://api.linkedin.com/v2/me"
soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml')
for i in soup.find_all('p', class_="pv-top-card-section__summary-text text-align-left mt4 ember-view"):
    print(i.text)
# print(A.text())
# print(A.text())
# summary=soup.find_all('section', { "id" : "summary" })
# print(summary.getText())


# In[26]:

import json, requests, pandas as pd
from requests_oauthlib import OAuth2Session
#from linkedin import *

CONSUMER_KEY = "78r005pxsjy8y6"
CONSUMER_SECRET = "GhS3B6qcmRLJdaER"
RETURN_URL = "http://localhost:8080"

linkedin = OAuth2Session(CONSUMER_KEY, redirect_uri=RETURN_URL)

authorization_url, state = linkedin.authorization_url("https://www.linkedin.com/oauth/v2/authorization")

print(authorization_url)


# In[27]:

auth_code = "AQQpNHoSxOctjIamfK-fm3-0PPbcehv_X7zrYPqYielYYJqP5S6-8CacOUVJbsUnVwzZQt3WW1zS2x-X3dEAlOfs98koNV7RE-TnU1zgVWvZxZP_UkcxBJJriTb4Ifab0VzsjfHbzjnsB6Oq4yWmknx5w5k2w7IXk64p5aGhKG6eC12uPRa0PPic_xm__w"
state="Il8vp1IZsSAjV7tCVcBV4l5LrIVApn"
linkedin.fetch_token('https://www.linkedin.com/oauth/v2/accessToken', client_secret=CONSUMER_SECRET, code=auth_code)
response = linkedin.get('https://api.linkedin.com/v2/people/~?{email:'+x+'}&format=json')
# emails = {'athadani@stevens.edu','satyathadani@gmail.com'}
# reslist = []
# for x in emails:
#     response = linkedin.get('https://api.linkedin.com/v2/people/~?{email:'+x+'}&format=json')
#     if response.status_code==200:
#         print(response.content)
#         reslist.append(json.loads(response.content))
#     else:
#         continue

# #df = pd.DataFrame("\n".join(reslist))

#print(application.get_connections)
print(response.status_code)


# In[29]:

response = linkedin.get('https://api.linkedin.com/v1/people/~?{email:'+x+'}&format=json')
# emails = {'athadani@stevens.edu','satyathadani@gmail.com'}
# reslist = []
# for x in emails:
#     response = linkedin.get('https://api.linkedin.com/v2/people/~?{email:'+x+'}&format=json')
#     if response.status_code==200:
#         print(response.content)
#         reslist.append(json.loads(response.content))
#     else:
#         continue

# #df = pd.DataFrame("\n".join(reslist))

#print(application.get_connections)
print(response.status_code)
print(response.content)

