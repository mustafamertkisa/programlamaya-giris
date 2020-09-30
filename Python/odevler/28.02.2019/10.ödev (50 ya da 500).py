kisiyas = int(input("Yaşınızı giriniz:"))
kisitutar = int(input("Alışveriş tutarınızı giriniz:"))

if kisiyas >= 50 or kisitutar >= 500:
    print("Ödemeniz gereken tutar: {} Türk Lirasıdır.".format(kisitutar - kisitutar * 20/100))

else:
    print("Ödemeniz gereken tutar: {} Türk Lirasıdır.".format(kisitutar))
    
