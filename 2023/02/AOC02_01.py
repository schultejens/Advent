import numpy as np
file1 = open('input', 'r')
Lines = file1.readlines()

game = 1
possibleGames = []
colorTemplate = {'green':0,'red':0,'blue':0}
colors = colorTemplate
for line in Lines:
    line = line.split("\n")[0]
    line = line.split(": ")[1].split(";")

    for i in line:
        sets = i.split(",")
        for set in sets:
            count, color = set.strip().split(" ")
            colors[color] = int(max(colors[color],int(count)))
    if (colors.get('red') <= 12 and colors.get('green') <= 13 and colors.get('blue') <= 14):
        possibleGames.append(game)
        colors = { x:0 for x in colors}
    else:
        colors = { x:0 for x in colors}
    game+=1
fin = np.array(possibleGames)
fin = np.unique(fin)
print(np.sum(fin))