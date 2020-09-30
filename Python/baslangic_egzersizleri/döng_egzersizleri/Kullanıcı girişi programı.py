
print("""
*************************
Kullanıcı Girişi Programı
*************************
""")

sys_kullanıcı_adı = "mstfmrt"
sys_parola = "12345"


while True:
    kullanıcı_adı = input("Kullanıcı adınızı giriniz:")
    parola = input("Parolanızı giriniz:")
    giriş_limiti = 3

    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Hatalı kullanıcı adı!")
        giriş_limiti -=1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Hatalı parola!")
        giriş_limiti -=1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Hatalı kullanıcı adı ve parola!")
        giriş_limiti -=1
    else:
        print("Sisteme giriş yapıldı...")
        break
    if (giriş_limiti == 0):
        print("Giriş limiti doldu!")
        break
        
