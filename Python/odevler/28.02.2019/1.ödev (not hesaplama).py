vize_not = int(input("Vize notunuzu giriniz:"))

final_not = int(input("Final notunuzu giriniz:"))

ortnot =  (vize_not * 40/100) + (final_not * 60/100)

print("Ortalamanız: {}".format(ortnot))

if ortnot < 50:
    print("Malesef dersten kaldınız.")

else:
    print("Tebrikler dersten geçtiniz.")
            
