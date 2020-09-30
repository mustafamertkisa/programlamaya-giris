print("""
*******************************
Çıkmak için 'ç' tuşuna basınız.
*******************************
""")

while True:

    girilensayi = input("Bir sayı giriniz:")

    if girilensayi == "ç":
        print("Program sonlandırılıyor...")
        break

    girilensayi = int(girilensayi)

    if girilensayi < 0:
        print("{} negatif bir sayıdır.".format(girilensayi))

    elif girilensayi == 0:
        print("{} sayısı sıfırdır.".format(girilensayi))

    else:
        print("{} pozitif bir sayıdır.".format(girilensayi))

    
