# Contoh overloading

# Mendefinisikan atau mengfungsikan operator sesuai kemauan kita (+)



# integer = 10 + 30

# print(integer)



# string = "Fauzi" + "bukan" + "Wibu"

# print(string)



# campur = "Fauzi" + "umur" + 20

# print(campur)



# Membuat class angka

class angka:

    def __init__(self, angka):

        self.angka = angka

    def __add__(self, objek):

        return angka(

            self.angka + objek.angka

        )



# Membuat objek

x1 = angka(10)

x2 = angka(20)

x3 = x1 + x2

print(x3.angka)