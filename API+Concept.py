
# coding: utf-8

# 

# In[1]:

import requests

A = 'http://api.openweathermap.org/data/2.5/weather?appid=aee5a6e361255c98ca66fd264305f490&q='
city = input("City Name : ")
url = A + city
json_data = requests.get(url).json()
print(json_data)


# In[2]:

import requests

A = 'http://api.openweathermap.org/data/2.5/weather?appid=aee5a6e361255c98ca66fd264305f490&q='
city = input("City Name : ")
url = A + city
json_data = requests.get(url).json()
B = json_data['main']['temp']
B = B - 273.15
print("Degree Celsius Temprature: ",B)


# In[38]:

import requests

A = 'https://developers.zomato.com/api/v2.1/restaurant?res_id=16774318'
#B = input("Rest Name : ")
#url = A+B
json_data = requests.get(A).json()
print(json_data)


# In[56]:

import urllib.request
import json
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCWNV6meqczlJL9BL7VtT3YsgR920x9hVI'
origin =input('where are you?: ').replace('','+')
destination = input('where do you want to go?: ').replace('','+')

nav_request= 'origin={}&destination={}&key={}'.format(origin,destination,api_key)

request = endpoint + nav_request 
response =urllib.request.urlopen(request).read()
directions = json.loads(response)
print(directions)


# In[61]:

directions.keys()


# In[64]:

routes = directions['routes']
routes[0].keys()


# In[76]:

routes[0]['legs']


# In[82]:

legs = routes[0]['legs']
print("Distance: ",legs[0]['distance']['text'])
print("Time: ",legs[0]['duration']['text'])


# In[ ]:



