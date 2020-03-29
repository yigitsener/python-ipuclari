"""1. Biz dizi içerisinden başka bir dizye ulaşma"""
# Bir liste oluşturalım
a = [1,3,5,7,9,11,13]
# Ardışık tek sırayla giden listeyi
# Range() fonksiyonuyla da oluşturabilirdik

a = [t for t in range(1,14,2)]
print(a)
# ÇIKTI: [1, 3, 5, 7, 9, 11, 13]

a[:3] # ilk üç değer
# ÇIKTI: [1, 3, 5]

a[2:] # ikinci değerden sonrakiler
# ÇIKTI: [5, 7, 9, 11, 13]

a[:] # tüm liste

# Liste içinde çoklu seçimi range() fonksiyonu
# gibi düşünülebilir.
# Örnek: a[başlangıç : durduğu yer : atlanılacak adım]

a[2:5] # 2. ve 5. sıra arasındaki sayıları veirir
# ÇIKTI: [5, 7, 9]

a[2:6:3] # 2. değer ile 6. Değer arasında 3 değer atalyacak
# 2. değerin karşığı 5
# 6. değer 13 ancak o hesaplamdan hariç tutulur
# ÇIKTI: [5, 11]

"""2. Bir diziniyi tersine çevirme"""
birliste = [t for t in range(10,20,2)]
print(birliste)
# ÇIKTI: [10, 12, 14, 16, 18]

birliste[::-1] # tersine çeviren ifade
# ÇIKTI: [18, 16, 14, 12, 10]

# Aynı yöntemi tuple üzerinde deneyelim
birtuple = (10, 12, 14, 16, 18)
birtuple[::-1]
# ÇIKTI: (18, 16, 14, 12, 10)

# Bir string üzerinde deneyelim
birstring = "sosyoloji"
birstring[::-1]
# ÇIKTI:  'ijoloysos'

"""3. Tersine çevirme ile son bölümü yakalama"""
birstring = "sosyoloji"
birstring[::-1] # tersine çevirdiğimiz durum
birstring[-4:-1] # sadece "log" ifadesini aldığımız kısım
# ÇIKTI: 'loj'

"""4. Çok değişkenlerin birbirlerine atanması"""
# a = 10 ve b = 15 değişkenleri aşağıdaki gibi yapılabilir
a, b = 10, 15
print(f'a = {a} ve b = {b} olduğu görülmektedir')
# ÇIKTI: 'a = 10 ve b = 15 olduğu görülmektedir'

# Değişkenlerdeki değerlerin birbiri ile yer değiştirmesi
a, b = b, a
print(f'a = {a} ve b = {b} olduğu görülmektedir')
# ÇIKTI: 'a = 15 ve b = 10 olduğu görülmektedir'

# Liste içindeki ilk ve son değerlerin yer değiştirmesi
birliste = [10, 12, 14, 16, 18]
birliste[0], birliste[-1] = birliste[-1], birliste[0]
birliste
# ÇIKTI: [18, 12, 14, 16, 10]

"""5. Veri tiplerinin içerisinin boş olup olmadığı kontrolü"""
bosListe = [set(), (), "", [], {}] # liste içinde boş veri tipleri
for eleman in bosListe:
    if not eleman: # eğer eleman yoksa
        print(f"{type(eleman)} tipinde herhangi bir eleman yok")

# ÇIKTI: <class 'set'> tipinde herhangi bir eleman yok
# ÇIKTI: <class 'tuple'> tipinde herhangi bir eleman yok
# ÇIKTI: <class 'str'> tipinde herhangi bir eleman yok
# ÇIKTI: <class 'list'> tipinde herhangi bir eleman yok
# ÇIKTI: <class 'dict'> tipinde herhangi bir eleman yok

"""6. List Comprehensions"""
# Range ile bir liste oluşturması da bu metoda dahildir
birliste = [eleman for eleman in range(7,13)]
birliste
# ÇIKTI: [7, 8, 9, 10, 11, 12]

# Yarattığımız liste içindeki sayıların karesini alalım
birlisteninkaresi = [x**2 for x in birliste]
birlisteninkaresi
# ÇIKTI: [49, 64, 81, 100, 121, 144]

# kakerlerini bulduğumuz listede 81'den büyüklerin kare kökünü alalım
birlistekosul =  [x**0.5 for x in birlisteninkaresi if x > 81]
birlistekosul
# ÇIKTI: [10.0, 11.0, 12.0]

"""7. Set Comprehensions"""
birliste = [10,10,20,20,30,30,42] # bir liste oluşttu
# Bu listeyi {} içerisinde set comprehension yapısına dönüştürüyoruz
birset = {eleman / 2 for eleman in birliste}
birset
# ÇIKTI: {5.0, 10.0, 15.0, 21.0}
# Çıktıda görüldüğü üzere tekil sonuçlar yazılmıştır.

"""8. Dict Comprehensions"""
birliste = [e for e in range(5)]
birsozluk = {x: x**2 for x in birliste}
birsozluk
# ÇIKTI: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

