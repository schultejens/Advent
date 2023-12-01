import datetime
import re

start_time = datetime.datetime.now()
#returns (index, value) of first word found
def getNumberStart(s, forward):
    found = []
    number_words = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number_words_rev = ["orez","eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]

    if(forward):
        found = re.findall(str("|".join(number_words)), str(s))
        if(found):
            return ((s.index(found[0]), number_words.index(found[0])))
        #print("found1",number_words.index(found))

    else:
        found = re.findall(str("|".join(number_words_rev)), str(s))
        #print("found2",number_words_rev.index(found))
        if(found):
            return ((s.index(found[0]), number_words_rev.index(found[0])))



file1 = open('input', 'r')
Lines = file1.readlines()

buffer = 0
finalsum = 0
charNum = ""
for line in Lines:
    line = line.strip()
    print(line)
    if (not any(char.isdigit() for char in line)):
        buffer += int(getNumberStart(line, True)[1])*10 + int(getNumberStart(line[::-1],False)[1])
        continue

    for i,c in enumerate(line):
        if c.isdigit():

            charNum = getNumberStart(line,True)
            #print("charnum1: ", charNum)
            if(charNum is not None and charNum[0]< i):
                buffer += int(charNum[1]) * 10
                print("buffer1: ", buffer)
                break
            else:
                buffer += int(c) * 10
                print("buffer1: ",buffer)
                break

    for i,c in enumerate(line[::-1]):
        if c.isdigit():
            charNum = getNumberStart(line[::-1], False)
            #print("charnum2: ",charNum)
            if ( charNum is not None and charNum[0] < i):
                buffer += int(charNum[1])
                print("buffer2: ", buffer)
                break
            else:
                buffer += int(c)
                print("buffer2: ", buffer)
                break
            break
    finalsum+= buffer
    buffer = 0


print(finalsum)
print("-- %s ms --" % ((datetime.datetime.now()-start_time).total_seconds()*1000))

