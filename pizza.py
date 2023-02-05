import sys,time

lan = input(' Hangi dil "Tur" veya "İng"\n\nWhich language"Tur" or "İng" ')
if lan == "Tur":
 

 a = int(input("Bütcenizi giriniz:"))



 print("                  ********Pizza yemek istermisiniz?********\n")

 tur = int(input('Pizanızı sucuklu istiyorsanız"1"karışık istiyorsanız"2"ve peynirli istiyorsanız"3"tıklayın\n'))
 time.sleep(0.10)

 boyut = input('Hangi boy olsun"S","M","L"\n')
 time.sleep(0.10)

 mazeme = input('Mezemeler çok olsunmu? "evet","hayır"\n')
 time.sleep(0.10)

 içecek = input('içecek olsunmu?"evet","hayır"\n')
 time.sleep(0.10)

 bahsis = input('bahşiş verecekmisiniziz?**hayır** diyorsan entere bas, evet ditorsan kaç tl "1","5","10":\n\n')
 time.sleep(0.10)

 hesap = 0

 if tur == "1":
  hesap =+ 18
 

 elif tur == "2":
  hesap += 22
 
 else:
  hesap += 13
  

 if boyut == "S":
    hesap += 30
     

 elif boyut == "M":
     hesap += 35
     
 else:
     hesap += 45
     

 if boyut == "evet":
   if boyut == "L":
    hesap += 25

    
 if içecek == "evet":
  hesap += 15  

 if bahsis == "1":
    hesap += 1
 elif bahsis == "5":
  hesap += 5
 elif bahsis == "10":
  hesap + 10
 else:
  hesap += 1  

 
 c = a - hesap
 print("Geriye kalan paranız:",c)
 time.sleep(0.10)
   
 dolar = hesap // 18,58
 euro = hesap // 19,25
 dinnar = hesap // 60,52
 azar = hesap // 10,95



 print(f"Hesabınız toplam: {hesap} TL.dir")
 print(f"Hesabınız toplam: {dolar} US Dolları")
 print(f"Hesabınız toplam: {euro} Euro dur")
 print(f"Hesabınız toplam: {dinnar} Kuwaiti Dinar ıdır")
 print(f"Hesabınız toplam: {azar} Azərbaycan manatıdır")






#
#ingilizce 
#kısım
#





elif lan == "İng":
  
  a1 = int(input("Enter your budget:"))



  print("                  ********Would you like to eat pizza?********\n")

  tur1 = int(input('Click "1" if you want your pizza with sausage "2" if you want mixed and "3" if you want cheese\n'))
  time.sleep(0.10)
  boyut1 = input('Which size"S","M","L"\n')
  time.sleep(0.10)

  mazeme1 = input('Is there a lot of appetizers? "Yes" "No"\n')
  time.sleep(0.10)

  içecek1 = input('drink?"yes","no"\n')
  time.sleep(0.10)

  bahsis1 = input('will you tip? If you say **no** press enter, yes ditorsan how much is "1","5","10":\n\n')
  time.sleep(0.10)

  hesap1 = 0

  if tur1 == "1":
   hesap1 =+ 18
 

  elif tur1 == "2":
   hesap1 += 22
 
  else:
   hesap1 += 13
  

  if boyut1 == "S":
    hesap1 += 30
     

  elif boyut1 == "M":
     hesap1 += 35
     
  else:
     hesap1 += 45
     

  if boyut1 == "yes":
   if boyut1 == "L":
     hesap1 += 25

    
  if içecek1 == "yes":
    hesap1 += 15  

  if bahsis1 == "1":
    hesap1 += 1

  elif bahsis1 == "5":
   hesap1 += 5

  elif bahsis1 == "10":
   hesap1 + 10

  else:
   hesap1 += 1  

 
  c1 = a1 - hesap1
  print("Your remaining money:",c1)
  time.sleep(0.10)
   
  dolar1 = hesap1 // 18,58
  euro1 = hesap1 // 19,25
  dinnar1 = hesap1 // 60,52
  azar1 = hesap1 // 10,95



  print(f"Your account total: {hesap1} TL.dir")
  print(f"Your account total: {dolar1} US Dollar")
  print(f"Your account total: {euro1} Euro")
  print(f"Your account total: {dinnar1} Kuwaiti Dinar")
  print(f"Your account total: {azar1} Azərbaycan manatıdır")

