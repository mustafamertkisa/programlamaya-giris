gdolar = float(input("Güncel dolar fiyatını giriniz:"))
geuro = float(input("Güncel euro fiyatını giriniz:"))
galtın = float(input("Güncel altın (gram) fiyatını giriniz:"))
gtl = float(input("Türk lirası miktarını giriniz:"))

def program(gdolar,geuro,galtın,gtl):
    print("{} TL = {} Dolar".format(gtl,gtl/gdolar))
    print("{} TL = {} Euro".format(gtl,gtl/geuro))
    print("{} TL = {} Altın (gram)".format(gtl,gtl/galtın))

program(gdolar,geuro,galtın,gtl)

    
