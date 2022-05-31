import datetime
import os

class LMS:
    def __init__(self, list_buku, nama_perpustakaan):
        self.list_buku = "list_buku.txt"
        self.nama_perpustakaan = nama_perpustakaan
        self.kamus_buku = {}
        id = 101
        with open(self.list_buku) as bk:
            content = bk.readlines()
        for line in content:
            self.kamus_buku.update({
                str(id): {
                    'judul_buku': line.replace('\n', ''), "nama_petugas": '', 'tanggal_rilis': '', 'status': 'Tersedia'
                }
            })
            id += 1

    def tampilkan_buku(self):
        print('-----------------List Buku------------------\n')
        print("ID Buku \t", "Judul")
        print('--------------------------------------------')
        for key, value in self.kamus_buku.items():
            print(key, '\t\t', value.get('judul_buku'),
                  '- [', value.get("status"), ']')

    def issue_buku(self):
        id_buku = input('Masukkan ID Buku : ')
        tanggal_sekarang = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if id_buku in self.kamus_buku.keys():
            if not self.kamus_buku[id_buku]['status'] == 'Tersedia':
                print(f"Buku ini sudah dikeluarkan dari {self.kamus_buku[id_buku]['nama_petugas']} pada saat {self.kamus_buku[id_buku]['tanggal_rilis']}")
                return self.issue_buku()
            elif self.kamus_buku[id_buku]['status'] == 'Tersedia':
                nama_kamu = input("Masukkan Nama Kamu : ")
                self.kamus_buku[id_buku]['nama_petugas'] = nama_kamu
                self.kamus_buku[id_buku]['tanggal_rilis'] = tanggal_sekarang
                self.kamus_buku[id_buku]['status'] = 'Sudah dikeluarkan'
                print("Buku berhasil dikeluarkan!!! \n")
            else:
                print("ID Buku tidak ditemukan")
                return self.issue_buku()

    def tambah_buku(self):
        buku_baru = input("Masukkan Judul Buku : ")
        if buku_baru == "":
            return self.tambah_buku()
        elif len(buku_baru) > 25:
            print("Judul Buku Terlalu Panjang, Judul harus kurang dari 25 karakter")
            return self.tambah_buku()
        else:
            with open(self.list_buku, 'a') as bk:
                bk.writelines(f'{buku_baru}\n')
                self.kamus_buku.update({str(int(max(self.kamus_buku)) + 1): {
                    'judul_buku': buku_baru,
                    'nama_petugas': '',
                    'tanggal_rilis': '',
                    'status': 'Tersedia'
                }})

                print(f'Buku "{buku_baru}" telah berhasil ditambahkan')

    def kembalikan_buku(self):
        id_buku = input("Masukkan ID Buku : ")
        if id_buku in self.kamus_buku.keys():
            if self.kamus_buku[id_buku]['status'] == 'Tersedia':
                print("Buku ini sudah ada di perpustakaan")
                print("Silahkan cek kembali id buku anda")
                return self.kembalikan_buku()
            elif not self.kamus_buku[id_buku]['status'] == "Tersedia":
                self.kamus_buku[id_buku]['nama_petugas'] = ''
                self.kamus_buku[id_buku]['tanggal_rilis'] = ''
                self.kamus_buku[id_buku]['status'] = 'Tersedia'
                print("Buku berhasil dikembalikan")
            else:
                print('ID Buku Tidak Ditemukan')


try:
    myLMS = LMS("list_buku.txt", "Perpustakaan Mas Tio")
    press_key_list = {"A": "Menampilkan Buku", "I": 'Issue Buku',
                      "T": "Tambah Buku", "R": "Kembalikan Buku", "Q": "Keluar"}
    key_press = False
    while not (key_press == 'q'):
        print(f"\n--------------Selamat Datang di {myLMS.nama_perpustakaan}--------------\n")
        for key, value in press_key_list.items():
            print("Ketik", key, 'untuk', value)
        key_press = input("Masukkan Kode : ").lower()
        if key_press == 'i':
            print("\n Sekarang berada di menu Issue Buku\n")
            myLMS.issue_buku()
        elif key_press == "t":
            print("\nSekarang berada di menu Tambah Buku\n")
            myLMS.tambah_buku()
        elif key_press == 'r':
            print("\nSekarang berada di menu Kembalikan Buku\n")
            myLMS.kembalikan_buku()
        elif key_press == 'a':
            print("\nSekarang berada di menu Tampilkan Buku\n")
            myLMS.tampilkan_buku()
        elif key_press == 'q':
            break
        else:
            print("Kode Salah! Masukkan Ulang Kode Anda.")
            continue
except Exception as e:
    print("Ada yang salah. Silahkan periksa kembali input anda!")

