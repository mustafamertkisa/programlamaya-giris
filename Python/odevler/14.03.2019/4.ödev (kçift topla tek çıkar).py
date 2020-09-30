toplam = 0
while True:        
    girdi=int(input("Sayıyı Girin:"))           
    if(girdi==0):
        break  
    if(girdi%2==0):   
        toplam += girdi         
    else:   
        toplam -= girdi             
print("Sonuç : {}".format(toplam))
    
