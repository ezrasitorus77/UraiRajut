def urai(inputString): # Membuat fungsi sesuai panduan soal dengan 1 parameter sebagai input user.
    outputString = str() # Variabel ini digunakan sebagai tempat penyimpanan inputString yang sudah dikonversi.
    for char in range(len(inputString)): # Looping sebanyak panjang inputString agar seluruh karakter di dalamnya dapat terambil.
        outputString += inputString[0 : char + 1] # Menambahkan hasil slicing terhadap inputString ke dalam var outputString yang akan ditampilkan. Penambahan 1 angka pada slicing "end" diperlukan karena pada slicing, bagian "end" adalah index untuk berhenti (tidak diambil).
    
    return outputString # Mengembalikan sebagai str namun tanpa fungsi "print" sesuai arahan soal.

print(urai("Purwadhika"))

def rajut(inputString): # Membuat fungsi sesuai panduan soal dengan 1 parameter sebagai input user.
    inputString = list(inputString) # Memecah inputString per karakter dan menjadikannya sebagai list karena ingin dilakukan metode "pop".
    for index in range(len(inputString)): # Loop sebanyak panjang inputString. Namun, panjang ini tidak menjadi proses determinan.
        if index == 0: # Jika index == 0, maka pop hanya dilakukan sebanyak 1 kali. Hal ini dikarenakan huruf pertama pada inputString pasti sama dengan huruf keduanya.
            inputString.pop(index) # Metode pop bersifat "inplace", jadi tidak perlu dinyatakan sebagai var kembali.
        # Sebenarnya, bisa juga blok kode di bawah dimasukkan ke dalam klausul "else" dan hanya menambahkan klausul "index != 1" di dalamnya. Namun, proses dirasa lebih efisien jika blok kode selanjutnya berada pada urutan pemrosesan yang sama (indent).
        if (index != 1) and (index != 0): # Jika index tidak sama dengan 0 dan 1, maka "pop" terhadap index yang sama diulang sebanyak jumlah index tersebut. Index 1 tidak disertakan karena index 1 sudah pasti berisi huruf yang ingin diambil.
            for loop in range(index): # Loop sebanyak index
                try: # Digunakan untuk terus berproses sampai error terjadi.
                    inputString.pop(index) # Menghilangkan karakter index tertentu yang terus berubah posisinya ("inplace").
                except: # Error sengaja dicari karena bila index yang ingin di-"pop" sudah melewati batas, maka saat itu adalah dimana inputString sudah terkonversi penuh.
                    return "".join(inputString) # Karena masih berbentuk list, maka harus di-"join" agar menjadi str. Fungsi "print" tidak digunakan disini sesuai arahan soal.

print(rajut("PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"))