print("""
*******************************
Çıkmak için 'ç' tuşuna basınız.
*******************************
""")
while True:

    girilensayi = (input("Bir sayı giriniz:"))

    if girilensayi == "ç":
        print("Program sonlandırılıyor...")
        break

    girilensayi = int(girilensayi)

    if (girilensayi % 2) == 0:
        print("{} sayısı çift bir sayıdır.".format(girilensayi))

    elif girilensayi == 0:
        print("0 sayısı çift bir sayıdır.")

    else:
        print("{} sayısı tek bir sayıdır.".format(girilensayi))
    
