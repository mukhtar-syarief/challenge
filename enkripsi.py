"""
Enkripsi adalah proses teknis yang mengonversikan informasi menjadi kode rahasia, sehingga mengaburkan data yang Anda kirim, terima, atau simpan.
Sebaliknya Deskripsi adalah proses teknis yang mengubah kode rahasia menjadi informasi yang dapat dibaca.

https://en.wikipedia.org/wiki/Encryption

data soal ada di rahasia.txt yang telah di enkripsi. silahkan lakukan deskripsi terhadap data tersebut.

"""

filename = 'example.txt'
output = 'output.txt'
pindah = 130

hurufs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
angkas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

alldictionary = hurufs + angkas

def enkripsi(konten):
    hasil = []
    for charactr in konten:
        try:
            index = alldictionary.index(charactr)
        except ValueError as e:
            hasil.append(charactr)
            continue

        newindex = index + pindah
        rahasiaindex = newindex % len(alldictionary)

        newchar = alldictionary[rahasiaindex]
        hasil.append(newchar)

    return ''.join(hasil)

# buka data asli dari txt
with open (filename, 'r') as f:
    konten = f.read()

# melakukan enkripsi
datarahasia = enkripsi(konten)

# simpan data rahasia ke file
with open(output, 'w') as f:
    f.write(datarahasia)

print('data rahasia telah disimpan di {}'.format(output))


