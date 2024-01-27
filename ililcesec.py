from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button


class IlIlceFormu(BoxLayout):
    def __init__(self, **kwargs):
        super(IlIlceFormu, self).__init__(**kwargs)

        # İlleri ve ilçeleri içeren sözlük
        self.iller_ilceler = {
            'İstanbul': ['Beşiktaş', 'Şişli', 'Kadıköy'],
            'Ankara': ['Çankaya', 'Keçiören', 'Mamak'],
            'İzmir': ['Konak', 'Karşıyaka', 'Bornova'],
            'Tekirdağ': ['Merkez', 'Çorlu', 'Süleymanpaşa'],
            'Kırklareli': ['Lüleburgaz', 'Babaeski', 'Kırklareli']
            # İsterseniz daha fazla il/ilçe ekleyebilirsiniz
        }

        # İl seçimi için Spinner (Drop-down) ekleyin
        self.il_spinner = Spinner(text='İl seçin',  background_color=(0, 1, 2, 5), values=list(self.iller_ilceler.keys()))
        self.il_spinner.bind(text=self.il_secildi)

        # İlçe seçimi için Spinner (Drop-down) ekleyin
        self.ilce_spinner = Spinner(text='İlçe seçin',  background_color=(0, 1, 2, 5))

        # Butonlar
        self.temizle_button = Button(text='Temizle', on_press=self.temizle, background_color=(1, 0, 0, 1))
        self.kapat_button = Button(text='Kapat', on_press=self.kapat, background_color=(0, 1, 0, 1))

        # Arayüz öğelerini düzenle
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        self.add_widget(Label(text='İl Seçimi'))
        self.add_widget(self.il_spinner)
        self.add_widget(Label(text='İlçe Seçimi'))
        self.add_widget(self.ilce_spinner)
        self.add_widget(self.temizle_button)
        self.add_widget(self.kapat_button)

    def il_secildi(self, spinner, text):
        # İl seçimi değiştiğinde çağrılır
        if text != 'İl seçin':
            # Seçilen ilin ilçelerini al ve ilce_spinner'a güncelle
            ilceler = self.iller_ilceler[text]
            self.ilce_spinner.values = ilceler
            self.ilce_spinner.text = 'İlçe seçin'

    def temizle(self, instance):
        # Temizle butonuna tıklandığında çağrılır
        self.il_spinner.text = 'İl seçin'
        self.ilce_spinner.text = 'İlçe seçin'

    def kapat(self, instance):
        # Kapat butonuna tıklandığında çağrılır
        App.get_running_app().stop()


class IlIlceApp(App):
    def build(self):
        return IlIlceFormu()


if __name__ == '__main__':
    IlIlceApp().run()
