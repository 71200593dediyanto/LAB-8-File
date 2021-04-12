# Dedi Yanto
# 71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# File
'''
Yuji merupakan mahasiswa yang boros dan sering kelupaan dimana uang dia 
dihabiskan, untuk itu yuji meminta kepada anda untuk dibuatkan program
catatan pengeluaran sederhana yang bisa dipakai yuji untuk mengingat
dimana uang dia dihabiskan, Yuji hanya meminta agar program dapat
mencatat waktu pada hari pengeluaran(tanggal/bulan/tahun), bentuk
pengeluaran,total pengeluaran tersebut dan keseluruhan total 
pengeluaran kedalam notepad. Kemudian program dapat menampilkan 
pengeluaran yang telah dicatatkan sebelumnya di notepad dalam waktu
hari pengeluaran di catatkan.'''

'''
Input:
1. menambahkan
2. menampilkan
3. exit

1.
1. 11/04/2021
2. Sabun mandi
3. 7000
4. tidak

2. 11/04/2021

Proses:
waktu;bentuk pengeluaran;total pengeluaran;total keseluruhan
1. waktu
2. bentuk pengeluaran
dst

buku,spidol,makanan
7000,4000,15000
1.buku      1. 7000
2.spidol    2. 4000
3. makanan  3.15000


Output:
1. tambah data
2. tampilkan data
3. exit

data anda telah ditambahkan

daftar barang   total 
sabun mandi     7000
total keseluruhan 7000

data tidak ditemukan
anda sudah keluar

'''

#Source Code

while True:
    print('1. Tambah Data\n2. Tampilkan Data\n3. Exit')
    pilihan = int(input("Masukkan pilihan yang diinginkan : "))
    if pilihan == 1:
        fiile = open('youtube7coba.txt','a')
        tanggal = input("Masukkan waktu(tanggal/bulan/tahun): ")
        fiile.write(tanggal+";")
        kata1 =''
        kata2 =''
        total = 0
        while True:
            barang =input("\nMasukkan nama barang : ")
            harga = input("Berapa total pengeluaran "+barang+": ")
            kata1 += barang+','
            kata2 += harga+','
            total += int(harga)
            stop = input("\nMasukkan 'stop' untuk berhenti: ").lower()
            if stop == 'stop':
                break
        fiile.write(kata1[:-1]+';'+kata2[:-1]+';'+str(total))
        fiile.write('\n')
        print('Data anda telah dimasukkan\n')
        fiile.close()
    elif pilihan == 2:
        fiile = open('youtube7coba.txt','r')
        waktu = input('Masukkan waktu yang ingin ditampilkan: ')
        counter = 0
        for i in fiile:
            if i.startswith(waktu):
                counter = 1
                pisah = i.split(';')
                print('waktu: ',pisah[0])
                barang = pisah[1].split(',')
                harga = pisah[2].split(',')
                print('Daftar Barang\t Pengeluaran')
                for j in range(len(barang)):
                    if len(barang[j]) > 7:
                        print(barang[j] + '\t   '+ 'Rp.'+ harga[j])
                    else:
                        print(barang[j]+ '\t\t   '+ 'Rp.'+harga[j])
                print('Total Pengeluaran: '+ 'Rp.'+pisah[3],'\n')
        if counter == 0:
            print('Data tidak ditemukan\n')
    elif pilihan == 3:
        print("Anda telah keluar")
        break
    else:
        print("Invalid input\n")