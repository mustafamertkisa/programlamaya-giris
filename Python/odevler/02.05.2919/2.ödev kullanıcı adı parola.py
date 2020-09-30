print("""
***Kullanıcı adı en az 5 en fazla 8 karakter olmalı***
***Şifre ise en az 7 en fazla 10 karakter olmalıdır***
""")
while True:
    kadi = input("Bir kullanıcı adı giriniz:")
    par = input("Bir parola giriniz:")
    adsay = (len(kadi))
    parsay = (len(par))
    if adsay <= 4 or adsay >= 7 or parsay <= 6 or parsay >= 9:
        print("Sisteme kayıt olamazsınız! Lütfen tekrar deneyin.")
        continue
    else:
        print("Başarıyla kaydınız oluşturuldu.")
        break
