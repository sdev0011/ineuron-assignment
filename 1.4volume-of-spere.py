''' Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r3 '''
from math import pi

def volume_of_spere(dimeter):
    radius = dimeter/2
    volume = 4/3 * (pi * pow(radius,3))
    return volume

print(volume_of_spere(12))

########## output #######
#### 904.7786842338603###