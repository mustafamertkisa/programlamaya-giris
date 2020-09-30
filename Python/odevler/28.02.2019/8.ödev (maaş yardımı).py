maasbilgi = int(input("Maaş miktarınızı giriniz:"))
cocuksayi = int(input("Çocuk sayınızı giriniz:"))

if cocuksayi == 1:
    print("Güncel maaşınız: {} Türk Lirasıdır.".format(maasbilgi + (maasbilgi * 5/100)))

elif cocuksayi == 2:
    print("Güncel maaşınız: {} Türk Lirasıdır.".format(maasbilgi + (maasbilgi * 10/100)))

elif cocuksayi == 0:
    print("Güncel maaşınız: {} Türk Lirasıdır.".format(maasbilgi))

else:
    print("Güncel maaşınız: {} Türk Lirasıdır.".format(maasbilgi + (maasbilgi * 15/100)))
    
