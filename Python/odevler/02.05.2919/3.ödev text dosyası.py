import random
file=open("ucuncuodev.txt","w")
for i in range(21):
    a = random.randrange(0,1000,3)
    file.write(str(a))
    file.write("\n")
file=open("ucuncuodev.txt","r")
file.close()
        
