import numpy as np
import time
start_time = time.time()
calories = []
caloriebuffer = 0

with open('2022/input1_1.txt') as f:
    inputlist = f.readlines()

for i in range(0,len(inputlist)):
    if(inputlist[i] == '\n'):
        calories.append(caloriebuffer)
        caloriebuffer = 0
        continue
    caloriebuffer += int(inputlist[i])     
    
calories = np.array(calories)
print(np.max(calories))
calories2 = np.argsort(-calories,axis=0)[:3]
print (calories[calories2[0]]+calories[calories2[1]]+calories[calories2[2]])
print("-- %s seconds --" % (time.time() - start_time))