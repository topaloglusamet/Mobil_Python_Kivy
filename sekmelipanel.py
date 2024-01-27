from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.lang import Builder

class SekmeliPanelApp(App):
    def build(self):
        sekmeli_panel = TabbedPanel()

        # İlk sekme
        sekmeli_panel.default_tab.text = 'İlk Sekme'
        sekmeli_panel.default_tab.content = Label(text="Sekmeli Panel'in İlk sayfası")

        # Diğer sekmeler
        for i, isim in enumerate(('Dilek', 'Fatih', 'Melike')):
            sekme = TabbedPanelHeader(text='Sekme %d' % (i + 1))
            sekme.content = Label(text="Bu sekmenin sahibi: %s" % isim)
            sekmeli_panel.add_widget(sekme)

        return sekmeli_panel

if __name__ == '__main__':
    SekmeliPanelApp().run()
