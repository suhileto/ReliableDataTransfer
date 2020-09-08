class gonder():
    def rdtgonder(self, veri):
        self.udtgonder(veri)    #veri paketlenmeye gonderiliyor

    def udtgonder(self, veri):
        print("Data paketlendi")
        checksum=0
        for i in range(len(veri)):
            checksum+=1
        p= self.paketle(veri, checksum)
        r= receiver()
        r.rdt_rcv(p)

    def paketle(self, veri, checksum):
        p = []
        for i in range(len(veri)):
            p.append(veri[i])
        p.append(checksum)
        print("Paket hazır: ", p)
        return p

    def isACK(self, ACK):
        print("ACK, paket başarıyla gönderildi.")

    def isNAK(self, NAK):
        print("NAK, paket gönderimi başarısız. Tekrar gönderiliyor...")
        self.rdtgonder(veri)



class receiver():
    def rdt_rcv(self, p):
        if(len(p)==9):
            self.notcorrupt(p)
            self.extract(p)

        else:
            self.corrupt(p)

    def corrupt(self, p):
        NAK=1
        ACK=0
        s= gonder()
        s.isNAK(NAK)

    def notcorrupt(self, p):
        NAK=0
        ACK=1
        s= gonder()
        s.isACK(ACK)

    def extract(self, p):
        veri= []

        for i in range(len(packet)-1):
            veri.append(packet[i])
        packet.clear()
        self.deliver_data(veri)

    def deliver_data(self, veri):
        print("Data alıcıya gonderildi  ",veri)



veri=['1','1','1','0','0','0','1','1']
s= gonder()
s.rdtgonder(veri)