import numpy as np
import time
import re
start_time = time.time()

stacksPassed = False
stack = []
stackArrange=[]
indexStart = 0

with open('2022/input5_1.txt') as f:
    inputlist = f.readlines()

for i in range(0,len(inputlist)): #readStacks
      if(inputlist[i] == '\n' and stacksPassed==False):
          stacksPassed = True  
      if(stacksPassed==False):
          stack.append(inputlist[i].strip('\n'))
      if(stacksPassed==True):
          indexStart=i #start of Steps
          break        
for i in range(len(stack)-1,-1,-1): #rearrange list-elements 
          stackArrange.append(stack[i].replace('    ',' ').split(' '))
stackArrange[0] = [value for value in stackArrange[0] if value!= '']
stacky = np.array(stackArrange)
stacky = stacky.T
stacky.tolist()
stackylist=[]

for row in stacky:
       stackylist.append([val for val in row.tolist() if val !='']) #remove ''
stackylist2=stackylist

for i in range(indexStart+1,len(inputlist)-1):
    steps = list(map(int,re.findall(r'\d+',inputlist[i]))) #get steps as numbers 0,1,2
    
    stackylist2[steps[2]-1].extend(stackylist2[steps[1]-1][-steps[0]:]) 
    
    for j in range(0,int(steps[0])):
      stackylist[steps[2]-1].append(stackylist[steps[1]-1].pop()) #pop last element and append to new spot
      if(len(stackylist2[steps[1]-1]) > 1):
            stackylist2[steps[1]-1].pop()

for k in stackylist:
    print(k)
for k in stackylist2:
    print(k)
      

print("-- %s seconds --" % (time.time() - start_time))
#-- 0.00500178337097168 seconds --