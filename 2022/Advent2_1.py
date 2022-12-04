import time
start_time = time.time()

with open('2022/input2_1.txt') as f:
    inputlist = f.read().splitlines()
sump1=0
sump2=0
#P1 
dict = {
    "A Y": 8,"B Z": 9,"C X": 7, #wins
    "A X": 4,"B Y": 5,"C Z": 6, #draws
    "X": 1,"Y":2,"Z":3 #loss
}
#P2 X Loose, Y Draw, Z Win
dict2 = {"A X":3, "A Y":4, "A Z":8, 
         "B X":1, "B Y":5, "B Z":9,
         "C X":2, "C Y":6, "C Z":7
         }
#P1
for i in range(0,len(inputlist)):
    sump1+=dict.get(inputlist[i],dict.get(inputlist[i].split(' ')[1]))
    sump2+=dict2.get(inputlist[i],dict.get(inputlist[i].split(' ')[1]))      
print(sump1)
print(sump2)
print("-- %s seconds --" % (time.time() - start_time))
#-- 0.003000497817993164 seconds --