"""9. Generator Kullanımı"""
sum(x**2 for x in range(10))
# ÇIKTI: 285
max((x**2 for x in range(10)))
# ÇIKTI: 81

"""10. Tuple Çözümlemesi"""
birtuple = (5, 5.2,'yedi', 6, 7, 'sekiz')
print(f"Bu veri yapısı bir {type(birtuple)}'dır")
# ÇIKTI: Bu veri yapısı bir <class 'tuple'>'dır

# Farklı değişkenlere elementlerin atanması
a, b, c, d, e, f = birtuple
print(c, type(c))
# ÇIKTI: 'yedi' <class 'str'>

# Yıldız verilen değişken isimleri
# Diğer değişkenlerden kalan yerlerdeki verileri üzerine alır
x, *y, z = birtuple
print(x) # ÇIKTI: 5
print(y) # ÇIKTI: [5.2, 'yedi', 6, 7]
print(z) # ÇIKTI: 'sekiz'

*y,z = birtuple
print(y) # ÇIKTI:  [5, 5.2, 'yedi', 6, 7]
print(z) # ÇIKTI: 'sekiz'

*_,y = birtuple
print(y) # ÇIKTI: 'sekiz'

"""11.enumerate() kullanımı"""

birliste = ["istanbul","izmir","kars","kastamonu"]
for i,j in enumerate(birliste):
    print(i,j)
# ÇIKTI: 0 istanbul
# ÇIKTI: 1 izmir
# ÇIKTI: 2 kars
# ÇIKTI: 3 kastamonu

# indeks 34'ten başlatılabilir
# Bu seger liste yerine tuple kullanılıyor
birtuple = ("istanbul","izmir","kars","kastamonu")
for i,j in enumerate(birliste,34):
    print(i,j)
# ÇIKTI: 34 istanbul
# ÇIKTI: 35 izmir
# ÇIKTI: 36 kars
# ÇIKTI: 37 kastamonu

"""12. Reversed() Kullanımı"""
birliste = ["Kahve","Meyve","Tatlı","Ana Yemek","Çorba"]
for eleman in reversed(birliste):
    print(eleman)
# ÇIKTI: Çorba
# ÇIKTI: Ana Yemek
# ÇIKTI: Tatlı
# ÇIKTI: Meyve
# ÇIKTI: Kahve

"""13. Zip() Kullanımı"""
meyveler = ["muz","elma","karpuz"]
adetler = [5,8,2]
kilolar = [1.5, 2.1, 3.8]

for meyve, adet, kilo in zip(meyveler,adetler,kilolar):
    print(f"Meyve adı: {meyve}, Adet: {adet}, Kilo: {kilo}")
# ÇIKTI: Meyve adı: muz, Adet: 5, Kilo: 1.5
# ÇIKTI: Meyve adı: elma, Adet: 8, Kilo: 2.1
# ÇIKTI: Meyve adı: karpuz, Adet: 2, Kilo: 3.8

# zip() fonksiyonu tersine çevirme
zipli = zip(meyveler,adetler,kilolar)
x, y, z = zip(*zipli)
print(x)
# ÇIKTI: ('muz', 'elma', 'karpuz')

"""14. Sıralama için lambda kullanımı"""
listeicindesozluk = [{'isim': 'Bursa', 'populasyon': 3.2},
                     {'isim': 'Ankara', 'populasyon': 5.6},
                     {"isim":"istanbul", 'populasyon': 15.5}]
# sıralama fonksiyonun çalıştırılması
sorted(listeicindesozluk, key=lambda x: x["populasyon"],reverse=True)
# ÇIKTI:
# [{'isim': 'istanbul', 'populasyon': 15.5},
# {'isim': 'Ankara', 'populasyon': 5.6},
# {'isim': 'Bursa', 'populasyon': 3.2}]

"""15. Tek Satırda Koşul Yazımı"""
birliste = ["kara","hava","deniz"]
# Normal durumda koşullu ifade
if "kara" in birliste:
    x = 1
else:
    x = 0
print(x)
# ÇIKTI: 1

# Tek satırda yazımı
x = 3 if "deniz" in birliste else 0
print(x)
# ÇIKTI: 3

"""16. in operatörünün kullanımı"""
birtuple = (8,6,9,10,12345)
if 12345 in birtuple:
    print("Bu değer tuple içerisinde var")
# ÇIKTI: Bu değer tuple içerisinde var

birsozluk = {"isim":"mehmet","bölge":"anadolu"}
if "isim" in birsozluk.keys():
    print("Bu değer tuple içerisinde var")
# ÇIKTI: Bu değer tuple içerisinde var

"""17. get() Fonksiyonun Kullanımı"""
birsozluk = {1:"x",2:"y",3:"z"}
birsozluk[1]
# CIKTI: 'x'

# Örneğin sözlükte bulunmayan 4 değerini çağıralım
birsozluk[4]
# Aşağıdaki gibi bir hata dönüyor
# Traceback (most recent call last):
#     bizsozluk[4]
# KeyError: 4

