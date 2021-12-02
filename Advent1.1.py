with open('input1.1.txt') as f:
    inputlist = f.readlines()
inputlist = list(map(int,(map(lambda s: s.strip(), inputlist))))
higherCounter = 0
for i in range(0,len(inputlist)):
        if inputlist[i] > inputlist[i-1]:
            higherCounter += 1 
print(higherCounter)