# This is just a simple test of the transport_c02 api
# March 26, 2021 (11:24 pm)

# Import Mode from the library
from transport_co2 import Mode
list(Mode)

# Print out the total emissions for a small car in 100 kms.
print (Mode.SMALL_CAR.estimate_co2(distance_in_km=100))

#Output: 11200.0
