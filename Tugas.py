list_barang = {}

def add_item():
    nama = input('Masukkan Nama Barang: ')
    if nama in list_barang:
        list_barang[nama] += 1
        print(f'Barang {nama} telah ditambahkan')
        return

    stok = int(input('Masukkan Jumlah Barang: '))
    list_barang[nama] = stok
    print(f'Barang : "{nama}" telah ditambahkan\nstok: {stok}')

def search():
    lihat = input('Cari Barang: ')
    if lihat in list_barang:
        print(f'Barang {lihat} ada dalam list\nstok: {list_barang[lihat]}')
    else:
        print(f'Barang {lihat} tidak tersedia')

def delete():
    Hapus = input('Hapus Barang: ')
    if Hapus in list_barang:
        del list_barang[Hapus]
        print(f'Barang {Hapus} telah dihapus')
    else:
        print(f'Barang {Hapus} tidak tersedia')

def edit():
    nama = input('Masukkan barang yang ingin diubah: ')
    if nama in list_barang:
        stok = int(input('Masukkan jumlah barang: '))
        list_barang[nama] = stok
        print(f'Barang {nama} telah diubah')
    else:
        print(f'Barang {nama} tidak tersedia')

def view_data():
    print(f"{list_barang}")

def view_item_count():
    if not list_barang:
        print('Tidak ada data')
        return
    print(f"Jumlah Data Barang Saat Ini :{len(list_barang)}")