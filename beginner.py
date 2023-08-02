
# ---------------------------------------------------------------------------- #
#                              Python Öğreniyorum                              #
# ---------------------------------------------------------------------------- #

#ornek 1 - degiskenler
"""
sayi1=32
print('degiskenin icinde ki sayi:',sayi1)
sayi1=33
print('degiskenin icinde ki sayi:',sayi1, "oldu")
"""

#ornek 2 - Değişkenler aralarına virgül eklenerek yan yana yazılır. Değerleri de aynı sıralama ile karşılarına yazılır

''''
adi,soyadi,yasi='ahmet','tayfur',22
print('adi=',adi)
print('soyadi=',soyadi)
print('yasi=',yasi)
'''

#ornek 3 - * operatorunun karakter iceren degiskende kullanimi
'''
sayi1=4
sayi2='31'
print(sayi1*sayi2)
#cevap 31313131
'''

#ornek 4 veri tipleri
'''
piSayisi=3.14
 #float tipinde bir veri
print ('pi sayısı=', piSayisi)
rCm=2
 #integer tipinde veri
alan=3.14*2**2
print ('Alan=', alan)
 #sonuç float tipinde
print('Yarıçapı 2 olan dairenin alanı ', alan, ' cm 2 dir' )
karmasikSayi=4+5j
print('Bir karmaşık sayı=', karmasikSayi+3j)
'''

#ornek 5 - len() kullanimi
'''
metin1='ahmet'
metin2='merhaba'
print(metin1)               #karakter dizisinin tamamini yazar
print (metin1*2)            #karakter dizisini 2 defa yazar
print(metin1+' '+metin2)        #iki karakter dizisini birlestirir
print('metin1 adli degiskenin uzunlugu: ',len(metin1))
'''

#ornek 6 - Karakter Dizilerinde (string) Dilimleme İşlemleri
'''
metin='merhaba ahmet bey'
print (metin[0])            # ifadenin ilk karakterini yazar.
print(metin[4:7])           # ifadenin 5, 6 ve 7. karakterlerini yazar.
print(metin[8::])           # 9. karakterden sonuncu karaktere kadar yazar.
print(metin[-2])            # karakter dizisinin en sondan ikinci karakterini yazar.
print(metin[:7])            # indisi 0' dan 7'ye kadar olan (7 dahil değil) karakterleri yazar.
print(metin[8:])            # başlangıç indisinden sonra tüm karakterleri yazar.
print(metin[0:8:2])         # 0, 2, 4 ve 6 indis numaralı karakterleri dilimler.
'''

#ornek 7- bir degiskenin veri tipi type(degiskeninAdi) ile kontrol edilir
'''
sayi1=7
sayi2=10.23
metin1="1"
sayi3=4+8j
askerlikYaptiMi=True
listem=['Çınar', 24, 'Mühendis', True]
demet1=('Çınar', 24, 'Mühendis', True)
sozluk={'adi': 'Çınar','yasi': 24, 'meslekUnvani':'Mühendis', 'askerlikDurumu': True}


print('1. degiskenin veri tipi:',type(sayi1))
print ("2. değişkenin veri tipi: ", type(sayi2))
print ("3. değişkenin veri tipi: ", type(metin1))
print ("4. değişkenin veri tipi: ", type(sayi3))
print ("5. değişkenin veri tipi: ", type(askerlikYaptiMi))
print ("6. değişkenin veri tipi: ", type(listem))
print ("7. değişkenin veri tipi: ", type(demet1))
print ("8. değişkenin veri tipi: ", type(sozluk))
'''

#ornek 8- veri tiplerini donusturmek
'''
metin1='4'
metin2='5'
print(metin1+metin2)
print(int(metin1)+int(metin2))
'''

#ornek 9- boolean veri tipinin donusumu
'''
askerlikYaptiMi=True
print('Askerlik yaptı mı?', askerlikYaptiMi)

askerlikYaptiMiInt=int(askerlikYaptiMi)     #integer tipine dönüştürüldü.
print('Askerlik yaptı mı?', askerlikYaptiMiInt)

askerlikYaptiMiStr=str(askerlikYaptiMi)     #string tipine dönüştürüldü.
print('Askerlik yaptı mı?', askerlikYaptiMiStr)
#Çıktı olarak True verir ancak bu boolean tipinde değildir.
'''

#ornek 10- mantiksal operatorler 'or','and','not'
'''
 #or operatoru kullanimi
sayi1=6
print(sayi1<7 or sayi1>10)

#adi elif veya emre ise true dondurur
adi='elif'
print(adi=='elif' or adi=='emre')

 #and oparetoru kullanimi (tek yanlis tum dogruyu goturur .d)
ogrenciderspuani=56
print(ogrenciderspuani>50 and ogrenciderspuani<60)

adi='ahmet'
yasi=22
print(adi=='ahmet' and yasi>=20)

 #not operatoru (tersi)
ogrencidersPuani=65
print(not(ogrencidersPuani<45))
print(ogrencidersPuani>45) #yukarida ki satirla ayni sonucu verecektir
'''

# --------------------------- BOLUM SONU ORNEKLERI --------------------------- #
'''
sayi1=8*5/2
print(sayi1>20)
#false

vizePuani=80
finalPuani=70
sonuc=(0.4*vizePuani)+(0.6*finalPuani)
print(sonuc>60)
#true

plaka='06'
print(type(plaka))
#class str
'''

# ---------------------------------------------------------------------------- #
#                     BOLUM 2 fonksiyonlarda bazi kurallar                     #
# ---------------------------------------------------------------------------- #
'''
# ters taksim (\) kullanimi
print('ahmet\'in yasi 22') #print() icinde tirnak karmasasini yok etti

#alt satir basi (\n)
print("1.satir\n2.satir\n3.satir")

#tab tusu kadar bosluk birakarak cikti alma (\t)
print("pazartesi\tsali\tcarsamba")

#end() parametresi (satirlari birlestiriyor)
print("Merhaba!",end=" ")
print("Python")

#sep() parametresi (degerlerin arasina sep ile belirtilen ifade ekleniyor)
print("pazartesi","salı","çarşamba","perşembe","cuma",sep="-")

#format metodu
print("çıktı işlemi {} {} {}".format(1,2,3))
#Burada print() fonksiyonunda kullanılan her bir {} ifadesine karşılık olarak format(  ) metoduna bir adet argüman verilmelidir.
print("{1} {0} {2}".format(10,"Python",20))
'''

#INPUT KOMUTU
#ornek
'''
isim=input("isminizi giriniz:" )
print("merhaba ", isim)
'''

#ornek inputun icindeki degeri integera cevirme
'''
a=int(input('bir sayi giriniz: '))
'''
#ornek input icindeki degerleri toplamak
'''
a=int(input('bir sayi girniz: '))
b=int(input('ikinci sayiyi girniz:' ))
print('girdiginiz sayilarin toplami: ',a+b)
'''

# --------------------------- BOLUM SONU ORNEKLERI --------------------------- #

#a=input('isminizi girin ')
#print('merhaba',a)

#iki sayinin ortalamasi
#a=int(input('birinci sayi ?'))
#b=int(input('ikinci sayi ?'))
#print ('sayilarin ortalamasi',(a+b)/2)

#ornek yas degeri 18 veya daha buyukse ona bir mesaj verir
'''
yasi=int(input('lutfen yasinizi giriniz.'))
if yasi>=18:
    print("yasiniz resittir.")
else:
    print('yasiniz resit degildir.')
'''

#ornek kullanicinin girdigi degerleri kontrol eden program
'''
kullaniciAdi=input('adinizi giriniz: ')
dogumTarihi=input('dogum yiliniz nedir ?')
if (kullaniciAdi=='ahmet'and dogumTarihi=='2001'):
    print('giris basarili hosgeldiniz')
else:
    print('kayit bulunamadi.')
'''

#ornek icice kosullar ilk kosul saglanirsa ikinci kosula gecilebilme
'''
kullaniciAdi=input('Kullanıcı Adı:')
kullaniciParola=input('Parola:')
if (kullaniciAdi=='Admin'):
 print('Kullanıcı adı doğru')
if (kullaniciParola=='123456'):
        print('Giriş başarılı.')
        print ('Menülere erişebilirsiniz.')
'''

