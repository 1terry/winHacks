# This is a simple test of the Google Maps API.
# March 26, 2021 (11:29 pm)

# Made changes to finalize the program's functionality by removing redudant code and dependencies.
# March 27, 2021 (8:18 pm)

import requests
import json 

# API key to allow access to the Google Maps Distance Matrix API.
key = "AIzaSyD5S_QsivrbmGtWzjs6Hp7r3YcQi5GInbE"
api_key = key
  
# Constructor for source and dest
def __init__(self, source, dest):
    self.source = source
    self.dest = dest

# Source and destination. This should be read from the calling frontend.
source = "Toronto"
dest = "London"
  
# Url variable to store the url of the distance matrix.
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
  
# Grabbing the updated url with the given arguments.
r = requests.get(url + 'origins = ' + source + '&destinations = ' + dest + '&key = ' + api_key)

# json method of response object
# return json format result
x = r.json()

# Method used to calculate the distance between the source and destination.
def getDistance():
    
    # Inelegant for loop to find the distance metric.
    for key in x:
        if (key == "rows"):
            
            # Formatting the string to make sure that it is acceptable as an integer.
            distance = (x[key][0]['elements'][0]['distance']['text']).split("km")
            distance = (str("").join(distance))
            distance, randomHoldingString = distance.split(",")
            distance = distance + randomHoldingString
            distance = int(distance)
            
    return distance # Return the value as an integer.






