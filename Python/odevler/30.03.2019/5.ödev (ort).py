import random

a = 0

for i in range(20):
    rastgele = random.randint(1,1000)
    print(rastgele)
    a += rastgele
print("Sayıların ortalaması:",a/20)
    
