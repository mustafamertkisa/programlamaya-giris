bolunen = 0
sayac = 0
for i in range(50,501):
    if i % 3 == 0 and i % 5 == 0:
        sayac +=1
        bolunen = bolunen + i
print("Bölünen sayıların toplamı: {}".format(bolunen))
print("Bölünen sayıların ortalaması: {}".format(bolunen/sayac))
