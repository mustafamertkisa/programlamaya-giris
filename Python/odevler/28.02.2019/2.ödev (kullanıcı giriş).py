kayitkullaniciadi = "mertybs"
kayitparola = "12345"

girislimiti = 3

while True:

    kullanici = input("Kullanıcı adınızı giriniz:")
    parola = input("Parolanızı giriniz:")

    if (kullanici != kayitkullaniciadi and parola == kayitparola):
        print("Hatalı kullanıcı adı!")
        girislimiti -= 1
        print("Giriş limiti: ", girislimiti)

    elif (kullanici == kayitkullaniciadi and parola != kayitparola):
        print("Hatalı parola!")
        girislimiti -= 1
        print("Giriş limiti: ", girislimiti)
      
    elif (kullanici != kayitkullaniciadi and parola != kayitparola):
        print("Hatalı kullanıcı adı ve parola!")
        girislimiti -= 1
        print("Giriş limiti: ", girislimiti)

    else:
        print("Sisteme başarıyla giriş yapıldı.")
        break

    if girislimiti == 0:
        print("Giriş limitiniz doldu!")
        break


   

    
        
    
