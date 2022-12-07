import numpy as np
import time
start_time = time.time()
with open('2022/input6_1.txt') as f:
    inputlist = f.readlines()
    
string = inputlist[0]

windowSizeP1=4
windowSizeP2=14
FoundFour = False

for i in range(0,len(string)):
     if(len(string[i:windowSizeP1+i]) == len(set(string[i:windowSizeP1+i])) and FoundFour==False):
         print(i+windowSizeP1,string[i:windowSizeP1+i]) #P1
         FoundFour=True
     if(len(string[i:windowSizeP2+i]) == len(set(string[i:windowSizeP2+i])) and FoundFour==True):
         print(i+windowSizeP2,string[i:windowSizeP2+i]) #P2
         break

print("-- %s seconds --" % (time.time() - start_time))
#-- 0.00700068473815918 seconds --