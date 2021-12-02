def sum_neighbors(list):
    new_list = []
    x = 1
    while x < len(list) - 1:
        new_list.append(list[x - 1] + list[x] + list[x + 1])
        x += 1
    new_list.append(list[x - 1] + list[x])

    return new_list

with open('input1.2.txt') as f:
    inputlist = f.readlines()
inputlist = list(map(int,(map(lambda s: s.strip(), inputlist))))
higherCounter = 0
print(inputlist)
inputlist = sum_neighbors(inputlist)
print(inputlist)
for i in range(0,len(inputlist)):
        if inputlist[i] > inputlist[i-1]:
            higherCounter += 1 
print(higherCounter)