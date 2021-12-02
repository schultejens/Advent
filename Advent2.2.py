with open('input2.1.txt') as f:
    inputlist = f.readlines()

#Input konvertieren
inputlist = list((map(lambda s: s.strip(), inputlist)))
direction, amount = zip(*(s.split(' ') for s in inputlist))
amount = list(map(int,amount))

horizontal = 0
depth = 0
aim = 0

for i in range(0,len(inputlist)):
    if direction[i] == 'forward':
        horizontal += amount[i]
        depth += (aim*amount[i])
    if direction[i] == 'up':
        aim -= amount[i]
    if direction[i] == 'down':
        aim += amount[i]

print(horizontal*depth)