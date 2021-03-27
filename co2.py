# This is just a simple test of the transport_c02 api
# March 26, 2021 (11:24 pm)

# Import Mode from the library
from transport_co2 import Mode
list(Mode)
import maps
# Print out the total emissions for a small car in 100 kms.

#constructor to call in the frontend
def __init__(self,passengers,carSize,mode):
    self.passengers = passengers
    self.carSize = carSize
    self.mode = mode



# Testing the output from the function in the maps class.
print (Mode.SMALL_CAR.estimate_co2(distance_in_km=maps.getDistance()))

#Output: 11200.0
