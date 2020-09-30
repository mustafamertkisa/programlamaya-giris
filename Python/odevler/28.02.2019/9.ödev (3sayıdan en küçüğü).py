aaa = int(input("Birinci sayıyı giriniz:"))
bbb = int(input("İkinci sayıyı giriniz:"))
ccc = int(input("Üçüncü sayıyı giriniz:"))

if aaa < bbb and aaa < ccc:
    print("Sayılarınızdan en küçüğü {} sayısıdır.".format(aaa))

elif bbb < aaa and bbb < ccc:
    print("Sayılarınızdan en küçüğü {} sayısıdır.".format(bbb))

else:
    print("Sayılarınızdan en küçüğü {} sayısıdır.".format(ccc))
    
    
