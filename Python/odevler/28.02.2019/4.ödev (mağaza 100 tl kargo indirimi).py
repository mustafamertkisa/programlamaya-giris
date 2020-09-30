aaa= int(input("Ürün tutarını giriniz:"))

if aaa > 100:
    print("Ödemeniz gereken tutar: {} TL".format(aaa))
else:
    print("Ödemeniz gereken tutar: {} TL".format(aaa+5))
