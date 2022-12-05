# Kelas induk = kendaraan, kelas turunan = mobil

# Kendaraan mempunyai sifat berjalan(), Mobil mempunyai sifat berjalan() tapi lebih spesifik



class kendaraan:

    def berjalan(self):

        print('Berjalan')



class mobil(kendaraan):

    def berjalan(self, kecepatan, satuan = 'km/j'):

        print(f'Berjalan lebih ngebut {kecepatan} {satuan}')



# instansiasi (memanggil fungsi dan kelas)

sepeda = kendaraan()

sedan = mobil()



sepeda.berjalan()

sedan.berjalan(10)