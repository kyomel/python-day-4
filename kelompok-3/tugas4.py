uang_masuk = []
uang_keluar = []

while True:
    print("Pilih menu (masuk/keluar/sum masuk/sum keluar/sum all)")
    pilihan = input()

    if pilihan == 'masuk':
        uang = int(input("Masukkan jumlah uang masuk: "))
        uang_masuk.append(uang)
        print("List uang masuk: ", uang_masuk)

    elif pilihan == 'keluar':
        uang = int(input("Masukkan jumlah uang keluar: "))
        uang_keluar.append(uang)
        print("List uang keluar: ", uang_keluar)

    elif pilihan == 'sum masuk':
        print("Jumlah uang masuk: ", sum(uang_masuk))

    elif pilihan == 'sum keluar':
        print("Jumlah uang keluar: ", sum(uang_keluar))

    elif pilihan == 'sum all':
        print("Selisih uang masuk dan uang keluar: ", sum(uang_masuk) - sum(uang_keluar))