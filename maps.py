# This is a simple test of the Google Maps API.
# March 26, 2021 (11:29 pm)

# Made changes to finalize the program's functionality by removing redudant code and dependencies.
# March 27, 2021 (8:18 pm)

# Adapted the code to work with coordinates and included some error validation (negative distance).
# March 27, 2021 (10:06 pm)

 # Full opp functionality according to python's specifications.
 # March 27, 2021 (10:34 pm)

import requests
import json 

# API key to allow access to the Google Maps Distance Matrix API.
key = "AIzaSyD5S_QsivrbmGtWzjs6Hp7r3YcQi5GInbE"
api_key = key

# Constructor for source and dest
def __init__(self, sourceLat, sourceLong, destLat, destLong):
    self.sourceLat = sourceLat
    self.sourceLong = sourceLong
    self.destLat = destLat
    self.destLong = destLong

# Method used to calculate the distance between the source and destination.
def getDistance(self):
    
    try:
        # Url variable to store the url of the distance matrix.
        url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
        
        # Grabbing the updated url with the given arguments.
        r = requests.get(url + '&origins=' + self.sourceLat + ',' + self.sourceLong + '&destinations=' + self.destLat + ',' + self.destLong + '&key=' + api_key)

        # json method of response object
        # return json format result
        x = r.json()

        # Inelegant for loop to find the distance metric.
        for key in x:
            if (key == "rows"):
            
                # Formatting the string to make sure that it is acceptable as an integer.
                distance = (x[key][0]['elements'][0]['distance']['text']).split("km")
                distance = (str("").join(distance))
                distance = float(distance)
            
        return distance # Return the value as an integer

    except KeyError:
        return (-1) # Return -1. If the value is negative we know there is an error.
        


#<web>: <rake jobs:work>

