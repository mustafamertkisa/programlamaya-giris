import random

a = 0

for i in range(20):
    rastgele = random.randint(0,100)
    print(rastgele)
    if rastgele > a:
        a=rastgele
print("Bu sayıların en büyüğü = {}".format(a))
            
        
        

