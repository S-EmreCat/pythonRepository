class Card:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger
        
    def __repr__(self):
        return f'{self.tip} {self.deger}'
        

class Deste:
    
    def __init__(self):
        kartTipleri = ["karo","sinek","kupa","maça"]
        kartDegerleri = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.kartlar = [] 
        for i in kartTipleri:
            for j in kartDegerleri:
                self.kartlar.append(Card(i , j))

    def getDeste(self):
        print(self.kartlar)
       
    def kartSayisi(self):
        print (len(self.kartlar) ) 
    
    def KartlariKaristir(self):
        import random
        random.shuffle(self.kartlar)

    def kartDagit(self,sayi):
        del self.kartlar[len(self.kartlar)-6:len(self.kartlar)]
        print(f"kart dağıtıldı: {self.kartlar[len(self.kartlar)-6:len(self.kartlar)]}")
        
    
    def kartAt(self):
        # self.kartlar.pop(len(self.kartlar)-1)
        print(f'card: {self.kartlar.pop(len(self.kartlar)-1)}')
        pass
    
deste1 = Deste()
deste1.KartlariKaristir()
deste1.getDeste()
deste1.kartSayisi()
deste1.kartAt()

deste1.kartSayisi()
deste1.getDeste()

deste1.kartDagit(6)
deste1.kartSayisi()
deste1.getDeste()



        



