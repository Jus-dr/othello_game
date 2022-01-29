
harfler={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
takim={0:"Beyaz",1:"Siyah"}#takımlar 0 ve 1 olarak geçiyor ve burada string anlamlarını tanımladım
BEYAZ=0#Kolay kodlama için 0 ve 1 i takım isimlerine atadım
SIYAH=1
sira=BEYAZ#başlangıç sırası beyazda

def tahta_yap(yatay):#tahtayı oluşturmak için method. satır sayısını argüman olarak alıyor
    global tahta,beyaztaslar,siyahtaslar
    dikey = yatay +1 
    tahta = [[" " for i in range(dikey)] for j in range(yatay)] #satır sayısının bir fazlası olarak içi boşluk stringiyle dolu bir tahta oluşturuyor
    beyaztaslar,siyahtaslar=int((yatay*(dikey))/2),int((yatay*(dikey))/2)#yerleştirme aşamasında eldeki taşları saymak için her renk için iki değişken

def tahta_ciz():#her hamleden sonra tahtayı tekrar çizdirmek için bir method tanımladım

    print("  ",end="")#daha sonra tahta uzunluğu kadar harfleri aralarında ikişer boşluk bırakarak yazıyoruz
    i=0
    for harf in harfler:
        if i ==len(tahta)+1:
            break
        print(harf+"   ",end="")
        i+=1
    print("")
    #bu for da ise her satırı olduğu gibi aralarında 3 çizgi olacak şekilde ve dikeyleri de ekleyerek çizdiriyorum
    for i in range(len(tahta)):
        print(str(i+1)+" "+"---".join(tahta[i])+" "+str(i+1))
        if i !=len(tahta)-1:
            print("  "+"|   "*(len(tahta)+1))
    #en alta yine harfleri çizdiriyoruz
    print("  ",end="")
    i=0
    for harf in harfler:
        if i ==len(tahta)+1:
            break
        print(harf+"   ",end="")
        i+=1
    print("")

def kordinat_ver(girilen_kordinat):#kullanıcıdan gelen kordinat girdisinin doğruluğunu, tahtada var olup olmadığını test edip array halinde sayısal kordinat olarak returnluyoruz. işimizi kolaylaştırması için yaptığm bir method
    if len(girilen_kordinat)!=2 or not girilen_kordinat[0].isdigit() or not girilen_kordinat[1].isupper() or girilen_kordinat[0]=="0":#önce istediğmiz kordinat formatında olup olmadığını kontrol ediyoruz
        return False
    harfler2=["A","B","C","D","E","F","G","H"]#burada maksimum tablo büyüklüğündeki harflerden şuanki tablo büyüklüğüne indirdiğimizde kalan harfleri alıyoruz çünkü birazdan test edilen kordinatlar tahtanın içinde mi onu test edeceğiz
    while len(harfler2)!=len(tahta)+1:
        harfler2.pop()
    if int(girilen_kordinat[0]) in range(len(tahta)+1) and girilen_kordinat[1] in harfler2:#eğer kullanıcıdan gelen kordinat girdisi oyun tahtasının içerisinde ise
        return [int(girilen_kordinat[0])-1,harfler[girilen_kordinat[1]]]#2 elemanla arrayın içinde sayısal hallerini returnluyoruz
    else:
        return False#istedğimiz formatta değilse yada tahta içinde değilse false yolluyoruz

    #üstteki methodun aynısı ama arada boşluk olan iki kordinat bilgisini alıp sayısal kordinat olarak veriyor.
def ikikordinat_ver(girilen_kordinat):
    if len(girilen_kordinat)!=5 or not girilen_kordinat[0].isdigit() or not girilen_kordinat[1].isupper() or girilen_kordinat[0]=="0" or not girilen_kordinat[3].isdigit() or not girilen_kordinat[4].isupper() or girilen_kordinat[3]=="0":
        return False
    harfler2=["A","B","C","D","E","F","G","H"]
    while len(harfler2)!=len(tahta)+1:
        harfler2.pop()
    if int(girilen_kordinat[0]) in range(len(tahta)+1) and girilen_kordinat[1] in harfler and int(girilen_kordinat[3]) in range(len(tahta)+1) and girilen_kordinat[4] in harfler2:
        return [[int(girilen_kordinat[0])-1,harfler[girilen_kordinat[1]]],[int(girilen_kordinat[3])-1,harfler[girilen_kordinat[4]]]]
    else:
        return False

def hareket_kontrol(nereden,nereye):#hareket edilmek istenen noktaya kadar arada başka taş var mı yada o nokta müsait mi onu test ettiğimiz method
    if tahta[nereye[0]][nereye[1]]!=" " or nereden==nereye:#varış noktası boşsa  yada varış ve kalkış eşitse false yolluyoruz direkt
        return False
    elif nereden[0]==nereye[0]:#eğer satır kordinatları aynıysa yolculuk sütunlar arası demektir.
        x=nereden[1]#başlangıçtan varışa tek tek noktaları kontrol ediyorum ve hepsi boşluk ise true yolluyorum. arada engel denk gelirse false yolluyorum
        while x!=nereye[1]:
            if x<nereye[1]:
                x+=1
            else:
                x-=1
            if x==nereye[1]:
                return True
            if tahta[nereden[0]][x]!=" ":
                return False

    elif nereden[1]==nereye[1]:#eğer sütunlar aynıysa yolculuk satırlar arası demektir
        y=nereden[0]#üsttekinin aynısı ama bu sefer satırlar arası engeller test edilmekte.
        while y!=nereye[0]:
            if y<nereye[0]:
                y+=1
            else:
                y-=1
            if y==nereye[0]:
                return True
            if tahta[y][nereden[1]]!=" ":
                return False
    else:
        return False

def tas_say():#tahtadaki beyaz ve siyah taşları sayıp iki elemanlı array olarak returnlayan bir method. oyunda kaç taş kalmış bulmak için yaptım.
    taslar=[0,0]#başlangıç olarak 0
    for i in range(len(tahta)):#tahta boyu gezilip her kordinatta kaç B veya S taşı varsa sayılıp artırma yapılıyor
        for j in range(len(tahta)+1):
            if tahta[i][j]=="B":
                taslar[BEYAZ]+=1
            if tahta[i][j]=="S":
                taslar[SIYAH]+=1
    return taslar

def kare_say():#ilk eleme aşamasında oyuncular kaçar kare oluşturmuş onları sayan bir method. sonuç olarak iki elemanlı array döndürüyor.
    beyazkare=0
    siyahkare=0
    for i in range(len(tahta)-1):
        for j in range(len(tahta)):
            if tahta[i][j]=="B" and tahta[i][j+1]=="B" and tahta[i+1][j]=="B" and tahta[i+1][j+1]=="B":#eğer bir taşın sağında altında ve sağ altında aynı taş var ise o bir karedir.
                beyazkare+=1
            if tahta[i][j]=="S" and tahta[i][j+1]=="S" and tahta[i+1][j]=="S" and tahta[i+1][j+1]=="S":
                siyahkare+=1
    return [beyazkare,siyahkare]

def kare_mi(cords):#verilen bir noktadaki taşın bir karenin parçası olup olmadığını anlamak için yaptığım fonksiyon. eğer öyle ise kaç kareye bağlı onu sayıp döndürüyor
    kareler=0
    try:#burada try kullandım çünkü noktanın sağını solunu üstünü altını kontrol ediyoruz kare mi diye. eğer tahtanın kenarında yada köşesinde bir nokta ise indexerror alırız. hatayı aldığımız anda zaten kare değildir diyip pass yapıyoruz.
        if tahta[cords[0]][cords[1]]==tahta[cords[0]][cords[1]+1] and tahta[cords[0]][cords[1]]==tahta[cords[0]+1][cords[1]] and tahta[cords[0]][cords[1]]==tahta[cords[0]+1][cords[1]+1]:
            kareler+=1
    except:
        pass
    try:#kare sayma taktiğimi aynı, bir nokta 4 taraftan kareya bağlı olabilir, 4 try ile deniyoruz. var ise kareler sayısını artırıyoruz
        if tahta[cords[0]][cords[1]]==tahta[cords[0]][cords[1]-1] and tahta[cords[0]][cords[1]]==tahta[cords[0]+1][cords[1]] and tahta[cords[0]][cords[1]]==tahta[cords[0]+1][cords[1]-1]:
            kareler+=1
    except:
        pass
    try:
        if tahta[cords[0]][cords[1]]==tahta[cords[0]][cords[1]+1] and tahta[cords[0]][cords[1]]==tahta[cords[0]-1][cords[1]] and tahta[cords[0]][cords[1]]==tahta[cords[0]-1][cords[1]+1]:
            kareler+=1
    except:
        pass
    try:
        if tahta[cords[0]][cords[1]]==tahta[cords[0]][cords[1]-1] and tahta[cords[0]][cords[1]]==tahta[cords[0]-1][cords[1]] and tahta[cords[0]][cords[1]]==tahta[cords[0]-1][cords[1]-1]:
            kareler+=1
    except:
        pass
    if kareler:#eğer temas edilen bir kare var ise onu döndürüyoruz yok ise false döndürüyoruz
        return kareler
    else:
        return False

def tek_eleme():#oyun ortasında tek bir eleme için kullandığım method
    elememusait=False#rakibin elenebilir bir taşı olup olmadığını test ediyoruz burada
    for i in range(len(tahta)):
        for j in range(len(tahta)+1):
            if sira==BEYAZ and tahta[i][j]=="S":#eğer rakibin bütün taşları kareler içindeyse elenebilir bir taşı yoktur.
                if kare_mi([i,j])==False:#ama bir tane bile kare olmayan taş bulunursa elenebilir taş vardır.
                    elememusait=True
            if sira==SIYAH and tahta[i][j]=="B":
                if kare_mi([i,j])==False:
                    elememusait=True

    if not elememusait:#elenebilir taş yok ise method sonlandırılıyor.
        input("Yeni bir kare oluşturdun ama rakibin elenecek bir taşı yok!\nSıra geçiyor")
        return

    tahta_ciz()#yeni tahta çizilip kullanıcıdan elenecek taşın kordinatı isteniyor
    print("--- Yeni bir kare oluşturdun! ---")
    print("Rakibin bir taşını eleyebilirsin")
    print("Oynama sırası:"+takim[sira])#sırası olan oyuncuyu belirtmek için takim sözlüğünü ve sira değişkenini kullanıyoruz.
    while 1:
        elenecek_kordinat=input("Elenecek rakip taşının kordinatı:")#düzgün bir input alınana kadar döngüye alıyoruz
        cords=kordinat_ver(elenecek_kordinat)#girdiyi test ediyoruz
        if cords==False:#eğer false döndüyse continue ile döngüyü başa sarıp input alıyoruz
            print("Geçersiz kordinat tekrar deneyin")
            continue
        if kare_mi(cords):#eğer bu kordinattaki taş bir karenin parçasıysa yine tekrar input istiyoruz
            print("Oluşmuş bir karenin parçasını eleyemezsiniz. Tekrar deneyin")
            continue
        if sira==BEYAZ and tahta[cords[0]][cords[1]]=="S":#sıra beyazınsa ve istenilen taş siyahınsa o kordinattaki taşı kaldırıyoruz
            tahta[cords[0]][cords[1]]=" "
            break
        elif sira==SIYAH and tahta[cords[0]][cords[1]]=="B":#sıra siyahsa da durum tam tersi
            tahta[cords[0]][cords[1]]=" "
            break
        else:
            print("Geçersiz rakip taşı tekrar deneyin")#bunlar dışında başka bir durum varsa tekrar girdi istiyoruz
    if 3 in tas_say():#silme işleminden sonra eğer tahtada 3 taşı kalan bir oyuncu varsa oyunsonunu çağırıyoruz.
        oyunsonu()


def oyunsonu():#oyunsonu
    if 3 in tas_say():#oyunun bitme sebebi, birisinin normal yolla kaybetmesi ise
        input("--- "+takim[not tas_say().index(3)]+" OYUNU KAZANDI ---")#kazananı taşı 3 olmayan oyuncu olandan bulup ekrana yazdırıyoruz
    else:
        input("--- Kazanan yok oyun berabere ---")#normal yolla oyun bitmediyse kazanan yoktur beraberedir.
    exit()

def basla():#ilk ve tek dışarıdan çağırılan method. oyunu başlatır
    print("---Kare kapan oyununa hoşgeldiniz!---")
    print(" ")
    while 1:
        yatay=input("Oyun alanı büyüklüğünü giriniz(en az 3 en çok 7):")
        if yatay in ["3","4","5","6","7"]:#tahta büyüklüğünü min maks olarak seçtirip tahtayap methoduyla oluşturuyoruz.
            tahta_yap(int(yatay))
            break
        else:
            print("Geçersiz tahta büyüklüğü tekrar deneyin\n")
    yerlestirme_asamasi()#ilk yerleştirme aşaması çağırılıyor
    eleme_asamasi()#o bitince ilk eleme asamasi
    oyun_asamasi()#o bitince oyun_asamasi

def oyun_asamasi():#oyuncuların taş hareket ettirip oluşturdukları karelerle eleme yaptıkları aşama.
    global sira
    while 1:#bir kazanan çıkana kadar sonsuz döngü
        tahta_ciz()#her hamlede tahta tekrar çiziliyor, ve oyun sırası gösteriliyor
        print("--- Oyun Aşaması ---")
        print("Taşlarını hareket ettirip yeni kareler oluşturmaya çalış!")
        print("Oynama sırası:"+takim[sira])
        while 1:#kullanıcıdan düzgün bir girdi gelene kadar döngü
            yer_degistirme_kordinati=input("Hareket kordinatları:")
            cords=ikikordinat_ver(yer_degistirme_kordinati)#ikikordinatver methoduyla girdideki iki kordinat ayıklanıyor.
            if cords==False:#düzgün formatta değillerse tekrar isteniyor
                print("Geçersiz kordinat tekrar deneyin")
                continue
            nereden,nereye=cords#kordinatları nereden ve nereye olarak ayırıyoruz
            if sira==BEYAZ and tahta[nereden[0]][nereden[1]]=="B" and hareket_kontrol(nereden,nereye):#eğer sıra beyazınsa ve oynatılmak istenen taş B ise ve hareket edilmek istenen noktaya güzergah temiz isetaş hareket ettiriliyor.
                tahta[nereden[0]][nereden[1]]=" "
                tahta[nereye[0]][nereye[1]]="B"
                if kare_mi(nereye):#eğer hamle sonucu yeni kare oluşturulmuş ise oluşturulan kare kadar tek eleme methodu çağırılıyor ve oyuncuya eleme yaptırılıyor
                    for i in range(kare_mi(nereye)):
                        tek_eleme()
                sira=not sira#sonra sıra geçiyor
                break

            elif sira==SIYAH and tahta[nereden[0]][nereden[1]]=="S" and hareket_kontrol(nereden,nereye):#siyah içinde aynı olaylar ama tam tersi
                tahta[nereden[0]][nereden[1]]=" "
                tahta[nereye[0]][nereye[1]]="S"
                if kare_mi(nereye):
                    for i in range(kare_mi(nereye)):
                        tek_eleme()
                sira=not sira
                break

            else:#başka bir girdi olursa tekrar girdi isteniyor.
                print("Geçersiz hamle. Tekrar deneyin")
        #bir oyuncu kazanana kadar oyun devam ediyor.


def eleme_asamasi():#yerleştirmeden sonra yapılan elemeler bu method içerisinde
    global sira
    elemehaklari=kare_say()#toplam kaç kare yapılmış karesay ile sayıyoruz
    if elemehaklari==[0,0]:#eğer hiç kare yapılmamışsa oyun beraberedir oyun sonu çağırılıyor
        oyunsonu()
        return
    elememusait=False#eleme yapılabilecek taş var mı o test ediliyor.
    for i in range(len(tahta)):
        for j in range(len(tahta)+1):
            if kare_mi([i,j])==False:
                elememusait=True

    if not elememusait:#hiç elenecek taş yoksa oyun kilittir. oyunsonu çağırılıyor.
        input("Elenecek müsait bir taş yok!")
        oyunsonu()
        return
    while elemehaklari!=[0,0]:#kareler ve müsait taşlar var ise, eleme hakları iki tarafında 0 olana kadar sırayla taş elettiriyoruz.
        if 3 in tas_say():#bu sırada iki taraftan birinde 3 taş kalırsa oyun sonu çağırılıyor
            oyunsonu()
            return
        if elemehaklari[sira]==0:#eğer sırası gelen oyuncunun eleme hakkı yok ama diğerinin hala var ise sıra pas geçiyor.
            sira=not sira
            continue
        tahta_ciz()#her hamleden sonra tahta tekrar çizdiriliyor, taş eleme hakları ve oyun sırası görüntüleniyor.
        print("--- Eleme Aşaması ---")
        print("Beyazın kare sayısı:"+str(elemehaklari[BEYAZ]))
        print("Siyahın kare sayısı:"+str(elemehaklari[SIYAH]))
        print("Oynama sırası:"+takim[sira])
        while 1:#oyuncudan düzgün bir girdi gelene kadar döngü
            elenecek_kordinat=input("Elenecek rakip taşının kordinatı:")
            cords=kordinat_ver(elenecek_kordinat)#kordinat girdisi kontrol ediliyor düzgün değilse tekrar isteniyor
            if cords==False:
                print("Geçersiz kordinat tekrar deneyin")
                continue
            if kare_mi(cords):#oluşmuş bir karenin parçası istenmiş ise tekrar girdi isteniyor
                print("Oluşmuş bir karenin parçasını eleyemezsiniz. Tekrar deneyin")
                continue
            if sira==BEYAZ and tahta[cords[0]][cords[1]]=="S":#eğer düzgün bir girdi ise, karşı o kordinattaki taş siliniyor ve sıra geçiyor.
                tahta[cords[0]][cords[1]]=" "
                elemehaklari[sira]-=1
                sira=not sira
                break
            elif sira==SIYAH and tahta[cords[0]][cords[1]]=="B":
                tahta[cords[0]][cords[1]]=" "
                elemehaklari[sira]-=1
                sira=not sira
                break
            else:
                print("Geçersiz rakip taşı tekrar deneyin")#yukardakilerin hiçbiri değilse yine tekrar input isteniyor
    #tüm eleme hakları bitince asıl oyun aşaması başlıyor


def yerlestirme_asamasi():
    global beyaztaslar,siyahtaslar,sira
    while beyaztaslar!=0 or siyahtaslar!=0:#oyuncuların ellerinde hiç taş kalmayana kadar yerleştirme yapılacak
        tahta_ciz()#her hamleden sonra tahta yeniden çizliyor ve elde kalan taşlarla birlikte sıra kimdeyse o görüntüleniyor
        print("--- Yerleştirme Aşaması ---")
        print("Beyazın yerleştireceği kalan taşı:"+str(beyaztaslar))
        print("Siyahın yerleştireceği kalan taşı:"+str(siyahtaslar))
        print("Oynama sırası:"+takim[sira])
        while 1:#oyuncudan düzgün bir hamle gelene kadar döngü
            yerlestirilecek_kordinat=input("Yerleştirilecek kordinat:")
            cords=kordinat_ver(yerlestirilecek_kordinat)#kordinatın düzgünlüğü test ediliyor
            if cords==False:
                print("Geçersiz kordinat tekrar deneyin")
                continue
            if tahta[cords[0]][cords[1]]!=" ":#kordinat boş değil ise tekrar input isteniyor
                print("Bu kordinat dolu tekrar deneyin")
                continue
            if sira==BEYAZ:#sıra beyazdaysa o kordinata B harfi koyuluyor ve sıra siyaha geçiliyor
                tahta[cords[0]][cords[1]]="B"
                sira=SIYAH
                beyaztaslar-=1#eldeki taşlardanda azaltma yapılıyor
                break
            if sira==SIYAH:#siyah içinde durum aynı
                tahta[cords[0]][cords[1]]="S"
                sira=BEYAZ
                siyahtaslar-=1
                break
            #tüm taşlar yerleştirilince ilk eleme aşaması başlıyor.

basla()#başlatılıyor