#ornek if elif else yapisi
'''
sinavPuani=int(input('puaninizi giriniz. '))
if sinavPuani>=85:
    print('pek iyi')
elif sinavPuani>=70:
    print('iyi')
elif sinavPuani>=55:
    print('orta')
elif sinavPuani>=45:
    print('gecer')
else: print('kaldi')
'''

# --------------------------- BOLUM SONU ORNEKLERI --------------------------- #
#1
'''
sayi1=int(input('bir tam sayi giriniz. '))
if sayi1>0:
    print('sayiniz pozitftir.')
elif sayi1<0:
    print('sayiniz negatiftir. ')
else: 
    print('sayiniz sifirdir.')
'''
#2
'''
sinavNot=int(input('sinav not ortalamaniz kac? '))
if sinavNot>=50:
    print('tebrikler dersi gectiniz. ')
else:
    print('kaldiniz. ')
    '''
#3
'''
sayi1=int(input('birinci sayiyi giriniz: '))
sayi2=int(input('ikinci sayiyi giriniz: '))
if sayi1>sayi2:
    print(sayi1, 'daha buyuktur.')
if sayi2>sayi1:
    print(sayi2, 'daha buyuktur.')
if sayi1==sayi2:
    print('sayilar esittir.')
'''
#4
'''
boy=float(input('boyunuzu girin. '))
kilo=float(input('kilonuzu girin. '))
endeks=(kilo/(boy**2))
if endeks<18.5:
    print(endeks,' zayifsiniz.')
elif endeks<=25 and endeks>18.5:
    print(endeks, 'normal')
elif endeks<=30 and endeks>25:
    print(endeks, "obezsiniz.")
else: print("parametre disina ciktiniz.")
'''

# --------------------------------- LISTELER --------------------------------- #

#ornek her veri tipini icerisinde barindiran liste
'''
liste=[1,2,'ali',0.25]
print(liste)
'''

#ornek
'''
meyve="erik"
meyve="ayva-"+meyve[0:]
print(meyve)

liste=['a','b']
liste[1]=2
print(liste)
'''

#ornek 
'''
esya=["ayna",'televizyon','perde']
if("perde" in esya):
    print("bu deger listede var.")
else:
    print("bu deger listede yok.")
'''

#ornek
'''
liste=[1,2,3,4,5,6,7]
oge=liste[1:3]          #1. indisten 3. indise kadar icerir
print(oge)              #cevap=[2,3]
'''

#ornek
'''
liste = [1,2,3,4,5,6,7,8,9,10]
print(liste)
# 1. eleman
print(liste[0])
# 6. eleman
print(liste[5])
# Baştan 5. indekse kadar (dahil değil)
print(liste[:5])
# 1.indisten 5.indise kadar
print(liste[1:7])
print(liste[5:])
print(liste[::2])
'''

#ornek
'''
liste = [ "merhaba", "dünya", "merhaba", "güle güle" ]
print (liste [- 1 ])    #son ögeyi listeler
print( liste [- 3 ])    #sondan üçüncü ögeyi listeler
print(liste [- 4 ])     #sondan dördüncü ögeyi listeler
print(liste[::-1])       #sondan başa doğru listeleme yapmak için kullanılır
'''
# ------------------------------ LISTE METOTLARI ----------------------------- #

#ORNEK - " append " kullanimi
"""
takimlar=['gs','fb','bjk']
takimlar.append("ts")
print(takimlar)
"""
#ORNEK- "insert" kullanimi - 2. indise oge eklenmesi
"""
sebzeler=['lahana','kivircik','pirasa','ispanak','fasulye']
sebzeler.insert(2,'patlican')
print(sebzeler)
"""

#ORNEK - "copy" kullanimi
"""
iller1=['konya','istanbul','izmir','bursa','balikesir']
iller2=[]
iller2=iller1.copy()
print(iller2)
"""
#ORNEK - 'count' kullanimi. Listedeki ogenin kac kere oldugunu soyler
"""
takimlar = ['GS','FB','BJK','TS']
print(takimlar.count('FB'))
"""
#ORNEK - 'extend' kullanimi. Listeleri birlestirerek genisletme
"""
garaj1=['bmw','audi','mercedes','porsche']
garaj2=['ferrari','skoda','tofas']
garaj1.extend(garaj2)
print(garaj1)
"""
#ORNEK= "indis" kullanimi. Listedeki ogenin indis numarasini ogrenme
"""
sebzeler1=['lahana','kivircik','pirasa','ispanak','fasulye']
#print(sebzeler1.indis("ispanak")) #calismiyor kontrol et indis komutunu
"""
#ORNEK- "clear" komutu listedeki tum ogeleri silme komutu
"""
sebzeler2=['lahana','kivircik','pirasa','ispanak','fasulye']
sebzeler2.clear()
print(sebzeler2)
"""
#ORNEK- 'pop' komutu. Listedeki indis numarasi verilen ogeyi silme komutu
"""
sebzeler3=['lahana','kivircik','pirasa','ispanak','fasulye']  
sebzeler3.pop(3)        #3. indisi silme emri verdim. ispanak silindi
print(sebzeler3)
"""

#ORNEK-  "remove" komutu. Listede ki ogenin ismini vererk silme
"""
sebzeler4=['lahana','kivircik','pirasa','ispanak','fasulye']
sebzeler4.remove('lahana')
print(sebzeler4)
"""

#ORNEK-  'reverse' kullanimi. Listeyi tersten siralama komutu.
"""
sayilar=[10,20,30,40,50,60,70]
sayilar.reverse()
print(sayilar)
"""
#ORNEK- 'sort' kullanimi. Listede ki ogeleri alfabetik siralama
"""
isimler=["elif","ayşe","kemal","kaan","hafsa"]
isimler.sort()
print(isimler)
"""
#ORNEK- 'del' kullanimi. Listede ki indis numarasina gore ogeyi silme komutu
"""
isimler1=["elif","ayşe","kemal","kaan","hafsa"]
del isimler1[3]
print(isimler1)
"""
# len() fonksiyonun ozellikleri
"""
##string degiskenin icindeki metnin harf sayisini olcmesi
a="dumtakadumbunubirdahaduy"
print(len(a))

##listed ki oge sayisini olcmesi
b=['bmw','audi','ferrari']
print(len(b))
"""

# --------------------------- Icice giren listeler --------------------------- #
#ORNEK- Listeleri birlestirerek buyuk liste olusturmak
"""
liste1=[1,2,3]
liste2=[4,5,6]
liste3=[7,8,9]
yeniliste=[liste1,liste2,liste3]
print(yeniliste)
"""
#ORNEK-  bos liste olusturup icine listeler eklenmesi
"""
meyveler=[]
meyveler.append(['elma'])
meyveler.append(['armut'])
meyveler.append(['muz','kiraz'])
meyveler.append(['portakal','ananas','kivi'])
print(meyveler)
"""
#ORNEK
"""
cumle="23 nisan herkese mutlu olsun"
kelimeler=cumle.split(" ")
print("cümlenizde ",len(kelimeler),"adet kelime vardır")
"""

