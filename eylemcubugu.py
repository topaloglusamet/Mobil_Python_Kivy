from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionPrevious
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class EylemCubugu(App):

    def build(self):
        eylem_cubugu = ActionBar(pos_hint={'top': 1})
        eylem_gorunumu = ActionView()
        eylem_cubugu.add_widget(eylem_gorunumu)



        # ActionPrevious nesnesini oluştururken app_icon özelliğini ekleyin
        onceki_eylem = ActionPrevious(title='Eylem Çubuğu', app_icon='samo.jfif',
                                      with_previous=True)
        eylem_gorunumu.add_widget(onceki_eylem)



        duzen = BoxLayout(orientation='vertical')
        duzen.add_widget(eylem_cubugu)

        # Metin girişi için TextInput öğesi
        self.metin_girisi = TextInput(multiline=True)
        duzen.add_widget(self.metin_girisi)

        # Butonlar için yatay bir düzen
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Silme butonu
        silme_butonu = Button(text='Sil', on_press=self.sil)
        button_layout.add_widget(silme_butonu)

        # Kaydetme butonu
        kaydetme_butonu = Button(text='Kaydet', on_press=self.kaydet)
        button_layout.add_widget(kaydetme_butonu)

        # Güncelleme butonu
        guncelleme_butonu = Button(text='Güncelle', on_press=self.guncelle)
        button_layout.add_widget(guncelleme_butonu)

        duzen.add_widget(button_layout)

        return duzen

    def sil(self, instance):
        self.metin_girisi.text = ''
        print("Metin silindi:", self.metin_girisi.text)

    def kaydet(self, instance):
        # Metni bir dosyaya kaydetme işlemleri buraya eklenir
        print("Metin kaydedildi:", self.metin_girisi.text)

    def guncelle(self, instance):
        # Metni güncelleme işlemleri buraya eklenir
        print("Metin güncellendi:", self.metin_girisi.text)


EylemCubugu().run()
