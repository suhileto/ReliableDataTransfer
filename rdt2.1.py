class gonder():
    deger=0
    def rdt_send(self, veri):  #veriyi alıyoruz
        self.udtgonder(veri)  #veriyi paketlemeye gonderiyoruz

    def udtgonder(self, veri):
        checksum=0                     #datanın boyutunu hesaplıyoruz
        for i in range(len(veri)):
            checksum+=1
        p=self.make_pkt(veri, checksum)
        r= receiver()
        r.rdt_rcv(p, self.deger)

    def make_pkt(self, veri, checksum):
        p= []
        for i in range(len(veri)):
            p.append(veri[i])    # veri pakete ekleniyor
        p.append(checksum)
        print("Paket hazır: ", p)
        return p

    def isACK(self, ACK, deger):
        print("ACK, paket gönderimi başarılı.")
        self.deger+=1  #bir sonraki datayı paketlemek icin
        if(deger==1):
            self.deger=0
            self.rdt_send(veri)

    def isNAK(self, NAK, deger):
        print("NAK, ",deger,". paket gönderimi başarısız. Tekrar gönderiliyor...")
        self.rdt_send(veri)



class receiver():
    def rdt_rcv(self, p, deger):
        if (len(p) == 9):  # uzunlugu konrol ediyor
            self.notcorrupt(p, deger)

        else:
            self.corrupt(p, deger)

    def corrupt(self, p, deger):
        NAK=1
        ACK=0
        s= sender()
        s.isNAK(NAK, deger)

    def notcorrupt(self, p, deger):
        NAK=0
        ACK=1
        s= gonder()
        s.isACK(ACK, deger)
        self.has_seq(p, deger)

    def has_seq(self, p, deger):
        if(deger==1):
            print(deger,". paket alındı.")

        elif(deger==0):
            print(deger,". paket alındı.")

        self.extract(p)

    def extract(self, p):
        veri= []

        for i in range(len(p)-1):
            veri.append(p[i])
        p.clear()
        print("Data ayıklandı, paket temizlendi.")
        self.deliver_data(veri)

    def deliver_data(self, veri):
        print("Data alıcıya ulaştı: ",veri)



veri=['1','1','1','0','0','0','1','1']
s= gonder()
s.rdtgonder(veri)