# --------------------------- BOLUM SONU ORNEKLERI --------------------------- #
#sayfa 120
# ---------------------------------------------------------------------------- #
#1 Harfler adıyla bir liste oluşturup içine ‘a’, ‘e’, ‘i’, ‘o’, ‘i’, ‘u’ elemanları kaydediniz. Bu listede i ve p
'''
harflerinin sayısını ekrana yazdırınız.
harfler=[]
harfler.append(['a'])
harfler.append(['w','a'])
harfler.append(['s'])
harfler.append(['d'])
harfler.append(['f'])
print(harfler)
print(harfler.count('a'))
print(harfler.count('w'))
'''
#2 Liste1, liste2, liste3 ve liste4 adında dört adet liste oluşturup aynı satırda olacak şekilde tanımlayıp,her bir listeye birer adet eleman girip listeleyiniz
'''
liste1,liste2,liste3,liste4=['a','araba',22,0.34]
print(liste1)
print(liste2)
print(liste3)
print(liste4)
'''
#3
'''
listem1,listem2=['hizli araba ','severim']
listem3=listem1+listem2
print(listem3)
'''
#4 listeyi buyukten kucuge ve kucukten buyuge siralamak
'''
liste = [34,1,56,334,23,2,3,19]
liste.sort()
print('kucukten buyuge dogru ',liste)
liste.reverse()
print('buyukten kucuge dogru ',liste)
'''
#5
'''
liste = [1, 2, 3, 4, 5, 6, 7]
print(liste[1:3])
print(liste[:3])
print(liste[3:])
print(liste[:])
'''
#6
'''
isimler=['ali','veli','ayse',]
soyisimler=['turk','izci','erel']
ad_soy1=isimler[0]+' '+soyisimler[0]
ad_soy2=isimler[1]+' '+soyisimler[1]
ad_soy3=isimler[2]+' '+soyisimler[2]
print(ad_soy1)
print(ad_soy2)
print(ad_soy3)
'''
#7
'''
liste = ['bir','iki','dört']
liste[2]='üç'
liste.insert(3,'dört')
liste.insert(4,'beş')
print(liste)
'''
#8
'''
liste=["birinci veri", "ikinci veri", "üçüncü veri ", "dördüncü veri",
"beşinci veri"]
print(liste[0])
print(liste[4])
'''

# ------------------------------ DONGU YAPILARI ------------------------------ #
#  WHILE DONGUSU
'''
#ORNEK
sayac=1
while sayac<6:
    print('merhaba ahmet')
    sayac=sayac+1
    
#ORNEK
sayac1=1
while sayac1<6:
    print(sayac1)
    sayac1=sayac1+1
'''

#ORNEK
'''
sayac1=1
while sayac1<6:
    print(sayac1)
    sayac1=sayac1+1
print("dongu sonlandi")
'''

#ORNEK 1-100 arasinda ki cift sayilari bulan kod
'''
a=1
while a<=100:
    if a%2==0:
        print(a,end=",")
    a=a+1
'''
#ORNEK 1-100 arasinda ki sayilarin toplamini bulan kod
'''
toplam=0
i=1
while i<=100:
    toplam=toplam+i
    i=i+1
print("sayilarin toplami ",toplam)
'''
#ORNEK WHILE TRUE-BREAK IFADELERI
'''
i=1
while True:
    print(i)
    i+=1
    if i==6:
        break
print("dongu sonlandi")
'''
#ORNEK 
'''
liste=[]
while 1:
    urun=input("urun adini giriniz.")
    if urun=='q':
        break
    liste.append(urun)
print("girdiginiz meyveler:",liste)
'''
#ORNEK
'''
sayi=45
sayac=0
print("1-100 arasinda bir sayi tuttum tahmin et")
while 1==1:
    sayac+=1
    cevap=int(input('1-100 arasi bir sayi girin:'))
    if cevap>sayi:
        print("daha kucuk bir sayi girmelisin")
    elif cevap<sayi:
        print("daha buyuk bir sayi girmelisin.")
    else:
        print("tebrikler tuttugum sayiyi bildin")
        break
print("tebrikler {} seferde sayiyi bulabildin.".format(sayac))
'''
#ORNEK
'''
i=1
f=int(input("faktoriyeli alinacak sayiyi giriniz: "))
sonuc=1
while i<=f:
    sonuc=sonuc*i
    i+=1
print(sonuc)
'''
#ORNEK
'''
yazi="Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği desktekeyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."
harf="a"
sayac=0
for i in yazi:
 if i=="a":
    sayac=sayac+1
print("cümle içerisinde geçen a harfi sayısı: ",sayac)
'''
#ORNEK sesli ve sessiz harfleri ayiran kod
'''
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler=""
sessizler=""
a=input("bir metin giriniz...")
for i in a:
    if i in sesli_harfler:
        sesliler=sesliler+i
    if i in sessiz_harfler:
        sessizler=sessizler+i
print("sesli harfler",sesliler)
print("sessiz harfler",sessizler)
'''

#ORNEK listeler uzerine iterasyon islemi
'''
sayilar=[1,2,3,4,5]
kareler=[]
for i in sayilar:
    kareler.append(i*i)
print (kareler)
'''

#ORNEK sayilarin ortalamasini bulan kod
'''
sayilar=[1,2,3,4,5,6,7,8,9]
toplam=0
for i in sayilar:
    toplam=toplam+i
    print("sayilarin ortalamasi: ",toplam/len(sayilar))
'''

#ORNEK listedeki degerlerden 3 un katlari olanlari bulan kod
'''
sayilar1=[5,23,12,43,51,60,72,36]
for i in sayilar1:
    if i%3==0:
        print(i,end=",")
'''

#ORNEK range komutu kullanimi
'''
print(*range(10))       #baslangic degeri girilmedigi icin 0 dan 10 a kadar sayr
print(*range(5,20))     #baslangic 5 girildigi icin 5 den 20 ye kadar sayar
print(*range(1,20,2))   #baslangic 1 den 20 ye kadar 2 ser artarak sayar
'''

#########ORNEK hatali calismiyor kontrol et
'''
toplam=0
for i in range(20):
    toplam+toplam+i
print("girdiginiz sayilarin toplami: ",toplam)
'''
#ORNEK 20 den 0 a geriye sayilari yazdiran kod
'''
for i in range(20,0,-1):
    print(i,end=",")
'''

#ORNEK 100e kadar 5 in katlari olan sayilari bulan kod
'''
for i in range(0,100,5):
    print(i,end=",")
'''

#ORNEK kullanicidan satir ve sutun degerleri alarak tablo seklinde yazan program
'''
a=int(input("tablonun satir sayisini giriniz. "))
b=int(input("tablonun sutun sayisini giriniz. "))

for i in range(1,a+1):
    for j in range(1,b+1):
        print(j,end=" ")
    print()
'''

#ORNEK continue ifadesi
'''
for i in range(1,6):
    if i==2 or i==4:
        continue
    print(i)
    #while dongusu ile yapilmak istenirse
i=0
while i<5:
    i=i+1
    if i==2 or i==4:
        continue
    print(i)
'''
    
# icice donguler [nested loop]

'''
#ORNEK

dersler=['ders1','ders2','ders3']
konular=['konu1','konu2','konu3']
for x in dersler:
    for y in konular:
        print(x,y)
        
#ORNEK iç içe while döngüsü kullanarak, i ve j olarak tanımlanan iki değişkenin değerlerini ekrana yazdırınız

i=1
while i<4:
    j=1
    while j<4:
        print('i nin degeri: {} j nin degeri: {}'.format(i,j))
        j=j+1
    i=i+1
'''

# --------------------------- BOLUM SONU ORNEKLERI --------------------------- #
'''
#1 girilen sayinin asal olup olmadigini bulan programi yazin

a=int(input('bir sayi giriniz: '))
asal=0
for i in range(2,a):
    if a%i==0:
        asal+=1
if asal==0:
    print('girdiginiz sayi asal.')
else:
    print('girdiginiz sayi asal degildir.')
    
#2 kullanicidan deger alarak agac sekli cizen program

a=int(input('agacin yuksekligi'))
b=a
for i in range(1,a+1):
    print (b * " " , (2*i-1) * "*")
    b-=1

#3 bir listede bulunan sayilarin en buyugunu ve en kucugunun bulan program

liste=[5,3,6,7,82,34,6,8,9,13]
buyuk=0
kucuk=999
for i in range(len(liste)):
    if liste[i]>buyuk:
        buyuk=liste[i]
    if liste[i]<kucuk:
        kucuk=liste[i]
print("""girilen sayilarin en buyugu {}, girilen sayilarin en kucugu {}""".format(buyuk,kucuk))

#4 elinizde bulunan iki adet listeye birlestirerek ucuncu liste olusturan program

liste1=[1,2,3,4,5,6,7]
liste2=["python","java","c","c++","c#","pascal","cobol"]
liste3=[]
for i in range(len(liste1)):
 liste3.append((liste1[i],liste2[i]))
print(liste3)

#5 bir cumledeki bosluklari silen program
a="m e r h a b a l a r"
for i in a :
    if i!=" ":
        print(i,end="")
'''


# ---------------------------- FONKSIYON OLUSTURMA --------------------------- #

