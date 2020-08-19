print("""
*******************************
Faktöriyel Bulma Programı

Çıkmak için 'ç' tuşuna basınız.
*******************************
""")

while True:
    sayı = input("Sayı:")

    if sayı == "ç":
        print("Program sonlandırılıyor...")
        break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):
            faktoriyel *= i
        print("Faktöriyel",faktoriyel)
      
