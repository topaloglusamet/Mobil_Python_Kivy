
"""merhabadunya
from kivy.app import App
from kivy.uix.label import Label
class ilkUygulama(App):
    def build(self):
        self.title = 'Benim Kivy Programım'
        return Label(text='Merhaba Dünya!')
ilkUygulama().run()
"""


"""login register 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class odev(App):

    def build(self):
        duzen = GridLayout(cols=2)

        duzen.add_widget(Label(text='Kullanıcı Adı:'))
        kullanici_adi = TextInput()
        duzen.add_widget(kullanici_adi)

        duzen.add_widget(Label(text='Parola:'))
        parola = TextInput()
        duzen.add_widget(parola)

        duzen.add_widget(Widget())
        gir_dugme = Button(text='Gir')
        duzen.add_widget(gir_dugme)


        self.title = "Giris Formu"
        return  duzen
odev().run()
"""




"""tıkla ve değiştir
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class OdevApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Etiket (Label) oluştur
        self.etiket = Label(text='Merhaba, tıkla ve değiştir!')

        # Düğme (Button) oluştur
        dugme = Button(text='Tıkla', on_press=self.metni_degistir)

        # Widget'ları düzenleme
        layout.add_widget(self.etiket)
        layout.add_widget(dugme)

        return layout

    def metni_degistir(self, instance):
        self.etiket.text = 'Tıkladın ve değiştirdim.'

if __name__ == '__main__':
    OdevApp().run()
"""



""" popap penceresi aç
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

class olayUyg(App):
    def popAc(self, nesne):
        icerik = Label(text= "iste bir popup")

        popup = Popup(title='Popup Pencere Basligi',
                  content=icerik,
                  size_hint=(None, None), size=(500, 500))

        icerik.bind(on_touch_down=popup.dismiss)
        popup.open()
    def build(self):
        return Button(text="Popup için tıkla", on_press=self.popAc)

olayUyg().run()
"""