#ORNEK def kullanimi
'''
def sayiCiftMi (sayi):
    if sayi%2==0:
        print("sayi cifttir.")
    else:
        print("sayi tektir.")

sayiCiftMi(11) #sayi tektir cevabi veriyor program calisiyor.
'''
#ORNEK 2
'''
def yazdir (metin,kacKere):
    for i in range (1,(kacKere+1)):
        print(metin,end='\n')
        
yazdir("merhabalar",5)
'''
#ORNEK 3
'''
yazdirilacakMetin=input("metni giriniz...")
yazdirmaSayisi=int(input("metin kac kere yazdirilacak ? "))
yazdir(yazdirilacakMetin,yazdirmaSayisi)
'''

#ORNEK calismadi hatali kontrol et
''' 
def asalMi (sayi):
    sayac=2 #tum sayilar 1 e boluneceginden 2 ile baslattik.
    while sayac<=int(sayi/2):
        if sayi%sayac==0:
            return False
        sayac+=1
    return True
asalMi(113)
'''

#ORNEK 
'''
def faktoriyelAl(sayi):
    sonuc=1
    if(sayi==0 or sayi==1):
        print('sonuc= ',1)
    elif sayi>1:
        for i in range(1,sayi+1):
            sonuc*=i
        print('sonuc= ',sonuc)
    else :print('0 veya daha buyuk sayi girmelisiniz')
faktoriyelAl(int(input('faktoriyeli alinacak sayiyi giriniz...')))
''' 
#ORNEK
'''
def agacCiz(agacinYuksekligi,karakter='*'):
    b=agacinYuksekligi
    for i in range (1,agacinYuksekligi+1):
        print(b*" ",(2*i-1)*karakter)
        b-=1
agacYuksekligi=int(input("agacin yuksekligi kac satir olsun ?"))
agacKarakteri=input('agac icin bir sembol veya karakter giriniz...')
if agacKarakteri!=''and agacYuksekligi>=1:
    agacCiz(agacYuksekligi,agacKarakteri[0])
elif agacKarakteri==''and agacYuksekligi>=1:
    agacCiz(agacYuksekligi)
else:print('hatali giris')
'''

#ORNEK
'''
def faktoriyelAl(sayi):
    sonuc=1
    if(sayi==0 or sayi==1):
        sonuc=1
    elif sayi>1:
        for i in range(1,sayi+1,1):
            sonuc*=i
    else:sonuc=-1 #hatali bir islem oldugunu anlamak icin -1 degerini veriyoruz
    return sonuc
sonucumuz=faktoriyelAl(5)
#fonksiyonu bir degiskene atayabiliyoruz
if sonucumuz!=-1:#bir hata olup olmadigini kontrol edelim
    print(sonucumuz)
else:print('bir hata olustu')
'''

#ORNEK hatali tekrar konrol et sayfa 157
'''
def ortalamaBul(sayilar):
    sayilarinToplami=0
    sayilarinOrtalamasi=0
    for i in range(len(sayilar)):
        sayilarinToplami+=sayilar[i]
    sayilarinOrtalamasi=sayilarinToplami/len(sayilar)
    return sayilarinOrtalamasi

sayiAdedi=int(input('kac adet sayinin ortalamasini alacaksiniz: '))
sayilarim=[]
for i in range(0,sayiAdedi):
    print(i+1,'. sayiyi giriniz ? ')
    #indis sifirdan basladigi icin +1 kullandik.
    sayi=int(input())
    sayilarim.append(sayi)
ortalamaBul(sayilarim)
'''

#ORNEK
'''
yas=22
dogumgununMu=True
if dogumgununMu==True:
    yas+=1 
    print('nice yillara yasiniz ',yas)
''' 
#ORNEK hatali calismadi kontrol et
'''
topla=0
def toplamBul(sayiListesi):
    topla=0
    for i in range (len(sayiListesi)):
        topla+=sayiListesi[i]
    return topla
print(topla)
toplamBul([1,2,3,4,5])
'''

# ---------------------- BOLUM SONU ORNEKLERI SAYFA 162 ---------------------- #

#ORNEK 1= CALISMADI KONTROL ET
'''
def puanHesaplama(vizePuani,finalPuani,vizeYuzdesi,finalYuzdesi):
    return ( vizePuani*vizeYuzdesi/100 + finalPuani*finalYuzdesi/100 )
puanHesaplama(50,60,30,70)
'''
#ORNEK 2= listede ki sayilarin tek olanlarin toplamini donduren fonksiyon
'''
def tekSayilariTopla(sayilar):
    sayilarinToplami=0
    for i in range(len(sayilar)):
        if sayilar[i]%2!=0:
            sayilarinToplami+=sayilar[i]
        return sayilarinToplami
tekSayilariTopla([1,2,3,4,5,6,7,9,11,1773,1679])
'''
# ---------------------------------------------------------------------------- #
#                              TURTLE ILE CALISMA                              #
# ---------------------------------------------------------------------------- #

#   ileri =  forward (mesafe)
#   geri  =  backward (mesafe)
#   sag   =  right (aci)
#   sol   =  left (aci)

#ORNEK saga dogru 100 birim giden ok  
'''
import turtle
kalem=turtle.Turtle()
kalem.forward(100)
turtle.done()
'''
#ORNEK RIGHT VE FORWARD FONKSIYONLARIN BERABER KULLANIMI
'''
import turtle
kalem=turtle.Turtle()
kalem.forward(100)
kalem.right(90)
kalem.forward(100)
turtle.done()
'''
#ORNEK RIGHT VE BACKWARD FONKSIYONLARIN BIRLIKTE KULLANIMI
'''
import turtle
kalem=turtle.Turtle()
kalem.backward(100)
kalem.right(90)
kalem.backward(100)
turtle.done()
'''
#ORNEK RIGHT VE FORWARD FONSKIYONLARIN BIRLIKTE KULLANIMI
'''
import turtle
kalem=turtle.Turtle()
kalem.forward(-100.5)
kalem.right(90)
kalem.forward(-100.5)
turtle.done()
'''
#ORNEK LEFT VE FORWARD FONKSIYONLARIN BIRLIKTE KULLANIMI
'''
import turtle
kalem=turtle.Turtle()
kalem.left(45)
kalem.forward(50)
turtle.done()
'''
#ORNEK ACI KULLANARAK sekil cizmek
'''
import turtle 
kalem=turtle.Turtle()
kalem.forward(50)
kalem.right(120)
kalem.forward(50)
kalem.right(120)
turtle.done()
'''
#aci ve uzunluklari kullanicidan alirken input kullanip int veya float degeri donusturmeyi unutma
#ORNEK 
''' 
import turtle
kalem=turtle.Turtle()
mesafe=float(input("cizgi mesafesini giriniz"))
kalem.forward(mesafe)
kalem.right(90)
kalem.forward(mesafe)
turtle.done()
'''
#ORNEK cizgi mesafesini kullanicidan alip sekil cizen program
'''
import turtle
kalem=turtle.Turtle()
mesafe=float(input("cizgi mesafesini giriniz..."))
kalem.forward(mesafe)
kalem.right(90)
kalem.forward(mesafe)
turtle.done()
'''
#ORNEK cizgi mesafesini ve donus acisini kullanicidan alan program
'''
import turtle
kalem=turtle.Turtle()
mesafe=int(input("cizgi mesafesini giriniz.."))
donus_acisi=int(input('donus acisini giriniz..'))
kalem.forward(mesafe)
kalem.right(donus_acisi)
kalem.forward(mesafe)
turtle.done()
'''

# ----------------------------- TURTLE nesnesinde ---------------------------- #
#cizim icin kalem rengi pencolor() veya color(" ") tirnak icinde renk adi
#kalinlik pensize(sayi degeri) seklinde ayarlaniyor.
#ORNEK
'''
import turtle
kalem=turtle.Turtle()

kalem.pencolor("red")
kalem.pensize(3)
kalem.forward(100)
kalem.left(90)
kalem.color("#ACE515")

kalem.pensize(8)
kalem.forward(100)
kalem.left(90)
kalem.pencolor("yellow")

kalem.pensize(6)
kalem.forward(100)
kalem.left(90)
kalem.color("#2259C1")

kalem.pensize(1)
kalem.forward(100)
kalem.left (90)

turtle.done()
'''
# Turtle çizim aracının görünüm şekli için de shape(  ) fonksiyonu bulunmaktadır. Bu fonksiyon ‘arrow’,‘classic’, ‘turtle’, ‘circle’ olmak üzere 4 şekle sahip olabilir.
# Kaplumbağa grafiklerde çizime tekrar dönmek için ilerleme pendown(  ) veya down(  ) ardından forward(  ) fonksiyonları kullanılır.
# Kaplumbağa grafiklerde çizmeden ilerleme penup(  ) veya up(  ) ardından forward(  )
# Kaplumbağa grafiklerde nokta çizme dot(  )
# Kaplumbağa grafiklerde pencerenin istenen noktasına gidebilme goto (x ekseni, y ekseni)

