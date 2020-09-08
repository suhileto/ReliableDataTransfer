class verigonder():
    def rdt_send(self, veri):
        print("veri alındı.")
        self.udtgonder(veri)   #veri paketlenmeye gonderiliyor

    def udtgonder(self, veri):
        print("paket hazırlanıyor")
        p= self.make_pkt(veri)
        r= verial()
        r.rdt_rcv(p)

    def paketle(self, veri):  #veri paketleniyor
        p= []
        for i in range(len(veri)):  #pakete veri ekleniyor
            p.append(veri[i])
        return p



class verial():
    def rdt_rcv(self, p):
        print("gonderildi")
        self.extract(p)

    def extract(self, p):
        veri= []

        for i in range(len(p)):
            data.append(p[i])    #pakete  veri ekleniyor
        p.clear()
        self.deliver_data(veri)

    def deliver_data(self, veri):
        print("Data alıcıya ulaştı: ",veri)



data=['1','1','1','0','0','0','1','1']
s= verigonder()
s.rdt_send(veri)