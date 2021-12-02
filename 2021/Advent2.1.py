with open('2021/input2.1.txt') as f:
    inputlist = f.readlines()

#Input konvertieren
inputlist = list((map(lambda s: s.strip(), inputlist)))
direction, amount = zip(*(s.split(' ') for s in inputlist))
amount = list(map(int,amount))

horizontal = 0
depth = 0

for i in range(0,len(inputlist)):
    if direction[i] == 'forward':
        horizontal += amount[i]
    if direction[i] == 'up':
        depth -= amount[i]
    if direction[i] == 'down':
        depth += amount[i]

print(horizontal)
print(depth)
print(horizontal*depth)