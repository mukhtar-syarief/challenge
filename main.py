hurufs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
angkas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

alldictionary = hurufs + angkas

rahasia = 'rahasia.txt'
keluaran = 'keluaran.txt'
pindah = 130

def deskripsi(konten):
    hasil = []
    for char in konten:
        try:
            index = alldictionary.index(char)
        except ValueError as e:
            hasil.append(char)
            continue
        new_index = index - pindah
        real_index = new_index % len(alldictionary)

        real_char = alldictionary[real_index]
        hasil.append(real_char)
        
    return ''.join(hasil)

# buka data rahasia dari txt
with open (rahasia, 'r') as f:
    konten = f.read()

# melakukan enkripsi
datarahasia = deskripsi(konten)

# simpan data rahasia ke file
with open(keluaran, 'w') as f:
    f.write(datarahasia)

print('data rahasia telah disimpan di {}'.format(keluaran))
