print("""
*************************************
Hesap Makinesi Programına Hoşgeldiniz

İşlem Numaraları;

1. Toplama işlemi

2. Çıkarma işlemi

3. Çarpma işlemi

4. Bölme işlemi

5. Programdan çıkış
*************************************
""")

while True:
    a = int(input("Birinci sayıyı giriniz:"))
    b = int(input("İkinci sayıyı giriniz:"))

    islem = input("İşlem numarasını giriniz:")

    if islem == "1":
        print("{} + {} = {}".format(a,b,a+b))

    elif islem == "2":
        print("{} - {} = {}".format(a,b,a-b))

    elif islem == "3":
        print("{} x {} = {}".format(a,b,a*b))

    elif islem == "4":
        print("{} / {} = {}".format(a,b,a/b))

    elif islem == "5":
        print("Program sonlandırılıyor...")
        break

    else:
        print("Lütfen geçerli bir işlem giriniz!")
        continue
    
