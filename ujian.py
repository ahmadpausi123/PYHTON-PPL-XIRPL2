print("kalkulator luas bidang datar")

print("1. segitiga")

print("2. lingkaran")

print("3. persegi panjang")

print("4. jajar genjang")



operasi = input("pilih operasi 1/2/3/4 :")

angka_1 = int(input("masukan angka pertama:"))

angka_2 = int(input("masukan angka kedua:"))



if operasi == "1":

    hasil = 0.5 * angka_1 * angka_2

    print("luas segitiga =", hasil)

elif operasi == "2":

    hasil = 3.14 * angka_1 * angka_2

    print("luas lingkaran =", hasil)

elif operasi == "3":

    hasil = angka_1 * angka_2

    print("luas persegi panjang =", hasil)

elif operasi == "4":

    hasil = angka_1 * angka_2

    print("luas jajar genjang =", hasil)

else :

    print("tidak valid")