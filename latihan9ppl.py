# Beberapa yang biasa digunakan untuk ngoding



# Magic method init (konstruktor) berfungsi untuk mendahulukan giliran satu sekali jalan codingnya atau looping

class halodunia:

    def __init__(self):

        print('Hello World')



# Membuat instansiasi

# a = halodunia()





# Magic method str, berfungsi menampilkan string saat ketika dijadikan parameter

class segitiga:

    def __init__(self, a, t):

        self.a = a

        self.t = t



    def __str__(self):

        luas = 0.5 * self.a * self.t

        return f'segitiga (alas = {self.a}) (tinggi = {self.t}) (luas = {luas})'



# Membuat instansiasi

# a = segitiga(10, 10)

# print(a)



# Magic method len, len berfungsi untuk menghitung panjang dari objek yang kita buat



# class siswa

class siswa:

    def __init__(self):

        self.__list_siswa = []

    def tambah_siswa(self, siswa):

        self.__list_siswa.append(siswa)

    def __len__(self):

        return len(self.__list_siswa)



# membuat instansiasi

grup1 = siswa()

grup1.tambah_siswa('Putra')

grup1.tambah_siswa('Putri')

grup1.tambah_siswa('Bagas')

grup1.tambah_siswa('Bagus')



print(len(grup1))

# ['Putra', 'Putri']