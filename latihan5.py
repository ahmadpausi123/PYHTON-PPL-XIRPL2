# Belajar Pewarisan (inheritance)

# 3 Objek = Orang, Pelajar, Pekerja

# masing-masing mempunyai nama, asal , kemampuan untuk introduce self

# Pelajar di sekolah, Pekerja di kantor



class Orang:

    def __init__(self, nama, asal):

        self.nama = nama

        self.asal = asal # print("fungsi init dieksekusi")



    def perkenalan(self):

        print("Perkenalkan nama saya", self.nama, "dari", self.asal)



class Pelajar(Orang):

    # Sekolahnya dimana

    def __init__(self, nama, asal, sekolah):

        Orang.__init__(self, nama, asal) # self.nama = nama <br> self.asal = asal // cara tidak singkat

        self.sekolah = sekolah



class Pekerja(Orang):

    # kerjanya dimana

    def __init__(self, nama, asal, kerja):

        Orang.__init__(self, nama, asal)

        self.kerja = kerja



dani = Orang('Dani', 'Zimbabwe\n')

dani.perkenalan()



rahma = Pelajar('rahma','jawa','SMK JP 1')

rahma.perkenalan()

print("Saya Bersekolah di", rahma.sekolah, "\n")



arya = Pekerja('arya','pakistan','SMK JP 1')

arya.perkenalan()

print("Saya Bekerja di", arya.kerja, "\n")