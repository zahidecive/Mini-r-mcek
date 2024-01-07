import time
from dataURL import DataURL
from getURL import GetURL

useDataURL = DataURL()
useGetURL = GetURL()

print("-: Mini Örümceğe hoş geldiniz! :-")
print("|------------------------------|")
print("")
time.sleep(2)

while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
    menuSecim = input("Tercihiniz: ")

    if menuSecim.isdigit():
        menuSecim = int(menuSecim)

        if menuSecim == 0:
            print("Mini Örümcek kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            useDataURL.dataRead()
        elif menuSecim == 2:
            useDataURL.dataWrite()
        elif menuSecim == 3:
            useGetURL.getWeb()
        elif menuSecim == 4:
            useGetURL.getList()
        else:
            print('Geçersiz bir seçim yaptınız. Lütfen menüdeki rakamlardan birini giriniz.')
    else:
        print('Geçersiz bir seçim yaptınız. Lütfen menüdeki rakamlardan birini giriniz.')
