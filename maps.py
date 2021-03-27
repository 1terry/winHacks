import requests
import json

# enter your api key here
api_key ='Your_api_key'
  
# Take source as input

source = input()
  
# Take destination as input
dest = input()
  
# url variable store url 
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
  
# Get method of requests module
# return response object
r = requests.get(url + 'origins = ' + source +
                   '&destinations = ' + dest +
                   '&key = ' + api_key)
                     
# json method of response object
# return json format result
x = r.json()
  
# by default driving mode considered
  
# print the value of x
print(x)