#ORNEK DOT ile cizim uygulamasi
'''
import turtle
kalem=turtle.Turtle()
for i in range(5):
    kalem.dot()
    kalem.forward(20)
turtle.done()
'''
#ORNEK DOT ile cizgisiz sekil uygulamasi
'''
import turtle
kalem=turtle.Turtle()
kalem.up()
for i in range(5):
    kalem.dot()
    kalem.forward(20)
turtle.done()
'''
#ORNEK shape ve goto fonksiyonlarinin kullanimi
'''
import turtle
kalem=turtle.Turtle()
kalem.shape('turtle')
kalem.forward(100)
kalem.penup()
kalem.goto(0,100)
for i in range(5):
    kalem.dot()
    kalem.forward(20)
turtle.done()
'''
#ORNEK shape ve goto fonksiyonlarının farklı bir çizim için kullanımı
'''
import turtle
kalem=turtle.Turtle()
kalem.shape("turtle")
for i in range(4):
 kalem.up()
 kalem.forward(20)
 kalem.dot()
 kalem.down()
 kalem.forward(20)
 kalem.dot()
turtle.done()
'''

# -------------------- TURTLE ILE GEOMETRIK SEKILLER CIZME ------------------- #

# KARE
'''
import turtle
kalem=turtle.Turtle()
kalem.pencolor("red")
kalem.pensize(3)
for i in range(4):
    kalem.forward(100)
    kalem.left(90)
turtle.done
'''

# ALTIGEN
'''
import turtle
kalem=turtle.Turtle()
kalem.pencolor("blue")
kalem.pensize(4)
for i in range(6):
    kalem.forward(100)
    kalem.left(60)
turtle.done()
'''

# --------------------------- BOLUM SONU ORNEKLERI --------------------------- #
#1 YILDIZ
'''
import turtle
yildiz=turtle.Turtle()
for i in range(5):
    yildiz.forward(100)
    yildiz.right(144)
turtle.done
'''
#2 ICICE YILDIZ
'''
import turtle
yildiz=turtle.Turtle()
for i in range(20):
    yildiz.forward(i*10)
    yildiz.right(144)
turtle.done
'''
#3 TEKERLEKIMSI BISEY .d
'''
import turtle
yildiz=turtle.Turtle()
for i in range(50):
    yildiz.forward(100)
    yildiz.right(123)
turtle.done
'''

# ----------------------------- SOZLUK OLUSTURMA ----------------------------- #

#ornek
'''
sozluk1={}
print(sozluk1)

sozluk2={1:'istanbul',2:'izmir'}
print(sozluk2)

sozluk3={'isim':'ahmet',1:[5,4,3]}
print(sozluk3)

sozluk4=dict({1:'armut',2:'kiraz'})
print(sozluk4)
'''
#ornek
'''
sozluk = {"bilgisayar" : "computer","sarı" : "yellow","masa" : "chair"}
print(sozluk)
'''

# --------------------------- BOLUM SONU ORNEKLERI --------------------------- #

# 1= 5 ve 6 elemanli iki demet tanimla once bu iki demeti birlestir sonra eleman sayilarini bul 
'''
demet1=('ahmet','mehemet','osman','tuna','burak')
demet2=('bir','iki','uc','dort','bes','alti')
yeni_demet=tuple(demet1+demet2)
print(len(yeni_demet))
'''

# 2= Sayilar=(20,24,25,79,40,39,50) olan demeti 5e bolunenleri ekrana yazdir
'''
Sayilar=(20,24,25,79,40,39,50)
for meyve in Sayilar:
    if meyve%5==0:
        print (meyve)
'''

# 3=Uygulama=("ali","veli","ayşe","Fatma","Hayriye","ali","deniz") demette kac tane ali var
'''
Uygulama=("ali","veli","ayşe","Fatma","Hayriye","ali","deniz")
print(Uygulama.count("ali"))
'''

# ---------------------------- MODULER PROGRAMLAMA --------------------------- #
#ornek
'''
import math
yaricap=4
alan=math.pi*(math.pow(yaricap,2))
print(alan)
'''
#ornek
'''
import random
print(dir(random)) #random kutuphanesini cagirip module ait ozellikleri yazar
'''
#ornek modul bu methodu kullandigi zaman 0 ile 1 arasinda bir sayi uretir sayi 0 olabilirken 1 olamaz
'''
import random
a=random.random()
print(a)
'''

# integer tipinde sayi uretilmek istenirse randint kullanilir baslangic ve bitis veilir

#ornek 0 dahil degil 10 dahil olmak uzere sayi ureten kod
'''
import random
sayi=random.randint(1,10)
print(sayi) 
'''
#random.choice ile listeden rasgele bir oge secilmesi saglanir
#ornek aylar listesinden random oge secen kod
'''
import random
aylar=['ocak','subat','mart','nisan','mayis','nisan']
print(random.choice(aylar))
'''

#ornek suan ki zamani gosteren kod
'''
import time 
print(time.ctime())
'''

 # --------------------------- BOLUM SONU ORNEKLERI --------------------------- #
#1= 0-20 ye kadar sayilari dongu yapisi ile ekrana yazdirirken her bir sayi arasinda yarim saniye duraklamalar yapan kod
'''
import time
for i in range(1,21):
    time.sleep(0.5)
    print(i)
'''

#2= iki sayinin toplamini yaptiran programi fonksiyon ve modul yazma kullanarak yap
## sayfa 216 cozmeyi dene tekrar

 # ---------------------------------------------------------------------------- #
 #                          ILERI SEVIYE VERI YAPILARI                          #
 # ---------------------------------------------------------------------------- #

# bin() 10 luk tabandaki bir sayiyi 2 lik sistemde ki bir sayiya cevirmak icin kullanilir.
# hex() 10 luk sayi sisteminde ki sayilari 16 lik sistemdeki sayiya cevirmek icin kullanilir.
# abs() fonksiyonu ingilizcede absolute(mutlak) sozcugunun kisaltilmasidir.
# round() fonskiyonu sayiyi belli bir kritere gore assagi veya yukariya yuvarlamaya yarar.
# chr() fonksiyonu kendisine parametre olarak verilen tma sayinin karakter olarak karsiligini verir.
"  chr(65) >>> 'A'  "
# max() fonksiyonu bir dizi icinde ki sayilarin en buyugunu verir.
# min() fonksiyonu max() fonksiyonun tam tersi islem yapar.
# pow() fonksiyonu power sozcugunun kisaltilmasidir. bir sayinin ussunu almak icin kullanilir.
# sum() fonksiyonu dizi icerisinde ki degerlerin toplamini bulmamizi saglar.
# replace() fonskiyonu bir karakter dizisi icerisinde ki karakterle baska karakterlerle degistirmeyi saglar.
'''
a='python'
print(a.replace('p','T'))
'''
# split() fonksiyonu bir karakter dizisini verilen kurala gore bolme islemi yapar.
# upper() ve lower() fonksiyonlari karakter dizilerini buyuk veya kucuk harfe cevirmeyi saglar.
# capitalize() fonksiyonu karakter dizilerin sadece ilk harfini buyuk yapar.
# find() fonksiyonu bir karakter dizisinde ki karakterin konumunu(indis sirasini) sorgular.
# rfind() fonksiyonu find() fonksiyonun benzeri islem yapar ancak arama islemini sag taraftan baslayarak yapar.
# isdiget() fonksiyonu karakter dizisinde sayisal deger olup olmadigini kontrol eder. eger tum karakterler sayi ise TRUE yazar.

