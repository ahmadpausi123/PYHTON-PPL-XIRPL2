# Nama: Pausi :3



class Agama:

    def __init__(self, nama, agama):

        self.nama = nama

        self.agama = agama



    def perkenalan(self):

        print(self.nama, "Beragama", self.agama)



class Dava(Agama):

    def __init__(self, nama, agama, sholat):

        Agama.__init__(self, nama, agama)

        self.sholat = sholat



class BongCin(Agama):

    def __init__(self, nama, agama, sembahyang):

        Agama.__init__(self, nama, agama)

        self.sembahyang = sembahyang



dava = Dava('Dava','Islam','Sholat')

dava.perkenalan()

print("Saya beribadah dengan melakukan", dava.sholat, "\n")



bongCin = BongCin('Bong Cin','Buddha','Sembahyang')

bongCin.perkenalan()

print("Saya beribadah dengan melakukan", bongCin.sembahyang, "\n")