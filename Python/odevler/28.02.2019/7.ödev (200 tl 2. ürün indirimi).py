birinciürün = int(input("Birinci ürün tutarını giriniz:"))
ikinciürün = int(input("İkinci ürün tutarını giriniz:"))

toplamtutar = (birinciürün + ikinciürün)

if toplamtutar >= 200:
    print("Ödemeniz gereken tutar: {} TL".format(birinciürün + (ikinciürün - (ikinciürün * 25/100))))

else:
    print("Ödemeniz gereken tutar: {} TL".format(toplamtutar))
