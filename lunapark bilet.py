print("Lunapark hızlı trenine hoşgeldiniz")
boy=int(input("Boyunuzu girin:"))
if boy>=120:
    print("Hız trenine girebilirsiniz")
    yas=int(input("Bilet almak için yaşınızı girin:"))
    if yas<12:
        print("Bilet ücreti: 20")
    elif yas<=18:
        print("Bilet ücreti: 35")
    else:
        print("Bilet ücreti:50")
else:
    print("Maalesef hızlı trene binme şartını sağlamıyorsunuz")