import math

a=0

for i in range(500,1001):
    if i % 2 == 0 and i % 4 == 0:
        i=math.sqrt(i)
        print(i)
        
        
