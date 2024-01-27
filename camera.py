import kivy

# Kivy sürümünü belirtmek
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.anchorlayout import AnchorLayout

import cv2
import numpy as np

# Kivy uygulamasını temsil eden CameraApp sınıfını oluşturun
class CameraApp(App):
    def build(self):
        # Kamerayı temsil eden bir değişken (başlangıçta kapalı)
        self.capture = None

        # Ana düzen: dikey bir kutu düzeni
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Orta hizalanacak bir AnchorLayout ekleyin
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        layout.add_widget(anchor_layout)

        # Kameradan alınan görüntüyü göstermek için Image widget'ı
        self.my_camera = Image(size=(640, 480), allow_stretch=True)
        anchor_layout.add_widget(self.my_camera)

        # Kamerayı açma/kapatma işlemlerini gerçekleştiren Toggle düğmesi
        self.toggle_button = Button(
            text='Kamera Aç', size_hint=(None, None), width=200, height=50,
            background_color=(0.2, 0.6, 1, 1),  # RGB renk formatı
            font_size=20, font_name='Arial'
        )
        self.toggle_button.bind(on_press=self.toggle_camera)
        layout.add_widget(self.toggle_button)

        # Fotoğraf çekme işlemini gerçekleştiren düğme
        self.photo_button = Button(
            text='Fotoğraf Çek', size_hint=(None, None), width=200, height=50,
            background_color=(0.2, 0.6, 0.2, 1),  # RGB renk formatı
            font_size=20, font_name='Arial'
        )
        self.photo_button.bind(on_press=self.take_photo)
        layout.add_widget(self.photo_button)

        # Kameradan alınan görüntüyü düzenli olarak güncellemek için bir Clock kullanılır
        Clock.schedule_interval(self.update, 1.0 / 30.0)

        # Oluşturulan düzeni uygulama penceresine yerleştirin
        return layout

    # Kamera açma/kapatma işlemini gerçekleştiren fonksiyon
    def toggle_camera(self, instance):
        if self.capture is None:
            # Kamera açılmamışsa
            self.capture = cv2.VideoCapture(0)
            self.toggle_button.text = 'Kamera Kapat'
        else:
            # Kamera açılmışsa
            self.capture.release()
            self.capture = None
            self.toggle_button.text = 'Kamera Aç'

    # Kameradan alınan görüntüyü güncelleyen fonksiyon
    def update(self, dt):
        if self.capture is not None:
            ret, frame = self.capture.read()
            if ret:
                # Kameradan alınan görüntüyü düzenleyip Image widget'ına aktarın
                buf1 = cv2.flip(frame, 0)
                buf = buf1.tostring()
                image_texture = Texture.create(
                    size=(frame.shape[1], frame.shape[0]), colorfmt='bgr'
                )
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.my_camera.texture = image_texture
        else:
            # Kamera kapalıysa beyaz bir ekran göster
            white_image = np.ones((480, 640, 3), dtype=np.uint8) * 255
            white_buf = cv2.flip(white_image, 0).tostring()
            white_texture = Texture.create(size=(640, 480), colorfmt='bgr')
            white_texture.blit_buffer(white_buf, colorfmt='bgr', bufferfmt='ubyte')
            self.my_camera.texture = white_texture

    # Fotoğraf çekme işlemini gerçekleştiren fonksiyon
    def take_photo(self, instance):
        if self.capture is not None:
            ret, frame = self.capture.read()
            if ret:
                # Fotoğrafı kaydetmek istediğiniz dosya adını ve yolunu belirtin
                photo_path = "deneme.jpg"
                cv2.imwrite(photo_path, frame)
                print(f"Fotoğraf kaydedildi: {photo_path}")

# Uygulamayı başlatın
if __name__ == '__main__':
    CameraApp().run()
