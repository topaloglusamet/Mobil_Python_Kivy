from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class PopUpPencere(Popup):
    def __init__(self, ana_pencere, **kwargs):
        super(PopUpPencere, self).__init__(**kwargs)
        self.title = "Başlık"
        self.content = BoxLayout(orientation='vertical', spacing=10)
        self.label = Label(text="Popup Açıklaması")
        self.text_input = TextInput(hint_text='Adınızı girin', multiline=False)
        self.button = Button(text='Tamam', on_press=lambda x: self.olayDugme(ana_pencere))

        self.content.add_widget(self.label)
        self.content.add_widget(self.text_input)
        self.content.add_widget(self.button)

    def olayDugme(self, ana_pencere):
        ad = self.text_input.text
        ana_pencere.ana_pencere_etiket.text = "Merhaba %s!" % ad
        self.dismiss()


class AnaPencere(BoxLayout):
    def __init__(self, **kwargs):
        super(AnaPencere, self).__init__(**kwargs)
        self.ana_pencere_etiket = Label(text="Merhaba Kivy!")
        self.buton = Button(text="Popup Aç", on_press=self.popAc)
        self.add_widget(self.ana_pencere_etiket)
        self.add_widget(self.buton)

    def popAc(self, instance):
        self.popup = PopUpPencere(self)
        self.popup.open()


class PopUpAcApp(App):
    def build(self):
        return AnaPencere()


if __name__ == '__main__':
    PopUpAcApp().run()
