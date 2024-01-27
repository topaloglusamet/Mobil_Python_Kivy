
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import os

class NotDefteri(BoxLayout):
    def kaydet(self):
        dosya_yolu = 'not_defteri.txt'
        with open(dosya_yolu, 'w', encoding='utf-8') as dosya:
            dosya.write(self.ids.metin_alani.text)
        self.bilgi_penceresi(f"{dosya_yolu} adlı dosya kaydedildi.")

    def sil_metin(self):
        dosya_yolu = 'not_defteri.txt'

        try:
            os.remove(dosya_yolu)
            self.bilgi_penceresi(f"{dosya_yolu} adlı dosya silindi.")
        except FileNotFoundError:
            self.bilgi_penceresi(f"{dosya_yolu} adlı dosya bulunamadı.")
        except Exception as e:
            self.bilgi_penceresi(f"Hata oluştu: {str(e)}")

        self.ids.metin_alani.text = ''  # Metin alanını temizle

    def bilgi_penceresi(self, mesaj):
        popup = Popup(title='Bilgi', content=Label(text=mesaj), size_hint=(None, None), size=(600, 200))
        popup.open()

    def kaydet_masaustune(self):
        masaustu_yolu = os.path.join(os.path.expanduser('~'), 'Desktop')
        dosya_adı = 'not_defteri.txt'
        dosya_yolu = os.path.join(masaustu_yolu, dosya_adı)

        with open(dosya_yolu, 'w', encoding='utf-8') as dosya:
            dosya.write(self.ids.metin_alani.text)
        self.bilgi_penceresi(f"{dosya_adı} adlı dosya masaüstüne kaydedildi.")


class gunluk(App):
    def build(self):
        return NotDefteri()


if __name__ == '__main__':
    gunluk().run()
