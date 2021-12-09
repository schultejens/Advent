from numpy.lib.function_base import append
from own_tools import get_strings
import numpy as np

inputlist = list(map(int,get_strings("2021/input7.txt")[0].split(',')))
numpy = np.sort(np.array(inputlist))

#https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Summenformel
def calculateFuel(number):
    return (number**2 + number) / 2

fuelCosts = []
fuelCost = 0
for number in numpy:
    fuelCost = 0
    for i in range(0, len(numpy)):
        if(number < numpy[i]):
            fuelCost += calculateFuel(numpy[i]-number)
        if(number > numpy[i]):
            fuelCost += calculateFuel(number-numpy[i])
        if(number == numpy[i]):
            pass
    fuelCosts.append(fuelCost)
    
print(min(fuelCosts))