from threading import Event

exit = Event()


class gonder():
    def rdt_send(self, veri):   #veriyi alıyoruz
        global deger
        deger=0
        self.udt_send(veri)   #veriyi paketlemeye gonderiyoruz

    def udt_send(self, veri):
        print("Data paketlendi")
        checksum=0
        for i in range(len(veri)):
            checksum+=1
        p=self.make_pkt(veri, checksum)
        r= receiver()
        r.rdt_rcv(p, deger)
        self.start_timer()

    def make_pkt(self, veri, checksum):
        p= []
        for i in range(len(veri)):    # veri pakete ekleniyor
            p.append(veri[i])
        p.append(checksum)
        print("Paket hazır: ", p)
        return p

    def isACK(self, ACK, deger):
        if(ACK==1):
            print("ACK")
            deger+=1 #bir sonraki dataya geçtik
            self.rdt_send(veri)

        elif(ACK==0):
            print("ACK 0, ",deger,". paket gönderimi başarısız. Tekrar gönderiliyor...")
            self.rdt_send(veri)

    def start_timer(self):
        while not exit.is_set():
            exit.wait(60)
        self.isACK(ACK, deger)

    def stop_timer(self):
        exit.set() #süreyi durduruyor



class receiver():
    def rdt_rcv(self, p, deger):
        if (len(p) == 9):
            self.notcorrupt(p, deger)

        else:
            self.corrupt(p, deger)

    def corrupt(self, p, deger):
        global ACK
        ACK=0
        s= gonder()
        s.isACK(ACK, deger)

    def notcorrupt(self, p, deger):
        global ACK
        ACK=1
        s= gonder()
        s.isACK(ACK, deger)
        s.stop_timer()
        self.has_seq(p, deger)

    def has_seq(self, p, deger):
        if(deger==0):
            print(deger,". paket alındı.")

        elif(deger==1):
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
s.rdt_send(veri)
