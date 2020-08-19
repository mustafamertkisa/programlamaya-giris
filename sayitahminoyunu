print("""
******************************************
1 ile 20 arasında bir sayıyı tahmin ediniz
******************************************
""")

import random
import time

rastgele_sayı = random.randint(1,20)
tahmin_limiti = 5

while True:

    tahmin = int(input("Tahmininiz:"))

    if tahmin == rastgele_sayı:
        print("Yanıtınız kontrol ediliyor...")
        time.sleep(1)
        print("Tebrikler bildiniz {}".format(tahmin))
        tahmin_limiti -= 1
        break

    elif tahmin < rastgele_sayı:
        print("Yanıtınız kontrol ediliyor...")
        time.sleep(1)
        print("Daha büyük bir sayı söylemelisiniz :)")
        tahmin_limiti -= 1
        
    else:
        print("Yanıtınız kontrol ediliyor...")
        time.sleep(1)
        print("Daha küçük bir sayı söylemelisiniz :)")
        tahmin_limiti -= 1

    if tahmin_limiti ==0:
        print("Malesef tahmin hakkınız doldu!")
        break
