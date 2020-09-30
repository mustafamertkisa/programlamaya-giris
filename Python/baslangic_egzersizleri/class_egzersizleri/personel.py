class ucgen:
    def __init__(self,aci1,aci2,aci3):
        self.aci1=aci1
        self.aci2=aci2
        self.aci3=aci3

    def kontrol(self):
        if self.aci1+self.aci2+self.aci3==180:
            print("Bu bir üçgendir")
        else:
            print("Bu bir üçgen değildir")

a1=int(input("Açı:1"))
a2=int(input("Açı:2"))
a3=int(input("Açı:3"))

deneme=ucgen(a1,a2,a3)

print(deneme.kontrol())
