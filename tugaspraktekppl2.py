class angka:

    def __init__(self, angka):

        self.angka = angka

    def __add__(self, objek):

        return angka(

            self.angka + objek.angka

        )



satu = angka(int(input("masukan angka Pertama: ")))

dua = angka(int(input("masukan angka Kedua: ")))

hasil = satu + dua

print('Hasil dari', satu.angka, '+', dua.angka, 'adalah', hasil.angka)