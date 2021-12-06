from collections import deque
from own_tools import get_strings

input = get_strings("input.txt")
inputlist = input[0].split(',')



def start_new_day(fishies):
        #"0" Sekunden entfernen, rest der Liste "rueckt" nach vorne
       buffer = fishies.popleft()
       #aktuelle 6 Sekunden Fische dann mit den "entfernten" addieren
       fishies[6] += buffer
       #die neu entstandenen 8 Sekunden Fische hinzufügen (vorher 0 Sek)
       fishies.append(buffer)
        

def initialise_first_fishies(inputlist):
    fishies = []
    fishies.append(0)
    fishies.append(sum(p == '1' for p in inputlist))
    fishies.append(sum(p == '2' for p in inputlist))
    fishies.append(sum(p == '3' for p in inputlist))
    fishies.append(sum(p == '4' for p in inputlist))
    fishies.append(sum(p == '5' for p in inputlist))
    fishies.append(0)
    fishies.append(0)
    fishies.append(0)
    fishies = deque(fishies)

    print('start',fishies)
    return fishies

#Queue Erstellen
fishies = initialise_first_fishies(inputlist)

#Tage durchlaufen
for i in range(0,256):
    start_new_day(fishies)

#Anzahl der Fische in einzelnen List-Indizees addieren
amount = 0
for i in range(0,len(fishies)):
    amount = amount + fishies[i]

#YEA
print('end', fishies)
print("Fishies :", amount)
