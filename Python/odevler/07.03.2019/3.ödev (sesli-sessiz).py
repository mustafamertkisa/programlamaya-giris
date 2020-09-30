sesliharf = {"a","e","ı","i","o","ö","u","ü","A","E","I","İ","O","Ö","U","Ü"} 

sesli_harfler =""
seslisayi = 0
sessiz_harfler = ""
sessizsayi = 0

kelime = input("Cümlenizi giriniz:") 

for i in kelime: 
    if i in sesliharf: 
        sesli_harfler += i
        seslisayi += 1
    else: 
        sessiz_harfler += i
        sessizsayi += 1
print("-----------------------------")
print("Sesli harfler:", sesli_harfler)
print("Sesli harf sayısı:", seslisayi)
print("-----------------------------")
print("Sessiz harfler:", sessiz_harfler)
print("Sessiz harf sayısı:", sessizsayi)
print("-----------------------------")

if seslisayi > sessizsayi:
    print("Cümlenizde sesli harf daha fazladır.")

elif sessizsayi > seslisayi:
    print("Cümlenizde sessiz harf daha fazladır.")

elif sessizsayi == seslisayi:
    print("Cümlenizde sesli ve sessiz harf sayısı eşittir.")
    
