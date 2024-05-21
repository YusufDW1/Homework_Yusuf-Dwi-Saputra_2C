import Tugas as Modul

print(f'{5*"<"}Selamat Datang Di Program Manajemen Stok Barang{5*">"}')
print("Masukkan Pilihan")
print("1. Tambah Data Barang")
print("2. Cari Barang")
print("3. Hapus Data Barang")
print("4. Edit Barang")
print("5. Tampilkan Data Barang")
print("6. Tampilkan Jumlah Data")
print("7. Keluar")

while True:
    pilihan = int(input('Masukkan Pilihan: '))
    if pilihan == 1:
        Modul.add_item()
    elif pilihan == 2:
        Modul.search()
    elif pilihan == 3:
        Modul.delete()
    elif pilihan == 4:
        Modul.edit()
    elif pilihan == 5:
        print(f"{5*'*'}Toko Elektronik{5*'*'}")
        Modul.view_data()
    elif pilihan == 6:
        Modul.view_item_count()
    elif pilihan == 7:
        print("Terima Kasih Telah Menggunakan Program Kami")
        break