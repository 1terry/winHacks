# This is a simple test of the Google Maps API.
# March 26, 2021 (11:29 pm)

import requests
import json 

# enter your api key here
key = "AIzaSyD5S_QsivrbmGtWzjs6Hp7r3YcQi5GInbE"
api_key = key
  
# Take source as input

source = "Toronto"
  
# Take destination as input
dest = "London"
  
# url variable store url 
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
  
# Get method of requests module
# return response object

#r = requests.get(url + 'origins = ' + source + '&destinations = ' + dest + '&key = ' + api_key)


r= requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&key=AIzaSyD5S_QsivrbmGtWzjs6Hp7r3YcQi5GInbE")

# json method of response object
# return json format result
x = r.json()

# by default driving mode considered
def getDistance():
    a = 100
    return a

# Grabbing the distance from the json file as a string. This is fairly inelegant and not that great; may need to be changed later.
for key in x:
    if (key == "rows"):
        print (x[key][0]['elements'][0]['distance']['text'])

# print the value of x
print(x)



