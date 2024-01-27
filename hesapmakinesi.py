from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Example(App):
    def build(self):
        self.title = "Hesap Makinesi"
        self.icon = 'jpg.jpg'

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.display = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    background_color=(0.2, 0.6, 1, 1),  # R, G, B, A renk değerleri (mavi tonu)
                    color=(1, 1, 1, 1),  # R, G, B, A renk değerleri (beyaz)
                    font_size=24
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)

            layout.add_widget(h_layout)

        # Silme tuşları
        delete_all_button = Button(
            text='C',
            background_color=(1, 0.2, 0.2, 1),  # Kırmızı tonu
            color=(1, 1, 1, 1),  # Beyaz
            font_size=24
        )
        delete_all_button.bind(on_press=self.on_delete_all)
        layout.add_widget(delete_all_button)

        delete_last_button = Button(
            text='<-',
            background_color=(1, 0.2, 0.2, 1),  # Kırmızı tonu
            color=(1, 1, 1, 1),  # Beyaz
            font_size=24
        )
        delete_last_button.bind(on_press=self.on_delete_last)
        layout.add_widget(delete_last_button)

        # Eşittir butonu
        equal_button = Button(
            text='=',
            background_color=(0.2, 0.8, 0.2, 1),  # Yeşil tonu
            color=(1, 1, 1, 1),  # Beyaz
            font_size=24
        )
        equal_button.bind(on_press=self.on_button_press)
        layout.add_widget(equal_button)

        return layout

    def on_button_press(self, instance):
        current_text = self.display.text

        if instance.text == '=':
            try:
                result = str(eval(current_text))
                self.display.text = result
            except Exception as e:
                self.display.text = 'HATA!'
        else:
            self.display.text = current_text + instance.text

    def on_delete_all(self, instance):
        self.display.text = ''

    def on_delete_last(self, instance):
        current_text = self.display.text
        self.display.text = current_text[:-1]

if __name__ == '__main__':
    Example().run()
