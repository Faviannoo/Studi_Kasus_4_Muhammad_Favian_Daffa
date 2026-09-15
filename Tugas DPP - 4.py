buku = {
    "buku1" : {
        "judul" : "Madilog",
        "penulis" : "Tan Malaka",
        "tahun" : "1943",
    },
    "buku2" : {
        "judul" : "Bedebah Di Ujung Tanduk",
        "penulis" : "Tere Liye",
        "tahun" : "2021",
    },
    "buku3" : {
        "judul" : "Sisi Tergelap Surga",
        "penulis" : "Brian Khrisna",
        "tahun" : "2023",
    }
}

while True:
    print("=== Pengelolaan Buku ===") 
    print()
    print("1. Tampilkan Buku")
    print("2. Tambah Penerbit")
    print("3. Ubah Penulis")
    print("4. Hapus Penerbit")
    print("5. Keluar")
    print()

    pilih = input("Pilih Menu (1 - 5): ")
    print()

    if pilih == "1":
        print("=== DATA BUKU ===")
        
        print("Buku ke- 1")
        print("Judul Buku   :", buku["buku1"]["judul"])
        print("Penulis      :", buku["buku1"]["penulis"])
        print("Tahun Terbit :", buku["buku1"]["tahun"])
        print("Penerbit     :", buku["buku1"].get("penerbit", "------"))
        print()

        print("Buku ke - 2")
        print("Judul Buku   :", buku["buku2"]["judul"])
        print("Penulis      :", buku["buku2"]["penulis"])
        print("Tahun Terbit :", buku["buku2"]["tahun"])
        print("Penerbit     :", buku["buku2"].get("penerbit", "------"))
        print()

        print("Buku ke - 3")
        print("Judul Buku   :", buku["buku3"]["judul"])
        print("Penulis      :", buku["buku3"]["penulis"])
        print("Tahun Terbit :", buku["buku3"]["tahun"])
        print("Penerbit     :", buku["buku3"].get("penerbit", "------"))
        print()

    elif pilih == "2":
        print("=== TAMBAH PENERBIT ===")
        print()
        print("Pilih Buku Yang Ingin Ditambah Penerbitnya")
        print("1. Madilog")
        print("2. Bedebah Di Ujung Tanduk")
        print("3. Sisi Tergelap Surga")
        print()
        pilih_buku = input("Pilih buku (1 - 3) : ")

        if pilih_buku == "1":
            penerbit = input("Masukkan Penertbit : " )
            buku["buku1"]["penerbit"] = penerbit
            print("Penerbit Berhasil Ditambahkan")

        elif pilih_buku == "2" :
            penerbit = input("Masukkan Penertbit : " )
            buku["buku2"]["penerbit"] = penerbit
            print("Penerbit Berhasil Ditambahkan")

        elif pilih_buku == "3":
            penerbit = input("Masukkan Penerbit: ")
            buku["buku3"]["penerbit"] = penerbit
            print("Penerbit berhasil ditambahkan!")
        else:
            print("Pilihan Buku Tidak Tersedia")

    elif pilih == "3":
        print("=== UBAH PENULIS ===")
        print()
        print("Pilih Buku Yang Ingin Diubah Penulisnya")
        print("1. Madilog")
        print("2. Bedebah Di Ujung Tanduk")
        print("3. Sisi Tergelap Surga")
        print()
        pilih_buku = input("Pilih buku (1 - 3) : ")

        if pilih_buku == "1":
            peenulis = input("Masukkan Nama Penulis : " )
            buku["buku1"]["penulis"] = peenulis
            print("Penulis Berhasil Diubah")

        elif pilih_buku == "2" :
            peenulis = input("Masukkan Nama Penulis : " )
            buku["buku2"]["penulis"] = peenulis
            print("Penulis Berhasil Diubah")

        elif pilih_buku == "3":
            peenulis = input("Masukkan Nama Penulis : " )
            buku["buku3"]["penulis"] = peenulis
            print("Penulis Berhasil Diubah")         
        else:
            print("Pilihan Buku Tidak Tersedia")

    elif pilih == "4":
        print("=== HAPUS PENERBIT ===")
        print()
        print("Pilih Buku Yang Ingin Dihapus Penerbitnya")
        print("1. Madilog")
        print("2. Bedebah Di Ujung Tanduk")
        print("3. Sisi Tergelap Surga")
        print()
        pilih_buku = input("Pilih buku (1 - 3) : ")

        if pilih_buku == "1":
            if "penerbit" in buku["buku1"]:
                del buku["buku1"]["penerbit"]
                print("Penerbit Berhasil Dihapus!")
            else:
                print("Data Penerbit Belum Ada!")

        elif pilih_buku == "2" :
            if "penerbit" in buku["buku1"]:
                del buku["buku2"]["penerbit"]
                print("Penerbit Berhasil Dihapus!")
            else:
                print("Data Penerbit Belum Ada")
                            
        elif pilih_buku == "3":
            if "penerbit" in buku["buku1"]:
                del buku["buku3"]["penerbit"]
                print("Penerbit Berhasil Dihapus")
            else:
                print("Dat Penerbit Belum Ada")
        else:
            print("Pilihan Buku Tidak Tersedia")

    elif pilih == "5":
            print("Terimakasih Telah Menggunakan Program Ini")
            break
    else:
        print("Pilihan Tidak Valid. Silakan Pilih Menu 1-5.")