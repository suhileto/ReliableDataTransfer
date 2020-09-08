class gonder():
    deger=0
    def rdt_send(self, veri):   #veriyi alıyoruz
        self.udt_send(veri)    #veriyi paketlemeye gonderiyoruz

    def udt_send(self, veri):
        print("Data paketlere çevriliyor...")
        checksum=0
        for i in range(len(veri)):
            checksum+=1
        packet=self.make_pkt(veri, checksum)
        r= receiver()
        r.rdt_rcv(packet, self.deger)

    def make_pkt(self, veri, checksum):
        packet= []
        for i in range(len(veri)):
            packet.append(veri[i])  # veri pakete ekleniyor
        packet.append(checksum)
        print("Paket hazır: ", packet)
        return packet

    def isACK(self, ACK, deger): #sadece ACK kontrol edildi
        if(ACK==1):
            print("ACK")
            self.deger+=1 #bir sonraki data paketlenmek için
            if(deger==1):
                self.deger=0
                self.rdt_send(veri)

        elif(ACK==0):
            print("ACK 0, ",deger,". paket gönderimi başarısız. Tekrar gönderiliyor...")
            self.rdt_send(veri)



class receiver():
    def rdt_rcv(self, packet, deger):
        if (len(packet) == 9):  # uzunluk kontrolu checksum ile 9
            self.notcorrupt(packet, deger)

        else:
            self.corrupt(packet, deger)

    def corrupt(self, packet, deger):
        ACK=0
        s= gonder()
        s.isACK(ACK, deger)

    def notcorrupt(self, packet, deger):
        ACK=1
        s= gonder()
        s.isACK(ACK, deger)
        self.has_seq(packet, deger)

    def has_seq(self, packet, deger):
        if(deger==1):
            print(deger,". paket alındı.")

        else:
            print(deger,". paket alındı.")

        self.extract(packet)

    def extract(self, packet):
        veri= []

        for i in range(len(packet)-1):
            veri.append(packet[i])
        packet.clear()
        print("Data ayıklandı, paket temizlendi.")
        self.deliver_data(veri)

    def deliver_data(self, veri):
        print("Data alıcıya ulaştı: ",veri)



veri=['1','1','1','0','0','0','1','1']
s= gonder()
s.rdt_send(veri)