from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import requests
from datetime import datetime


class WeatherApp(App):
    def build(self):
        self.title = 'Hava Durumu Uygulaması'
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.city_input = TextInput(hint_text='Şehir adını girin', multiline=False)
        self.get_weather_button = Button(text='Hava Durumu Getir', on_press=self.get_weather)
        self.weather_label = Label(text='Hava durumu bilgisi burada görünecek.')
        self.clock_label = Label(text='')

        self.layout.add_widget(self.city_input)
        self.layout.add_widget(self.get_weather_button)
        self.layout.add_widget(self.weather_label)
        self.layout.add_widget(self.clock_label)

        # Saatte bir get_weather fonksiyonunu çağırmak için Clock.schedule_interval kullanılıyor.
        Clock.schedule_interval(self.update_clock, 1)  # Her saniyede bir saat güncelle

        return self.layout

    def get_weather(self, instance):
        # Bu fonksiyon, butona tıklandığında hava durumu bilgisini günceller.
        api_key = '1f8d22bc120b6e3200fe0f9bbb038085'
        city_name = self.city_input.text
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            timestamp = data['dt']
            timezone_offset = data['timezone']
            observation_time = datetime.utcfromtimestamp(timestamp + timezone_offset)

            # Tarih ve saat bilgisini daha okunabilir bir formata dönüştür
            formatted_time = observation_time.strftime("%Y-%m-%d %H:%M:%S")

            weather_info = f'{city_name} - Sıcaklık: {temperature}°C, Tarih ve Saat: {formatted_time}, Durum: {description.capitalize()}'
            self.weather_label.text = weather_info
        else:
            self.weather_label.text = 'Hava durumu bilgisi alınamadı. Lütfen şehir adını kontrol edin.'

    def update_clock(self, dt):
        # Saat bilgisini günceller
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.clock_label.text = f"Aktüel Saat: {current_time}"


if __name__ == '__main__':
    WeatherApp().run()
