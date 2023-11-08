def para ():
    tl=int(input("Lütfen hesaplanacak tutarı giriniz; "))
    işlem_list = input("İşlem listesini görmek için 'L'ye basınız").lower()
    if işlem_list== "l":
        işlem=["Dolar","Euro","Sterlin"]
        for i in işlem:
            print(i)

    Döviz = input("Lütfen dönüştürmek istediğiniz Dövizi giriniz; ").lower()
    if Döviz == "dolar":
        print(tl/28.5)
    elif Döviz == "euro":
        print(tl/30.5)
    elif Döviz == "sterlin":
        print(tl/35)
    else:
        print("Lütfen geçerli bir işlem birimi giriniz")
    para()
para()
        