# --------------------------- try except kullanimi --------------------------- #
#ornek
'''
try:
 s1 = int(input("Birinci Sayı :"))
 s2 = int(input("İkinci Sayı :"))
 sonuc = s1/s2
 print("Sonuc :",sonuc)
except ZeroDivisionError:
 print("Lütfen ikinci sayıya sıfırdan farklı bir değer girin…")
except ValueError:
 print('Lütfen sayısal bir karakter girin..')
except:
 print("Beklenmeyen bir hata oluştu")
'''

#try except as kullaniciya hata mesajlarini gostermek icin kullanilir.
'''
try:
 s1 = int(input("Birinci Sayı :"))
 sonuc = s1**2
 print("Sonuc :",sonuc)
except ValueError as hata:
 print('Lütfen sayı giriniz')
 print(hata)
'''

# --------------------- BOLUM SONU ORNEKLERI (SAYFA 251) --------------------- #

#1=Kullanıcı tarafından 3 tane sayı girilecek. Bu üç sayı toplanıp ekrana yazdırılacaktır. Hata ayıklama ile programı yapınız.


#2=Kullanıcı tarafından 2 sayı girilip ortalaması alınacaktır. Hata ayıklama ile programı yapınız ve hatayı ekrana yazdırınız.


#3=Kullanıcıdan ad, soyad, yas bilgileri girilip ekrana yazdırılacaktır. Yanlış girilmesi durumunda hata giderilinceye kadar tekrar veri girilmesi sağlanacaktır. Hata ayıklama ile programı yapınız.

# ---------------------------------------------------------------------------- #
#                              SQL LİTE KULLANIMI                              #
# ---------------------------------------------------------------------------- #
#sql lite işlemlerini çalıştırmak için sqlite3 isimli modül kullanılmaktadır.
#bu nedenle import sqlite3 komutunu kullanarak modülü pragrama dahil ediyoruz.
#sqlite3.connect(veritabanı adı) komutu
#sqlite3.connect(veri tabanı adı) ile veri tabanı yok ise oluşturma ve bağlanma, var ise sadece bağlanma işlemi gerçekleştirilir.
#imleç oluşturmak için slite3.cursor() komutu kullanılır.

#örnek 1 = kitaplarım isimli veri tabanı oluşturma
''''
import sqlite3
baglantı=sqlite3.connect("kitaplarim.db")
imlec=baglantı.cursor()
baglantı.close()
'''

#ornek 2 = veri tabaninda tablolar olusturma
'''
import sqlite3
baglantı=sqlite3.connect("kitaplarim.db")
imlec=baglantı.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS kitaplar (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
baglantı.commit()
baglantı.close()
'''

#ornek 3 = veri tabaninda ki tablolara veri ekleme
'''
import sqlite3
baglantı=sqlite3.connect("kitaplarim.db")
imlec=baglantı.cursor()
imlec.execute ("INSERT INTO kitaplar VALUES('dogunun limanları','amin maaluf','ykredi',50)")
baglantı.commit()
baglantı.close()
'''

#ornek 4 = kullanicidan veri alarak tabloya veri ekleme(terminalde)
'''
import sqlite3
def veri_ekle(kitap_adı,kitap_yazar,kitap_yayınevi,kitap_sayfa):
 baglantı=sqlite3.connect("kitaplarim.db")
 imlec=baglantı.cursor()
 imlec.execute("INSERT INTO kitaplar VALUES(?,?,?,?)",(kitap_adı,kitap_yazar,kitap_yayınevi,kitap_sayfa))
 baglantı.commit()
 baglantı.close()
kitap_adı=input("lütfen kitap adı giriniz...")
kitap_yazar=input("lütfen kitabın yazarını giriniz...")
kitap_yayınevi =input("lütfen kitabın yayınevini giriniz...")
kitap_sayfa= int(input("lütfen kitabın sayfa sayısını giriniz..."))
veri_ekle(kitap_adı,kitap_yazar,kitap_yayınevi,kitap_sayfa)
'''

#ornek 5= tablolarda ki tum verileri cekme islemi
'''
import sqlite3
baglanti=sqlite3.connect('kitaplarim.db')
imlec=baglanti.cursor()
imlec.execute('SELECT*FROM kitaplar')
gelen_veri_listesi=imlec.fetchall()
print(type(gelen_veri_listesi))
print(gelen_veri_listesi)
baglanti.close()
'''

# ------------------------ tablodaki veriyi guncelleme ----------------------- #

#Sql dilinde veri güncelleme işlemi: “UPDATE tablo_adı SET yeni_değer WHERE değişecek değer”
'''
import sqlite3
baglantı=sqlite3.connect("kitaplarim.db")
imlec=baglantı.cursor()
imlec.execute (" UPDATE kitaplar SET Yayınevi= ? WHERE Yayınevi=?",('YKY ', 'ykredi'))
baglantı.commit()
baglantı.close()
'''

# ---------------------------- tablodan veri silme --------------------------- #

#Sql dilinde veri silme işlemi: “DELETE FROM tablo_adı WHERE koşulumuz”
'''
import sqlite3
baglantı=sqlite3.connect("kitaplarim.db")
imlec=baglantı.cursor()
imlec.execute (" DELETE FROM kitaplar WHERE Yayınevi='yky'")
baglantı.commit()
baglantı.close()
'''

#ornek 10= kullanicinin gircegi kitap ismine uyan verileri silen program.
'''
import sqlite3
baglanti=sqlite3.connect("kitaplarim.db")
imlec=baglanti.cursor()
kitap_adi=input("silmek istediginiz kitabin adini giriniz lutfen ")
imlec.execute("DELETE FROM kitaplar WHERE İsim=?",(kitap_adi,))
baglanti.commit()
baglanti.close()
'''

#ornek 11= sirket veri tabani ve personel tablosu olusturma
''''
import sqlite3
baglanti=sqlite3.connect("sirket.db")
imlec=baglanti.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS personel (kimlik_no INT, ad_soyad TEXT, telefon_no TEXT, e_posta TEXT, rolu TEXT, calisilan_birim TEXT)")
baglanti.commit()
baglanti.close()
'''

#ORNEK 12= veri tabani olusturduktan sonra veri ekleme,guncelleme,sorgulama ve silme islemlerini tek bir program ile yapabilecegi kod
"""
import sqlite3
baglanti=sqlite3.connect("sirket.db")
imlec=baglanti.cursor()
def veri_ekle(veri):
    bilgiler=veri.split(",")
    imlec.execute("INSERT INTO personel VALUES(?,?,?,?,?,?)",(bilgiler[0],bilgiler[1],bilgiler[2],bilgiler[3],bilgiler[4],bilgiler[5]))
    baglanti.commit()

def veri_getir(sorgu_metni):
    imlec.execute(sorgu_metni)
    sonuc=imlec.fetchall()
    print("veri tabaninda bulunan kayitlar...")
    for satir in sonuc:
        print(satir)
    print("toplam",len(sonuc),"adet kayit listelenmistir.")

def veri_sil(sorgu_metni):
    imlec.execute(sorgu_metni)
    baglanti.commit()

def veri_guncelle(sorgu_metni):
    imlec.execute(sorgu_metni)
    baglanti.commit()

while True:
    secim=input(
'''
    |---------------------------------------------|
        | yapmak istediğiniz işlemi seçiniz |
        | 1- veri ekleme işlemi             |
        | 2- veri sorgulama işlemi          |
        | 3- veri güncelleme işlemi         |
        | 4- veri silme işlemi              |
        | E- programı sonlandırma işlemi    |
    |---------------------------------------------|
''')
    if secim=='1':
        veri=input('''kimlik numarasi,ad soyad, telefon,e posta, rolu, calisilan birim bilgilerini araya virgul koyarak yaziniz''')
        veri_ekle(veri)
    elif secim=='2':
        sorgu=input('lutfen sorgu yapmak sql metnini giriniz.')
        veri_getir(sorgu)
    elif secim=='3':
        sorgu=input("lutfen veri guncelleme icin gerekli metni giriniz.")
        veri_guncelle(sorgu)
    elif secim=='4':
        sorgu=input("lutfen sorgu yapmak icin gereken sql metnini girniz")
        veri_sil(sorgu)
    elif secim=="E":
        baglanti.close()
        break
    else:
        print("listede olmayan bir secim yaptiniz...")
    print("program sonlandirildi.")
"""

