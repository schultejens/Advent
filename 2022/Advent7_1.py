from anytree import Node, RenderTree
import time
start_time = time.time()
with open('2022/input7_1.txt') as f:
    inputlist = f.readlines()
    
cursorDepth=0
root = Node("")
t1 = Node('d',parent=root)
for i in range(0,len(inputlist)):
        print(inputlist[i])
   
print(RenderTree(root))
print("-- %s seconds --" % (time.time() - start_time))
#-- 0.00700068473815918 seconds --