from tabulate import tabulate

list_alat = [
    {"Kode_Barang": "TND001", "nama_alat": "Tenda Dome 4P", "Kategori": "Tenda", "Stock": 5, "Harga": 50000},
    {"Kode_Barang": "TND002", "nama_alat": "Tenda Dome 2P", "Kategori": "Tenda", "Stock": 8, "Harga": 30000},
    {"Kode_Barang": "MSK001", "nama_alat": "Kompor Portable", "Kategori": "Alat Masak", "Stock": 12, "Harga": 15000},
    {"Kode_Barang": "MSK002", "nama_alat": "Panci Camping", "Kategori": "Alat Masak", "Stock": 10, "Harga": 20000},
    {"Kode_Barang": "SLP001", "nama_alat": "Sleeping Bag", "Kategori": "Perlengkapan Tidur", "Stock": 15, "Harga": 25000},
    {"Kode_Barang": "SLP002", "nama_alat": "Matras Lipat", "Kategori": "Perlengkapan Tidur", "Stock": 20, "Harga": 10000},
    {"Kode_Barang": "TSK001", "nama_alat": "Tas Carrier 60L", "Kategori": "Tas", "Stock": 7, "Harga": 40000},
    {"Kode_Barang": "TSK002", "nama_alat": "Tas Carrier 40L", "Kategori": "Tas", "Stock": 10, "Harga": 30000},
    {"Kode_Barang": "LAM001", "nama_alat": "Lampu LED Camping", "Kategori": "Lampu", "Stock": 18, "Harga": 12000},
    {"Kode_Barang": "LAM002", "nama_alat": "Headlamp", "Kategori": "Lampu", "Stock": 25, "Harga": 15000}
]

list_customer = [
    {"ID_Customer": "CST001", "Nama": "Budi Santoso", "No_HP": "081234567890", "Alamat": "Jl. Merdeka No. 10, Jakarta"},
    {"ID_Customer": "CST002", "Nama": "Ani Wijaya", "No_HP": "085678901234", "Alamat": "Jl. Raya Bogor No. 25, Bogor"},
    {"ID_Customer": "CST003", "Nama": "Doni Prasetyo", "No_HP": "089876543210", "Alamat": "Jl. Sudirman No. 15, Bandung"},
    {"ID_Customer": "CST004", "Nama": "Siti Rahma", "No_HP": "082345678901", "Alamat": "Jl. Diponegoro No. 8, Surabaya"},
    {"ID_Customer": "CST005", "Nama": "Ahmad Fauzan", "No_HP": "087654321098", "Alamat": "Jl. Gajah Mada No. 20, Semarang"}
]

list_sewa = [
    {"No_Sewa": "S001", "Nama": "Budi Santoso","nama_alat":"Tenda Dome 4P", "No_HP": "081234567890", "Durasi":"3 Hari","Total_Harga":200000, "Status": "Sudah Kembali"},
    {"No_Sewa": "S002", "Nama": "Budi Santoso","nama_alat":"Tenda Dome 4P", "No_HP": "081234567890", "Durasi":"3 Hari","Total_Harga":200000, "Status": "Belum Kembali"}
]

#Function barang

def tampil_nbarang():
    if not list_alat:
        print("Daftar Kosong.")
    else:
        headers = ["No","Kode Barang", "Nama Alat", "Kategori", "Stock", "Harga"]
        data = [[i, item["Kode_Barang"], item["nama_alat"], item["Kategori"], item["Stock"], f"Rp {item['Harga']:,}".replace(",", ".")] for i, item in enumerate(list_alat, start=1)]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def tampil_kategori():
    # Ambil daftar kategori unik
    kategori_list = list(set(item["Kategori"] for item in list_alat))
    
    # Tampilkan daftar kategori dengan angka
    print("Pilih Kategori:")
    for i, kategori in enumerate(kategori_list, start=1):
        print(f"{i}. {kategori}")
    while True :
        try:
            # Minta input angka dari pengguna
            pilihan = int(input("\nMasukkan nomor kategori yang ingin ditampilkan: "))

            if 1 <= pilihan <= len(kategori_list):
                kategori_terpilih = kategori_list[pilihan - 1]
                data_filtered = [item for item in list_alat if item["Kategori"] == kategori_terpilih]

                # Tampilkan hasil dalam tabel
                headers = ["Kode Barang", "Nama Alat", "Kategori", "Stock", "Harga"]
                data = [[item["Kode_Barang"], item["nama_alat"], item["Kategori"], item["Stock"], f"Rp {item['Harga']:,}".replace(",", ".")] 
                        for item in data_filtered]

                print(f"Daftar Alat dalam Kategori: {kategori_terpilih}")
                print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
                break
            else:
                print("Nomor kategori tidak valid.")

        except ValueError:
            print("Input harus berupa angka.")


