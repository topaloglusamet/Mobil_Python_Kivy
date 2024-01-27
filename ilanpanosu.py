# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random

Builder.load_string("""
<duyuruPenceresi>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Duyurular'
            font_size: 30
        Button:
            text: 'Ana Sayfa'
            on_press: root.manager.current = 'anasayfa'
        BoxLayout:
            orientation: 'vertical'
            id: duyuru_layout

<anasayfaPenceresi>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Ana Sayfa'
            font_size: 30
        Button:
            text: 'Atasözleri ve Deyimler'
            on_press: root.manager.current = 'atasozleri'
        Button:
            text: 'Resimler'
            on_press: root.manager.current = 'resimler'
        Button:
            text: 'Duyurular'
            on_press: root.manager.current = 'duyurular'

<atasozuPenceresi>:
    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Atasözleri ve Deyimler'
                font_size: 30
            Button:
                text: 'Ana Sayfa'
                on_press: root.manager.current = 'anasayfa'
            Label:
                id: atasozu_label
                text: ''
                font_size: 20

<resimPenceresi>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Resimler'
            font_size: 30
        Button:
            text: 'Ana Sayfa'
            on_press: root.manager.current = 'anasayfa'
        Image:
            id: resim
            source: ''
            size_hint_y: None
            height: '300dp'


""")

class duyuruPenceresi(Screen):
    def on_enter(self):
        duyuru_layout = self.ids.duyuru_layout
        duyuru_layout.clear_widgets()  # Mevcut widget'ları temizle

        for i in range(5):  # Örnek olarak 5 adet duyuru ekleyelim
            duyuru_label = Label(text=f'Duyuru {i + 1}', font_size=20)
            duyuru_layout.add_widget(duyuru_label)

class atasozuPenceresi(Screen):
    def on_enter(self):
        atasozu_text = "\n".join(IlanPanosuUyg.atasozleri)
        self.ids.atasozu_label.text = atasozu_text

class resimPenceresi(Screen):
    def on_enter(self):
        resim = random.choice(IlanPanosuUyg.resimler)
        self.ids.resim.source = resim[0]

class anasayfaPenceresi(Screen):
    pass

class IlanPanosuUyg(App):
    atasozleri = [
        'Abanın kadri yağmurda bilinir.',
        'Acı patlıcanı kırağında çalmaz.',
        'Aç bırakma hırsız edersin, çok söyleme arsız (yüzsüz) edersin.',
        'Misafir on kısmetle gelir; birini yer dokuzunu bırakır.'
    ]

    resimler = [
        ('resim.jpg', 'Ilçemizde bu yıl kiraz verimin yüksek olacağı beklenmektedir'),
        ('resim2.jpg', 'Ilçemizde yetişen Şeftali\'ler tüm dünyaya satılıyor'),
        ('resim3.jpg', 'Çilek mevsimi geldi. Bol vitamin için çilek yiyin')
    ]

    def build(self):
        sm = ScreenManager()

        sm.add_widget(anasayfaPenceresi(name='anasayfa'))
        sm.add_widget(atasozuPenceresi(name='atasozleri'))
        sm.add_widget(resimPenceresi(name='resimler'))
        sm.add_widget(duyuruPenceresi(name='duyurular'))

        return sm

if __name__ == '__main__':
    IlanPanosuUyg().run()
