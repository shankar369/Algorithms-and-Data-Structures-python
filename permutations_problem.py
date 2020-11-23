from itertools import combinations
x = "".join(sorted(list("954311"),reverse=True))

cmbs = sorted([int(''.join(l)) for i in range(len(x)) for l in combinations(x, i+1)],reverse=True) 
print("worst case iterations : ",len(cmbs))
for i in cmbs:
    if(int(i)%3==0):
     print(i)
     break





