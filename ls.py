import os
ls =  os.listdir('.')
gap = 0
for i in ls:
    length = len(i)
    if length > gap:
        gap = length
if gap > 64 : 
    gap =32
gap += 4
for i, item in enumerate (ls):
    if i % 4 == 0 : 
        print('')
    x = ' '* (gap - len(item[0:32]))
    print(item[0:32], end=x)