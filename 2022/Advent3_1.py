with open('2022/input3_1.txt') as f:
    inputlist = f.read().splitlines()
sum=0   
#Ascii a = 097, A = 065
#Part1
for i in range(0,len(inputlist)):
    val = ord(str(set(inputlist[i][:len(inputlist[i])//2])&set(inputlist[i][len(inputlist[i])//2::]))[2]) #2er Set -> Common Char aus 2 Hälften
    if(val<97):
        sum+= (val-38) #Offset Ascii Großbuchstaben
    else:
        sum+= (val-96) #Offset Ascii Kleinbuchstaben
print(sum)
sum=0
#Part 2
for i in range(0,len(inputlist),3):
    val = ord(str(set(inputlist[i])&set(inputlist[i+1])&set(inputlist[i+2]))[2]) #3er Set -> Common Char aus 3 Zeilen
    if(val<97):
        sum+= (val-38)
    else:
        sum+= (val-96)
        
print(sum)