# --------------------------- BOLUM SONU ORNEKLERI --------------------------- #

# 1= Okul adında bir veritabanı oluşturup personel adında tablo oluşturunuz. Örnek tablo alanları ve veri tipleri kimlik_no INT ,ad_soyad TEXT, telefon_no TEXT,e_posta TEXT,rolu TEXT,çalışılan_birim TEXT
'''
import sqlite3
baglanti=sqlite3.connect("okul.db")
imlec=baglanti.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS personel (kimlik_no INT, ad_soyad TEXT, telefon_no TEXT,e_posta TEXT,rolu TEXT,calisilan_birim TEXT)")
baglanti.commit()
baglanti.close()
'''

# 2= Okul veri tabanında personel kimlik numarasına göre bilgilerini ekrana getiren programı yazınız.
'''
import sqlite3
baglanti=sqlite3.connect("okul.db")
imlec=baglanti.cursor()
kimlik_no=input("bilgilerini gormek istediginiz personelin kimliik no giriniz...")
sorgu="SELECT*FROM personel WHERE kimlik_no=' "+kimlik_no+" ' "
imlec.execute(sorgu)
bilgiler=imlec.fetchall()
print(bilgiler)
baglanti.close()
'''

# 3= Okul veri tabanında ogrenci adında tablo oluşturunuz.Örnek tablo alanları ve veri tipleri ogrenci_no INT ,ad_soyad TEXT, telefon_no TEXT,e_posta TEXT,sınıfı TEXT,veli_adı TEXT,veli_numarası TEXT
'''
import sqlite3
baglanti=sqlite3.connect("okul.db")
imlec=baglanti.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenci(ogrenci_no INT ,ad_soyad TEXT, telefon_no TEXT,e_posta TEXT,sınıfı TEXT,veli_adı TEXT,veli_numarası TEXT)")
baglanti.commit()
baglanti.close()
'''

# 4= Okul veri tabanında öğrenci bilgilerinin tamamını güncelleyebilen programı yazınız
####calismadi kontrol et
"""
import sqlite3
baglanti=sqlite3.connect("okul.db")
imlec=baglanti.cursor()
ogrenci_no=input("bilgilerini gormek istediginiz ogrencinin numarasini giriniz.")
sorgu="SELECT*FROM ogrenci WHERE ogrenci_no=' "+ogrenci_no+" ' "
imlec.execute(sorgu)
bilgiler=imlec.fetchall()
print(bilgiler)
yeni_bilgiler=input(''' lutfen yeni bilgileri araya virgul koyarak giriniz
ogrenci_no, ad soyad, telefon no, e posta, sınıfı,veli adı, veli telefon numarası:\n ''')
liste=yeni_bilgiler.split(",")
sorgu="UPDATE ogrenci SET ogrenci_no =?,ad_soyad=?,telefon_no=?,e_posta=?,sınıfı=?,veli_adı=?,veli_numarası=? WHERE ogrenci_no=?"
imlec.execute(sorgu,(liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],ogrenci_no))
baglanti.commit()
baglanti.close()
"""

# 5= okul veritabanina veri ekeleme 
"""
import sqlite3
baglantı=sqlite3.connect("okul.db")
imlec=baglantı.cursor()
imlec.execute ("INSERT INTO ogrenci VALUES('555','ahmet','538','aet@gmail','B3','adem','543')")
baglantı.commit()
baglantı.close()
"""

# ---------------------------------------------------------------------------- #
#                          ILERI SEVIYE FONSKSIYONLAR                          #
# ---------------------------------------------------------------------------- #⁡
#   tek bir kod satırında güçlü ve işlevsel özellikler oluşturabilmemize olanak SAGLAYAN
#   List Comprehension, lambda, map, filter ve reduce fonksiyonları ornekleri

# ---------------------------- list comprehension ---------------------------- #

#-for dongusu kullanarak liste olusturma
'''
liste1=[1,2,3,4,5,6]
liste2=[]
for i in liste1:
    liste2.append(i)
print(liste2)
'''

#-list comprehension metodu icinde for dongusu kullanarak liste olusturma
"""
liste1=[1,2,3,4,5,6,7]
liste2=[i for i in liste1]
print(liste2)
"""

#-list comprehension metodu içinde for döngüsü kullanarak liste elemanlarının karesini alma
'''
liste1=[3,4,5,6,8,1,2]
liste2=[i**2 for i in liste1]
print(liste2)
'''

#-list comprehension metodu ile 1’den 10’a kadar sayılardan oluşan bir liste oluşturma.
'''
liste2=[i for i in range(11)]
print(liste2)
'''

#-list comprehension metodu ile Stringler üzerinde gezinme işlemleri
'''
yazi="ahmet"
liste=[i*3 for i in yazi]
print(liste)
'''

#-list comprehension metodu ile İç içe listeleri birleştirerek tek bir liste üzerinde birleştirme.
"""
liste1=[[1,2,3],[4,5,6],[7,8,9]]
liste2=[j for i in liste1 for j in i]
print(liste2)
"""

#-list comprehension metodu ile çift Sayıları bulan uygulama
"""
liste=[i for i in range(1,20)if i%2==0]
print(liste)
"""

# ------------------------- OZYINELEMELI FONKSIYONLAR ------------------------ #

#faktoriyel hesaplama
"""
faktoriyel=1
sayi=int(input("faktoriyelini hesaplamak istediginiz sayiyi girin..."))
if sayi>=0:
    for i in range(1,sayi+1):
        faktoriyel*=i
print (faktoriyel)
"""

#faktoriyel hesaplayan fonksiyon
"""
def faktoriyel_hesapla(sayi):
    faktoriyel=1
    if sayi>=0:
        for i in range(1,sayi+1):
            faktoriyel*=i
    return faktoriyel
sayi=int(input("faktoriyelini hesaplamak istediginiz sayiyi giriniz"))
print(faktoriyel_hesapla(sayi))
"""

#ozyineleme metodu ile faktoriyel hesaplama
"""
def faktoriyel_hesapla(sayi):
    faktoriyel=1
    if sayi==1:
        return 1
    else:
        return sayi*faktoriyel_hesapla(sayi-1)
sayi=int(input("faktoriyelini hesaplamak istediginiz sayiyi giriniz "))
print (faktoriyel_hesapla(sayi))
"""

#ozyineleme metodu ile fibonacci terim sayisini hesaplama
"""
def fibonacci(n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
sayi=int(input("hesaplanmasini istediginiz fibonacci terim sayisini gioriniz "))
print(fibonacci(sayi))
"""

#for dongusu ile toplam hesaplama
"""
sayi=int(input("kendisine kadar olan sayilarin toplamini hesaplamak istediginiz sayiyi giriniz..."))
toplam=0
for i in range (1,sayi+1):
    toplam+=i
print(toplam)
"""

#ozyineleme yontemi ile toplam hesaplama
"""
def topla (sayi):
    if sayi==1:
        return 1
    else:
        return sayi+topla(sayi-1)
sayi=int(input("kendisine kadar olan sayilarin toplamini hesaplamak istediginiz sayiyi giriniz..."))
print(topla(sayi))
"""

# --------------------------- Lambda Fonksiyonlari --------------------------- #
#Argümanlar giriş - ifadeler çıkış değerleridir. Kullanım şekli: Lambda arguman : ifadeler şeklindedir.
# ---------------------------------------------------------------------------- #

#lambda fonksiyonu kullanim 
"""
x=lambda a:a+15
print(x(5))
"""

#lambda fonksiyonu ile hipotenus hesaplama
"""
import math
hipotenus=lambda x,y:math.sqrt(x*x+y*y)
print(hipotenus(3,4))
"""

#lambdanin direkt kullanim sekli
"""
print((lambda x,y:3*x+5*y)(2,5))
"""

# ------------------------------ MAP FONKSIYONU ------------------------------ #
# Map fonksiyonu bir işlemin veya fonksiyonun birden çok veriye tek satırda uygulanmasını sağlayan pratik fonksiyonlardan biridir. 
# Map fonksiyonu for döngüsü kullanarak yapılabilecek işlemlerin tek satırda çözümlesine olanak tanır. 
# Map fonksiyonun kullanımı şu şekildedir: 
# map(fonksiyon,iterasyon yapılabilecek veri tipi(liste,demet vb),)
# ---------------------------------------------------------------------------- #