def create_alat():
    try:
        print("Daftar Barang")
        tampil_nbarang()
        
        # Validasi kode barang unik
        while True:
            kode_barang = input("Masukkan Kode Barang: ").upper()
            if any(item["Kode_Barang"] == kode_barang for item in list_alat):
                print("Kode Barang sudah ada. Silakan masukkan kode yang berbeda.")
            else:
                break  # Kode barang valid
        
        nama_alat = input("Masukkan Nama Alat: ").title()
        kategori = input("Masukkan Kategori: ").title()

        # Validasi input angka untuk stock dan harga
        while True:
            try:
                stock = int(input("Masukkan Stock: "))
                harga = int(input("Masukkan Harga: "))
                break  # Keluar dari loop jika input valid
            except ValueError:
                print("Input tidak valid. Stock dan Harga harus berupa angka.")

        # Menampilkan data yang akan disimpan
        print("\nData yang dimasukkan:")
        print(f"Kode Barang : {kode_barang}")
        print(f"Nama Alat   : {nama_alat}")
        print(f"Kategori    : {kategori}")
        print(f"Stock       : {stock}")
        print(f"Harga       : Rp{harga:,}")  # Format harga dengan pemisah ribuan
        
        # Konfirmasi penyimpanan data
        putusan = input("Simpan data? (Y/N): ").upper()
        if putusan == "Y":
            list_alat.append({
                "Kode_Barang": kode_barang,
                "nama_alat": nama_alat,
                "Kategori": kategori,
                "Stock": stock,
                "Harga": harga
            })
            print(f"\nBarang berhasil ditambahkan: {nama_alat} (Kode: {kode_barang})")
            tampil_nbarang()
        else:
            print("Data batal disimpan.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def update_barang():
    tampil_nbarang()  # Tampilkan semua barang sebelum mulai update
    
    if not list_alat:
        print("Tidak ada barang yang tersedia.")
        return
    
    while True:
        try:
            index = int(input("\nMasukkan No Index barang yang ingin diperbarui: "))
            if 1 <= index <= len(list_alat):  # Pastikan index valid
                index -= 1
                break
            else:
                print("No Index tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka.")

    barang = list_alat[index]  # Ambil barang berdasarkan index yang dipilih
    print(f"\nKode Barang: {barang['Kode_Barang']}, Nama Alat: {barang['nama_alat']}, Kategori: {barang['Kategori']}, Stock: {barang['Stock']}, Harga: {barang['Harga']}")

    while True:
        print("\nSub-Menu Update:")
        print("1. Ubah Nama Alat")
        print("2. Ubah Kategori")
        print("3. Ubah Stock")
        print("4. Ubah Harga")
        print("5. Kembali")

        
        pilihan = int(input("Pilih menu yang ingin diperbarui: "))
        
        match pilihan:
            case 1:
                nama_baru = input(f"Masukkan Nama Alat Baru (sebelumnya '{barang['nama_alat']}'): ").title()
                putusan = input("Simpan data? (Y/N): ").upper()
                if nama_baru :
                    if putusan == "Y":
                        barang["nama_alat"] = nama_baru
                        print("Nama Alat berhasil diperbarui.")
                        tampil_nbarang()
                    else :
                        print("Data Batal Disimpan")
                else:
                    print("Nama tidak boleh kosong.")

            case 2:
                kategori_baru = input(f"Masukkan Kategori Baru (sebelumnya '{barang['Kategori']}'): ").title()
                putusan = input("Simpan data? (Y/N): ").upper()
                if kategori_baru :
                    if putusan == "Y":
                        barang["Kategori"] = kategori_baru
                        print("Kategori berhasil diperbarui.")
                        tampil_nbarang()
                    else :
                        print("Data Batal Disimpan")
                else:
                    print("Kategori tidak boleh kosong.")

            case 3:
                try:
                    stock_baru = int(input(f"Masukkan Stock Baru (sebelumnya {barang['Stock']}): "))
                    putusan = input("Simpan data? (Y/N): ").upper()
                    if stock_baru >= 0:
                        if putusan == "Y":  
                            barang["Stock"] = stock_baru
                            print("Stock berhasil diperbarui.")
                            tampil_nbarang()
                        else :
                            print("Data Batal Disimpan")
                    else:
                        print("Stock harus berupa angka positif.")
                except ValueError:
                    print("Input tidak valid. Stock harus berupa angka.")

            case 4:
                try:
                    harga_baru = int(input(f"Masukkan Harga Baru (sebelumnya Rp {barang['Harga']:,}): "))
                    putusan = input("Simpan data? (Y/N): ").upper()
                    if harga_baru >= 0:
                        if putusan == "Y":
                            barang["Harga"] = harga_baru
                            print("Harga berhasil diperbarui.")
                            tampil_nbarang()
                        else :
                            print("Data Batal Disimpan")
                    else:
                        print("Harga harus berupa angka positif.")
                except ValueError:
                    print("Input tidak valid. Harga harus berupa angka.")

            case 5:
                break

            case _:
                print("Pilihan tidak valid. Silakan pilih angka 1-5.")

    print("\nData barang setelah diperbarui:")
    tampil_nbarang()

def readbarang():
    while True:
        print("\nMenu Read:")
        print("1. Tampil Data Semua Barang")
        print("2. Tampil Data Berdasarkan Kategori")
        print("3. Kembali ke menu sebelumnya")

        try:
            pilihan = int(input("Masukkan angka menu yang ingin dijalankan: "))
            
            match pilihan:
                case 1:  # Tampil data barang
                    tampil_nbarang()
                case 2:  # tampil data berdasarkan kategori
                    tampil_kategori()
                case 3:  # kembali menu sebelumnya
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih angka 1-3.")
        except ValueError:
            print("Input harus berupa angka.")

def read():
    while True:
        print("\nMenu Read:")
        print("1. Data Barang")
        print("2. Data Customer")
        print("3. Kembali ke menu utama")

        try:
            pilihan = int(input("Masukkan angka menu yang ingin dijalankan: "))
            
            match pilihan:
                case 1:  # Tampil data barang
                    readbarang()
                case 2:  # tampil data customer
                    readcustomer()
                case 3:  # kembali menu utama
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih angka 1-3.")
        except ValueError:
            print("Input harus berupa angka.")


def readcustomer():
    while True:
        print("\nMenu Read:")
        print("1. Tampil Data Semua Customer")
        print("2. Kembali ke menu sebelumnya")

        try:
            pilihan = int(input("Masukkan angka menu yang ingin dijalankan: "))
            
            match pilihan:
                case 1:  # Tampil data barang
                    tampil_ncustomer()
                case 2:  # kembali menu sebelumnya
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih angka 1-2.")
        except ValueError:
            print("Input harus berupa angka.")

def delete_barang():
    tampil_nbarang()
    if not list_alat:
        print("Tidak ada barang yang tersedia.")
        return
    
    while True:
        try:
            index = int(input("\nMasukkan No Index barang yang ingin dihapus: ")) - 1
            if 0 <= index < len(list_alat):
                konfirmasi = input(f"Apakah Anda yakin ingin menghapus {list_alat[index]['nama_alat']}? (Y/N): ").upper()
                if konfirmasi == "Y":
                    list_alat.pop(index)
                    print("Barang berhasil dihapus.")
                    tampil_nbarang()
                else:
                    print("Penghapusan dibatalkan.")
                break
            else:
                print("No Index tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka.")

def sewa_alat():
    tampil_ncustomer()
    try:
        index_customer = int(input("Masukkan nomor index customer: ")) - 1
        if 0 <= index_customer < len(list_customer):
            customer = list_customer[index_customer]
        else:
            print("Nomor index customer tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    tampil_nbarang()
    try:
        index_barang = int(input("Masukkan nomor index barang yang ingin disewa: ")) - 1
        if 0 <= index_barang < len(list_alat):
            barang = list_alat[index_barang]
            if barang["Stock"] <= 0:
                print("Barang ini sedang kosong.")
                return
        else:
            print("Nomor index barang tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return
    
    try:
        durasi = int(input("Masukkan durasi sewa (hari): "))
        if durasi <= 0:
            print("Durasi sewa harus lebih dari 0 hari.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    total_harga = durasi * barang["Harga"]
    print(f"Total biaya sewa: Rp {total_harga:,}")
    konfirmasi = input("Konfirmasi sewa? (Y/N): ").upper()
    if konfirmasi == "Y":
        barang["Stock"] -= 1
        list_sewa.append({
            "No_Sewa": f"S00{len(list_sewa) + 1}",
            "Nama": customer["Nama"],
            "nama_alat": barang["nama_alat"],
            "No_HP": customer["No_HP"],
            "Durasi": f"{durasi} Hari",
            "Total_Harga": f"Rp {total_harga:,}",
            "Status": "Belum Kembali"
        })
        print("Sewa berhasil ditambahkan.")
        tampil_sewa()
    else:
        print("Sewa dibatalkan.")

def update_sewa():
    tampil_sewa()
    if not list_sewa:
        print("Tidak ada data sewa yang tersedia.")
        return

    while True:
        try:
            index = int(input("Masukkan Nomor Index Sewa yang ingin diperbarui: ")) - 1
            if 0 <= index < len(list_sewa):
                break
            else:
                print("Nomor Index tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka.")

    sewa = list_sewa[index]
    print(f"\nNo Sewa: {sewa['No_Sewa']}, Nama: {sewa['Nama']}, Nama Alat: {sewa['nama_alat']}, Durasi: {sewa['Durasi']}, Status: {sewa['Status']}")

    while True:
        print("\nSub-Menu Update Sewa:")
        print("1. Ubah Durasi")
        print("2. Ubah Status")
        print("3. Kembali")

        try:
            pilihan = int(input("Pilih menu yang ingin diperbarui: "))

            match pilihan:
                case 1:
                    try:
                        durasi_baru = int(input(f"Masukkan Durasi Baru (sebelumnya '{sewa['Durasi']}'): "))
                        if durasi_baru > 0:
                            sewa["Durasi"] = f"{durasi_baru} Hari"
                            print("Durasi berhasil diperbarui.")
                            tampil_sewa()
                        else:
                            print("Durasi harus lebih dari 0 hari.")
                    except ValueError:
                        print("Input tidak valid. Durasi harus berupa angka.")

                case 2:
                    print("1. Sudah Kembali")
                    print("2. Belum Kembali")
                    status_baru = int(input(f"Masukkan Status Baru (sebelumnya '{sewa['Status']}'): "))
                    if status_baru == 1:
                        sewa["Status"] = "Sudah Kembali"
                        print("Status berhasil diperbarui.")
                        tampil_sewa()
                    elif status_baru == 2:
                        sewa["Status"] = "Belum Kembali"
                        print("Status berhasil diperbarui.")
                        tampil_sewa()
                    else:
                        print("Status tidak boleh kosong.")

                case 3:
                    break

                case _:
                    print("Pilihan tidak valid. Silakan pilih angka 1-3.")

        except ValueError:
            print("Input harus berupa angka.")

    print("\nData sewa setelah diperbarui:")
    tampil_sewa()

def tampil_sewa():
    if not list_sewa:
        print("Daftar Sewa Kosong.")
    else:
        headers = ["No","No Sewa","Nama Customer", "Nama Alat", "No. HP", "Durasi", "Status"]
        data = [[i, item["No_Sewa"], item["Nama"], item["nama_alat"], item["No_HP"],item["Durasi"], item["Status"]] for i, item in enumerate(list_sewa, start=1)]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

#Function untuk customer
def tampil_ncustomer():
    if not list_customer:
        print("Daftar Customer Kosong.")
    else:
        headers = ["No","ID Customer", "Nama", "No. HP", "Alamat"]
        data = [[i, item["ID_Customer"], item["Nama"], item["No_HP"], item["Alamat"]] for i, item in enumerate(list_customer, start=1)]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def create_customer():
    try:
        print("Daftar Customer")
        tampil_ncustomer()
        
        # Validasi id customer unik
        while True:
            id_customer = input("Masukkan ID Customer: ").upper()
            if any(item["ID_Customer"] == id_customer for item in list_customer):
                print("ID Customer sudah ada. Silakan masukkan kode yang berbeda.")
            else:
                break  # Kode barang valid
        
        nama_customer = input("Masukkan Nama Customer: ").title()
        nohp = input("Masukkan No. HP: ")
        alamat = input("Masukkan Alamat: ").title()

        # Menampilkan data yang akan disimpan
        print("\nData yang dimasukkan:")
        print(f"ID Customer     : {id_customer}")
        print(f"Nama Customer   : {nama_customer}")
        print(f"No.HP           : {nohp}")
        print(f"Alamat          : {alamat}")
        
        # Konfirmasi penyimpanan data
        putusan = input("Simpan data? (Y/N): ").upper()
        if putusan == "Y":
            list_customer.append({
                "ID_Customer": id_customer,
                "Nama": nama_customer,
                "No_HP": nohp,
                "Alamat": alamat
            })
            print(f"\nCustomer berhasil ditambahkan: {nama_customer} (Kode: {id_customer })")
            tampil_ncustomer()
        else:
            print("Data batal disimpan.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def update_customer():
    tampil_ncustomer()  # Tampilkan semua barang sebelum mulai update
    
    if not list_customer:
        print("Tidak ada data customer yang tersedia.")
        return
    
    while True:
        try:
            index = int(input("\nMasukkan No Index barang yang ingin diperbarui: "))
            if 1 <= index <= len(list_customer):  # Pastikan index valid
                index -= 1
                break
            else:
                print("No Index tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka.")

    customer = list_customer[index]  # Ambil barang berdasarkan index yang dipilih
    print(f"\nID Customer: {customer['ID_Customer']}, Nama: {customer['Nama']}, No. HP: {customer['No_HP']}, Alamat: {customer['Alamat']}")

    while True:
        print("\nSub-Menu Update:")
        print("1. Ubah Nama")
        print("2. Ubah No. HP")
        print("3. Ubah Alamat")
        print("4. Kembali")
        
        pilihan = int(input("Pilih menu yang ingin diperbarui: "))
        
        match pilihan:
            case 1:
                nama_baru = input(f"Masukkan Nama Alat Baru (sebelumnya '{customer['Nama']}'): ").title()
                putusan = input("Simpan data? (Y/N): ").upper()
                if nama_baru :
                    if putusan == "Y":
                        customer["Nama"] = nama_baru
                        print("Nama Customer berhasil diperbarui.")
                        tampil_ncustomer()
                    else :
                        print("Data Batal Disimpan")
                else:
                    print("Nama tidak boleh kosong.")

            case 2:
                nohp_baru = input(f"Masukkan Kategori Baru (sebelumnya '{customer['No_HP']}'): ")
                putusan = input("Simpan data? (Y/N): ").upper()
                if nohp_baru :
                    if putusan == "Y":
                        customer["No_HP"] = nohp_baru
                        print("No. HP berhasil diperbarui.")
                        tampil_ncustomer()
                    else :
                        print("Data Batal Disimpan")
                else:
                    print("No. HP tidak boleh kosong.")

            case 3:
                try:
                    alamat_baru = input(f"Masukkan Stock Baru (sebelumnya {customer['Alamat']}): ").title()
                    putusan = input("Simpan data? (Y/N): ").upper()
                    if alamat_baru:
                        if putusan == "Y":
                            customer["Alamat"] = alamat_baru
                            print("Alamat berhasil diperbarui.")
                            tampil_ncustomer()
                        else :
                            print("Data Batal Disimpan")
                except ValueError:
                    print("Input tidak valid. Stock harus berupa angka.")

            case 4:
                break

            case _:
                print("Pilihan tidak valid. Silakan pilih angka 1-4.")

    print("\nData customer setelah diperbarui:")
    tampil_ncustomer()

def delete_customer():
    tampil_ncustomer()
    if not list_customer:
        print("Tidak ada data customer yang tersedia.")
        return
    
    while True:
        try:
            index = int(input("\nMasukkan No Index customer yang ingin dihapus: ")) - 1
            if 0 <= index < len(list_customer):
                konfirmasi = input(f"Apakah Anda yakin ingin menghapus {list_customer[index]['Nama']}? (Y/N): ").upper()
                if konfirmasi == "Y":
                    list_customer.pop(index)
                    print("Customer berhasil dihapus.")
                    tampil_ncustomer()
                else:
                    print("Penghapusan dibatalkan.")
                break
            else:
                print("No Index tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka.")

#Function untuk Main Menu
def create():
    while True:
        print("\nMenu Tambah:")
        print("1. Tambah Data Barang")
        print("2. Tambah Data Customer")
        print("3. Kembali ke menu utama")

        try:
            pilihan = int(input("Masukkan angka menu yang ingin dijalankan: "))
            
            match pilihan:
                case 1:  # tambah data barang
                    create_alat()
                case 2:  # tambah data customer
                    create_customer()
                case 3:  # kembali menu utama
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih angka 1-3.")
        except ValueError:
            print("Input harus berupa angka.")

def update():
    while True:
        print("\nMenu Update:")
        print("1. Update Data Barang")
        print("2. Update Data Customer")
        print("3. Sewa")
        print("4. Update Sewa")
        print("5. Kembali ke menu utama")

        try:
            pilihan = int(input("Masukkan angka menu yang ingin dijalankan: "))
            
            match pilihan:
                case 1:  # update data barang
                    update_barang()
                case 2:  # update data customer
                    update_customer()
                case 3:  # update data customer
                    sewa_alat()
                case 4:  # kembali menu utama
                    update_sewa()
                case 5:  # kembali menu utama
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih angka 1-3.")
        except ValueError:
            print("Input harus berupa angka.")

def delete():
    while True:
        print("\nMenu Delete:")
        print("1. Hapus Data Barang")
        print("2. Hapus Data Customer")
        print("3. Kembali ke menu utama")
        
        try:
            pilihan = int(input("Masukkan angka menu yang ingin dijalankan: "))
            
            match pilihan:
                case 1:
                    delete_barang()
                case 2:
                    delete_customer()
                case 3:
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih angka 1-3.")
        except ValueError:
            print("Input harus berupa angka.")

def main_menu():
    while True:
        print("====================================")
        print(" Manajemen Rental Alat Camping ")
        print("====================================")
        print("\nMenu Utama:")
        print("1. Tampil Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Exit")

        try:
            pilihan = int(input("Masukkan angka menu yang ingin dijalankan: "))

            match pilihan:
                case 1:  # Read
                    read()
                case 2:  # Create
                    create()
                case 3:  # Update
                    update()
                case 4:  # Delete
                    delete()
                case 5:  # exit
                    print("Program selesai.")
                    break
                case _:
                    print("Pilihan tidak valid. Silakan pilih angka 1-5.")
        except ValueError:
            print("Input harus berupa angka.")

main_menu()