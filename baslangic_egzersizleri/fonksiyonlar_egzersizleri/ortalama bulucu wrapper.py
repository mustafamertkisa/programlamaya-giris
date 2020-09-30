def ekstra(fonk):
    
    def wrapper(sayılar):
        çiftler=0
        tekler=0
        çifttop=0
        tektop=0
        for i in sayılar:
            if i % 2 == 0:
                çiftler += i
                çifttop += 1
            else:
                tekler += i
                tektop +=1
        print("Çift sayıların ortalaması: {}".format(çiftler/çifttop))
        print("Tek sayıların ortalaması: {}".format(tekler/tektop))
        
        fonk(sayılar)

    return wrapper

@ekstra
def ortalamabul(sayılar):
    toplam = 0
    for i in sayılar:
        toplam += i
    print("Genel ortalama: {}".format(toplam/len(sayılar)))
ortalamabul([1,60,40,30,5,7,8,9,36])