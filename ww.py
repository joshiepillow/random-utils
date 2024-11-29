import math
ans = set([])
for i in [32]:
    for j in [16]:
        if(i != j):
            for k in [25]:
                if(i != k and j != k):
                    for r in range(36):
                        if(r != i and r != j and r != k):
                            if int(math.sqrt(i**2 + j**2 + k**2 + r**2)+0.5)**2 == i**2 + j**2 + k**2 + r**2:
                                    x = int(math.sqrt(i**2 + j**2 + k**2 + r**2)+0.5)
                                    ans.add(x)
                                
print(ans)
