print(*"AKILLI HESAP MAKİNESİ")
print(*"*********************")

 
print("Bu program sayesinde matematiksel işlemlerinizi kolayca yapabilirsiniz.Ama öncelikle işlem yapılacak sayıları giriniz..")

_a1=int(input("İşem yapılacak birinci sayıyı giriniz:"))
_a2=int(input("İşlem yapılacak ikinci sayıyı giriniz: "))

print("\n1.Toplama(+)\n2.Çıkarma(-)\n3.Çarpma(*)\n4.Bölme(/)")#Topma işleminin önüne konulan \n daha düzgün bir görüntü içindir.

operator=int(input("Lütfen bir operatör belirleyin:"))
 

if (operator==1) :
    print("{} ve {} toplamı {} sonucunu veriyor".format(_a1,_a2,_a1+_a2)) #if ile koşul belirttik eğer 1 numaralı operator seçilirse seçilen sayıların toplanmasını istedik

elif (operator==2) :
    print("{} ve {} çıkarımı {} sonucunu veriyor".format(_a1,_a2,_a1-_a2)) #elif ile diğer koşulları belirrtik 2,3,4 numaralı operatorler seçilirse belirtilen işlemlerin yapılmasını istedik

elif (operator==3) :
    print("{} ve {} çarpımı {} sonucunu veriyor".format(_a1,_a2,_a1*_a2))

elif (operator==4) :
    print("{} ve {} bölümü {} sonucunu veriyor".format(_a1,_a2,_a1/_a2))

else :
    print("Böyle bir prosedür yoktur....") #else ile olur da kullanıcı prosedür dışı bir şey seçmek isterse uyarı vermesini istedik..

    




