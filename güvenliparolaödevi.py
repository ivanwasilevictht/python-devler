print(*"GÜVENLİ ŞİFRE PROGRAMI")

print("Bu program kullanıcılara daha güvenli şifreler sunar...")

büyükharfler= "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVWXYZ"
küçükharfler= "abcçdefghgğhıijklmnoöprsştuüvwxyz"
rakamlar="0415862379"
özelkarekterler=".,*-+?/ "


a1= input("Şifrenizde büyük karekter olsun mu? [E/H]")
a2= input("Şifrenizde küçük karekter olsun mu? [E/H]")
a3= input("Şifrenizde rakam olsun mu? [E/H]")
a4= input("Şifrenizde özel karekter olsun mu? [E/H]")

if (a1=="E" and a2=="E" and a3=="E" and a4=="E"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[:3] + küçükharfler[-1] + rakamlar[:3] + özelkarekterler[:4])

elif (a1=="E" and a2=="E" and a3=="E" and a4=="H"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[:2] + küçükharfler[-3] + rakamlar[:5])

elif (a1=="E" and a2=="E" and a3=="H" and a4=="E"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[:3] + küçükharfler[-1] + özelkarekterler[:4])

elif (a1=="E" and a2=="H" and a3=="E" and a4=="E"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[:6] + rakamlar[:2] + özelkarekterler[:-2])

elif (a1=="H" and a2=="E" and a3=="E" and a4=="E"):
    print("Güvenli şifreniz oluşturuldu...")
    print(küçükharfler[-3] + rakamlar[:8] + özelkarekterler[:-4])

elif (a1=="H" and a2=="H" and a3=="E" and a4=="E"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(rakamlar[:5] + özelkarekterler[:4])

elif (a1=="H" and a2=="E" and a3=="H" and a4=="E"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(küçükharfler[:6] + özelkarekterler[:5])

elif (a1=="H" and a2=="E" and a3=="E" and a4=="H"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(küçükharfler[-6] + rakamlar[:5] )

elif (a1=="H" and a2=="H" and a3=="E" and a4=="E"):
    print("Güvenli şifreniz oluşturuldu...")
    print(rakamlar[:6] + özelkarekterler[:3])

elif (a1=="E" and a2=="H" and a3=="H" and a4=="E"):  #(Burası)
    print(*"Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[6:10] + özelkarekterler[:2])

elif (a1=="E" and a2=="H" and a3=="E" and a4=="H"):
    print("Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[4:8] + rakamlar[:5])

elif (a1=="H" and a2=="E" and a3=="H" and a4=="E"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(küçükharfler[-6]+ özelkarekterler[:3])

elif (a1=="E" and a2=="H" and a3=="H" and a4=="E"): #Yukarıda belirtilen koşul ile aynı sonucu verecektir.İndexleri farklı olsa bile
    print(*"Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[:12] + özelkarekterler[:2])

elif (a1=="E" and a2=="E" and a3=="H" and a4=="H"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[:8] + küçükharfler[:6])

#Bundan sonraki oluşturacağımız koşullar daha önceden oluşturuldukları için aynı sonuç verilecektir. 2H 1E kombinasyonu


elif (a1=="H" and a2=="H" and a3=="H" and a4=="E"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(özelkarekterler[:5]) #Genellikle şifrelerde yalnızca özel k. kullanılması yasaktır.

elif (a1=="E" and a2=="H" and a3=="H" and a4=="H"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(büyükharfler[8:16])

elif (a1=="H" and a2=="E" and a3=="H" and a4=="H"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(küçükharfler[11:-6])

elif (a1=="H" and a2=="H" and a3=="E" and a4=="H"):
    print(*"Güvenli şifreniz oluşturuldu...")
    print(rakamlar[:9])

elif (a1=="H" and a2=="H" and a3=="H" and a4=="H"):
    print("Belirtilen kriterlere uygun şifre oluşturulamadı.")

else:
    print("Geçersiz..")
    
    
    
    
    
    
    


    
