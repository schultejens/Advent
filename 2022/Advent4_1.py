import time
import re
start_time = time.time()

with open('2022/input4_1.txt') as f:
    inputlist = f.read().splitlines()
sum=0
 
#Part1
for i in range(0,len(inputlist)):
   numbers = list(map(int,re.findall(r'\d+',inputlist[i]))) #13-30,40-50
   set1 = set(range(numbers[0],numbers[1]+1))
   set2 = set(range(numbers[2],numbers[3]+1))
   if (set1.issubset(set2) | set1.issuperset(set2)): #Subsets or Supersubsets of each other
       sum +=1
print(sum)

#Part2
sum=0
for i in range(0,len(inputlist)):
    numbers = list(map(int,re.findall(r'\d+',inputlist[i])))
    set1 = set(range(numbers[0],numbers[1]+1))
    set2 = set(range(numbers[2],numbers[3]+1))
    if (not set1.isdisjoint(set2)): #Contains atleast one matching number
       sum +=1
print(sum)

print("-- %s seconds --" % (time.time() - start_time))
#-- 0.01400446891784668 seconds --