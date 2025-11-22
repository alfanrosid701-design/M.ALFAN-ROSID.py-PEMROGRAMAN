# program penentuan nilai tempat bilangan M.Alfan Rosid

# meminta input dari pengguna
angka = input ("Masukkan bilangan: ")

("--------------------------------------")
print(f"Anda memasukkan bilangan {angka} dimana: ")
("----------------------------------------")

# nama posisi nilai tempat dari satuan sampai juta
tempat = ["satuan", "puluhan", "ratusan", "ribuan",
          "puluh ribuan", "ratus ribuan", "juta"]

# menghitung panjang digit angka
panjang = len(angka)

# menampilkan setiap digit beserta nilai tempatnya
for i in range(panjang):
    digit = angka[i]                  
    posisi = tempat [panjang - 1 - i]  

    print(f"{digit} merupakan {posisi}")