# for dongusu ile kisiye ozel davetiye metni olusturma
"""
def davetiye_metni (isim):
    gonderilecek_metin="Sayin "+isim+"\n"+"bu mutlu gunumuzde sizleri de aramizda gormekten mutluluk duyariz."
    return gonderilecek_metin
isimler=['ali','ahmet','emir','omer']

for birey in isimler:
    print(davetiye_metni(birey))
"""

# map fonksiyonu ile kisiye ozel davetiye metni olusturma
"""
def davetiye_metni (isim):
    gonderilecek_metin="Sayin "+isim+"\n"+"bu mutlu gunumuzde sizleri de aramizda gormekten mutluluk duyariz.\n"
    return gonderilecek_metin
isimler=['ali','ahmet','emir','omer']

davetiye=map(davetiye_metni,isimler)
print(davetiye)     #davetiye değişkeninin bellekteki konumunu yazdırır.
print(*davetiye)    #davetiye değişkeninin değerini yazdırır.
"""

# map ve lambda fonskiyonlarinin birlikte kullanimi
"""
isimler=['ahmet','bilge','emir','ezgi','omer']
yeni_liste=map(lambda x:"sayin "+x+"\n etkinligimize davetlisiniz.\n", isimler)
print(*yeni_liste)
"""

# ----------------------------- REDUCE FONKSIYONU ---------------------------- #
# reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular. 
# Daha sonra çıkan sonucu listenin 3. elemanına uygular. 
# Bu şekilde devam ederek liste bitince bir tane değer döner. 
# Reduce fonksiyonu functools modülünde olduğundan bu modülü dâhil ediyoruz
# ---------------------------------------------------------------------------- #

#REDUCE ornegi
"""
from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))
"""

#REDUCE ile faktoriyel hesaplama
"""
import functools
sayi=int(input("faktoriyelini bulmak istediginiz sayiyin giriniz. "))
liste=[i for i in range(1,sayi+1)]
print(functools.reduce(lambda x,y:x*y,liste))
"""

# ----------------------------- FILTER FONKSIYONU ---------------------------- #
# filter() fonksiyonu liste veri tipindeki yapılar için kullanılır. 
# Kullanım şekli: filter(fonksiyon1, liste1)
# ---------------------------------------------------------------------------- #

# filter fonksiyonu ornek kullanimi
"""
def buyuk_harf(isim):
    return isim.isupper()
liste=['AHMET','emre','ali','ece']
sonuc=filter(buyuk_harf,liste)
print(*sonuc)
"""

# uce bolunebilen sayilari ekrana yazdirma. lambda fonskiyonu yardimi ile
"""
sayilar=[10,14,15,25,27,35,41,36,69, ]
sonuc=filter(lambda x:(x%3==0),sayilar)
print(*sonuc) 
"""

# bakiyesi 150 den buyuk olan musterileri secen program. lambda ve reduce yardimi ile
"""
# musteriler listesi musteri no ile bakiye miktari
musteriler=[[1,22],[2,234],[3,432],[4,155]]
sonuc=filter(lambda x:(x[1]>149),musteriler)
print(*sonuc)
"""

# ---------------------------------------------------------------------------- #
#                        BOLUM SONU ORNKELERI SAYFA 300                        #
# ---------------------------------------------------------------------------- #

# SORU 1=
# SORU=5’ten başlayıp 20’ye kadar olan çift sayılardan oluşan bir listeyi list comprehension kullanarak yapınız
# CEVAP hatali
"""
liste=[ i for i in range(5,21,2)]
print(liste)
"""

# SORU 2=
# liste1=[“ahmet”,“ayşe”,“metin”] listesinden list comprehension metodu ile verilerin başına sayın ifadesi gelecek şekilde ([‘Sayın ahmet’, ‘Sayın ayşe’, ‘Sayın metin’]) liste2 adında bir liste o
# CEVAP
"""
liste1=["ahmet","emre","musatafa"]
liste2=["Sayin "+i for i in liste1]
print(liste2)
"""

# SORU3=
# Elinizde bir teste ait cevap anahtarı ve öğrenci cevaplarının olduğu listeler var. 
# siz bu cevapları anahtar ile kontrol ederek sonuçları doğru veya yanlış olarak çıktı almak istiyorsunuz.
# Bunu yapacak kodları lambda ve map fonksiyonları ile nasıl yaparsınız.
# Örnek: cevap_anahtarı=[“a”,“c”,“e”,“b”,“a”] ogrenci_1=[“a”,“d”,“d”,“b”,“a”]
# İstenen çıktı Çıktı: [‘doğru’, ‘yanlıs’, ‘yanlıs’, ‘doğru’, ‘doğru’]
# CEVAP
"""
cevap_anahtarı=["a","b","c","d","e"]
ogrenci_1=['a','b','e','d','c']
liste2=list(map(lambda x,y:"dogru" if x==y else "yanlis",cevap_anahtarı,ogrenci_1))
print(liste2)
"""

# ---------------------------------------------------------------------------- #
#                           NESNE TABANLI PROGRAMLAMA                          #
# ---------------------------------------------------------------------------- #

# bir sinif tanimlama

"""
class orneksinif():
    __doc__='bu sinif ornek amacli olusturulmustur.'
    def __init__(self):
        print("merhab sinif")
"""

# siniftan bir nesne olusturma
"""
nesnem=orneksinif()
print(nesnem)
print(nesnem.__doc__)
"""

# yapici "___init___()" fonksiyonu
"""
class metinSinifi:
    def __init__(self,ifade,tekrarSayisi,kacisKarakteri):
        print((ifade+kacisKarakteri)*tekrarSayisi)
nesnem=metinSinifi("sinif olusturduk.",5,"\n")

"""

# asiri yukleme (over loading)

# ----------------------- masa lambasi sinifi olusturma ---------------------- #
"""
class masaLambasi:
    isikRengi='sari'    #ozellik
    isikDurum=False     #ozellik
    def isikAc(self):   #ozellik
        self.isikDurum=True
        return'aydinlik'
"""
# -------------------- sinifinizi adiyla cagirabilirsiniz -------------------- #
"""
print(masaLambasi.isikRengi)
"""
#--- Sinifinizdan bir nesne turetebilir ve sinifinizdan tanimladiginiz ozelliklere erisebilirsiniz---#
"""
lambam=masaLambasi()
print(lambam.isikAc())
print(lambam.isikDurum)
"""
# ------- olusturdugunuz nesneyi silmek icin del() fonksiyonu kullanma ------- #
"""
del(lambam)
print(lambam.isikDurum)
#nesne silindigi icin hata ile karsilasilir
"""

# --- masa lambasi sinifini yeniden tanimlama. farkli ozellik ve islev ekleme --- #
class masaLambasi:
    __doc__='masa lambasi sinifi'
    isikDurum=False
    def __init__(self, isikSiddeti,isikRengi='kirmizi',garantiSuresi=2):
        self.isikSiddeti=isikSiddeti
    def isikAc(self):
        self.isikDurum=True
    def isikKapat(self):
        self.isikDurum=False
    def isigiArtir(self,artirmaMiktari):
        self.isikSiddeti+=artirmaMiktari

#--- Sinifinizdan bir nesne turetin. Bunun icin parametrelere degerleri giriniz ---#
lambam=masaLambasi(60,garantiSuresi=3)

# ---------- nesnenin ozelliklerini ve islevlerini kullanabilirsiniz --------- #
# ---------------------------------------------------------------------------- #
lambam.isikAc()         # simdi isigi acalim
print('isik acik mi ?',lambam.isikDurum)    #isigin durumu
# ---------------------------------------------------------------------------- #
lambam.isigiArtir(5)    # isik siddetini artirma
print('isik siddeti:',lambam.isikSiddeti)
# ---------------------------------------------------------------------------- #
lambam.isikKapat()      # isigi kapatma
print('isik acik mi ?',lambam.isikDurum)
# ---------------------------------------------------------------------------- #

