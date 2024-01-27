

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import os,sys


class farkliKaydetForm(Popup):
    pass
class dosyaAcForm(Popup):
    pass
class dosyaKaydedilmedi(Popup):
    pass
class yeniDosyaForm(Popup):
    pass
class metinDuzenleyici(App):
    def farkliKaydetPencere(self):
        f1=farkliKaydetForm()
        f1.open()
    def farkliKaydetSec(self,form):
        secilenDosya=form.ids.dosya_secim.selection
        if secilenDosya:
            if len(secilenDosya)>0:
                dosyaAdi=os.path.split(secilenDosya[0])[1]
                form.ids.dosya_adi.text=dosyaAdi
    def kaydetBtn(self,form):
        self.son_yol=form.ids.dosya_secim.path
        self.son_dosya=form.ids.dosya_adi.text
        self.dosyaKaydet()
    def BildirimGoster(self,turu,hata):
        icerik=Label(text=hata,markup=True)
        hataPen=Popup(title=turu,content=icerik)
        hataPen.size_hint=(.7,.7)
        icerik.bind(on_touch_down=hataPen.dismiss)
        hataPen.open()
    def dosyaKaydet(self):
        if not self.son_dosya:
            self.BildirimGoster("Hata!","dosya adi yazmalısınız!")
        else:
            try:
                dosyaTamAd=os.path.join(self.son_yol,self.son_dosya)
                dosya=open(dosyaTamAd,"w")
                dosya.write(self.root.ids.metin.text)
                self.metin_degisti=False
                dosya.close()
                self.BildirimGoster("yapıldı","Dosya kaydedildi")
            except:
                self.BildirimGoster("Hata!","Dosya Yazılamadı")
    def dosyaKaydetBtn(self):
        if self.son_dosya:
            self.dosyaKaydet()
        else:
            self.farkliKaydetPencere()
    def degisti(self,nesne,deger):
        if self.ilkAcilis:
            self.ilkAcilis=False
        else:
            self.metin_degisti=True
    def dosyaKaydedilmediKaydet(self,ana):
        if self.son_dosya:
            self.dosyaKaydet()
            ana.dismiss()
            self.dosyaAcPencere()
        else:
            self.BildirimGoster("uyarı","dosya hiç kaydedilmemiş. farklı kaydet ")
            #self.farkliKaydetPencere()
            #ana.dismiss()

    def dosyaAcBtn(self):
        if self.metin_degisti :
            dosyaKaydedilmediForm=self.dosyaKaydedilmediKaydet(self)
            dosyaKaydedilmediForm.open()
            #self.BildirimGoster("Uyarı","Dosya kaydedilmedi. Önce kaydedin!")
        else:
            self.dosyaAcPencere()
    def dosyaAcPencere(self):
        form=dosyaAcForm()
        form.open()
    def dosyaOku(self,dosya_secim):
        if dosya_secim.selection:
            if len(dosya_secim.selection)>0:
                (self.son_yol,self.son_dosya)=dosya_secim.selection[0].split(dosya_secim.selection[0])
                try:
                    self.root.ids.metin.text=open(dosya_secim.selection[0]).read()
                    self.metin_degisti=True
                    #self.root.ids.metin.cursor=self.root.metin.get_cursor_from_index(0)
                except:
                    self.BildirimGoster("hata","dosya açılamadı:") #%str(sys.exc_info().__str__()[1][1]))
            else:
                self.BildirimGoster("uyarı:","dosya seçmelisiniz!!")
    def yeniDosyaAc(self):
        self.root.ids.metin.text=""
        self.son_dosya=""
    def build(self):
        self.son_yol=os.getcwd()
        self.son_dosya=""
        self.metin_degisti=False
        self.root.ids.metin.bind(on_change=self.degisti)
        self.ilkAcilis=True

uyg=metinDuzenleyici()
uyg.run()