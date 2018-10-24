
# coding: utf-8



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

