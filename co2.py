# This is just a simple test of the transport_c02 api
# March 26, 2021 (11:24 pm)

# Cleaning up the code by removing redundancies.
# March 27, 2021 (8:23 pm)

from transport_co2 import Mode
list(Mode)
import maps

# Constructor to call in the frontend
def __init__(self,passengers,carSize,mode,map):
    self.passengers = passengers
    self.carSize = carSize
    self.mode = mode
    self.totalEmissions = 0
    self.map = map

# Method used to retrieve the total emissions using a given distance.
# Current only works with small cars.
def tripEmissions(self):
    sizeOfCar = self.carSize
    tripCO2 = Mode.sizeOfCar.estimate_co2(distance_in_km = self.map.getDistance(), occupancy = self.passengers)
    self.totalEmissions += tripCO2 
    return (tripCO2)

# Method used to return the total emissions per 100 km. Recall thta 
# this currently only works for small cars.
def averageEmissions(self):
    sizeOfCar = self.carSize
    return ((Mode.sizeOfCar.estimate_co2(distance_in_km= self.map.getDistance(), occupancy = self.passengers))/100)

def getTotalEmissions(self):
    return self.totalEmissions
