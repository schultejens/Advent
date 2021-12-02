with open('2020/input1.1.txt') as f:
    inputlist = f.readlines()
inputlist = list(map(int,(map(lambda s: s.strip(), inputlist))))

for i, number in enumerate(inputlist[:-1]):  
    complementary = 2020 - number
    if complementary in inputlist[i+1:]:  
        print("Solution Found: {} and {}".format(number, complementary))
        break
else: 
    print("No solutions exist")

print(complementary*number)