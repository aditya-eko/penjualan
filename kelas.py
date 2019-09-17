class Penjualan:
    pass


    def __init__(self,inputnama,inputharga,inputpajak):
        self.nama=inputnama
        self.harga=inputharga
        self.pajak=inputpajak



    def jual(self,x):
        total=x*self.harga
        return "total yang harus di bayar untuk pembelian {2} sebanyak {1} unit adalah{0}".format(total,x,self.nama)

    def diskon(self):
        self.diskon=10
        y=self.harga*self.diskon//100
        return self.harga-y

    def bonus(self):
        self.bonus="tas"
        print("setiap pembeian ",self.nama + " mendapatkan " + self.bonus)

dell=Penjualan("dell",7000000,5)

print(dell.__dict__)
print(dell.jual(4))
print(dell.diskon())
dell.bonus()