# Hata yerine istediğimiz değeri verebiliriz
birsozluk.get(4,"Böyle bir key yok")
# ÇIKTI: 'Böyle bir key yok'

"""18 Sözlükki maksimum değerin anahtarını getirme"""
modelSonuclari = {"SVM":0.78,"Regression":0.64,"Bayes":0.70}
# Normal yok
anahtar, deger = list(modelSonuclari.keys()), list(modelSonuclari.values())
print(anahtar) # ÇIKTI: ['SVM', 'Regression', 'Bayes']
print(deger) # ÇIKTI: [0.78, 0.64, 0.7]

# Maksimum değerden anahtarın bulunması
anahtar[deger.index(max(deger))]
# ÇIKTI: 'SVM'

# Kısa yol
max(modelSonuclari, key=modelSonuclari.get)
# ÇIKTI: 'SVM'

# minimum için
min(modelSonuclari, key=modelSonuclari.get)
# ÇIKTI: 'Regression'

"""19. Print() fonksiyonun farklı kullanımları"""
# 11 rakamına kadar değerlerin bulunduğu bir liste oluşturalım.
birliste = [e for e in range(11)]
print(birliste)
# ÇIKTI: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tek rakamları ve çift rakamları ayrı sütunlarda gösterelim
for i in birliste:
    print("# ÇIKTI: ",i, end=", " if i % 2 == 1 else '\n' )
# ÇIKTI:  1, # ÇIKTI:  2
# ÇIKTI:  3, # ÇIKTI:  4
# ÇIKTI:  5, # ÇIKTI:  6
# ÇIKTI:  7, # ÇIKTI:  8
# ÇIKTI:  9, # ÇIKTI:  10

"""20. Walrus Operatörünin Kullanımı"""
birliste = [t for t in range(10)]
# if koşulundaki n liste içerisindeki eleman sayısına eşitleniyor
# Yani n eleman sayısı kadar bir rakam almış yeni bir değişken
if (n := len(birliste))%2 == 1:
    print(f"{n} adet eleman listede yer almaktadır")
# ÇIKTI: '10 adet eleman listede yer almaktadır'

"""21. String ifadelerde split() ve rsplit"""
birstring = "veri bilimi, alanında, oldukça, fazla, kaynak, bulunmaktadır."
# virgül ve boşluk dahil ayırarak liste içine alma
birstring.split(", ")
# ÇIKTI: ['veri bilimi', 'alanında', 'oldukça', 'fazla', 'kaynak', 'bulunmaktadır.']

# split(,x) x yazan yere verilen değer ile
# Bölmeye işlemine dahil edilmeyen karakter sayısı yazılır
birstring.split(", ",2)
# ÇIKTI: ['veri bilimi', 'alanında', 'oldukça, fazla, kaynak, bulunmaktadır.']

# rsplit(,x) ise tam tersi yönten başlayarak karakterleri ayırır
birstring.rsplit(", ",2)
# ÇIKTI: ['veri bilimi, alanında, oldukça, fazla', 'kaynak', 'bulunmaktadır.']

"""22. string join() işlemleri"""
kelimelerlistesi = ["masa","bilgisayar","haber"]
"%".join(kelimelerlistesi) # liste içerindeki kelimler seçilen karakter ile birleştiriliyor
# ÇIKTI:  'masa%bilgisayar%haber'

# sözlüklerde kullanımı
kelimlersozluk = {0: "masa", 1: "bilgisayar", 2: "haber"}
"+".join(kelimlersozluk.values())
# ÇIKTI: 'masa+bilgisayar+haber'

"""23. Map() Fonksiyonu"""
rakamlar = [1,2,3,4,5]
usler = [5,6,7,8,9]

# map() kullanımı
list(map(pow, rakamlar, usler))
# ÇIKTI: [1, 64, 2187, 65536, 1953125]

# list comprehensions yöntemi
[pow(x, y) for x, y in zip(rakamlar, usler)]
# ÇIKTI: [1, 64, 2187, 65536, 1953125]

"""24. Filter() Fonksiyonu"""
# harf listesi
harfler = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# sesli harfleri filtreleyen fonksiyon
def sesliHarfFiltresi(harfler):
    sesliHarfler = ['a', 'e', 'i', 'o', 'u']

    if(harfler in sesliHarfler):
        return True
    else:
        return False

sesliHarfleriFiltrele = filter(sesliHarfFiltresi, harfler)

# Sesli harf filtresinden çıkanlar
for harf in sesliHarfleriFiltrele:
    print(f"# ÇIKTI: Sesli harf {harf}")
# ÇIKTI: Sesli harf a
# ÇIKTI: Sesli harf e
# ÇIKTI: Sesli harf i
# ÇIKTI: Sesli harf o

"""25. Sık geçen değerleri bulma"""
kazananlar = ["ali","veli","veli","merve"]
max(set(kazananlar), key = kazananlar.count)
# ÇIKTI: 'veli'
