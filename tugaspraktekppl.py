# Pausi



class angka:

    def __init__(self, satu, dua):

        self.satu = satu

        self.dua = dua

    def __str__(self):

        hasil = self.satu + self.dua

        return f'Hasil dari {self.satu} + {self.dua} adalah : {hasil}'



hasil = angka(int(input("masukan angka Pertama: ")), int(input("masukan angka Kedua: ")))

print(hasil)