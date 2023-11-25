def anamenu():
   
    print("=======================")
    print("= 1-Yılan oyunu       =")
    print("=2-                   =")
    print("=======================")
    print("=======================")
    secim =input()
    if secim == "1":
        import yilan_oyunu
        yilan_oyunu.baslat()
        anamenu()
    if secim == "2":
        pass

anamenu()
    
    
