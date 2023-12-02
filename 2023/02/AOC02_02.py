import numpy as np
file1 = open('input', 'r')
Lines = file1.readlines()

finVal = 0
colors = {'green':0,'red':0,'blue':0}
for line in Lines:
    line = line.split("\n")[0]
    line = line.split(": ")[1].split(";")

    for i in line:
        sets = i.split(",")
        for set in sets:
            count, color = set.strip().split(" ")
            colors[color] = int(max(colors[color],int(count)))

    values = colors.values()
    finVal += np.prod(np.array(list(colors.values())))
    colors = { x:0 for x in colors}

print(finVal)