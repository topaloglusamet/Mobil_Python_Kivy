# kivy modülünü içe aktarın
import kivy

# Bu, kivy sürümünü kısıtlar, yani
# bu kivy sürümünden düşük sürümü kullanamazsınız
kivy.require("1.9.1")

# Uygulamanızın temel sınıfı, App sınıfından kalıtım alır.
# app her zaman uygulamanızın örneğine işaret eder
from kivy.app import App

# Animasyonlarla çalışmak için Animasyon'u içe aktarmalısınız
from kivy.animation import Animation

# Button, basıldığında (veya tıklama/dokunma sonrasında) tetiklenen
# eylemlerle ilişkilendirilmiş bir etiket olan bir Label'dir.
from kivy.uix.button import Button


# Uygulama sınıfını oluşturun
class TestApp(App):

    # Animasyonların eklenmiş olduğu fonksiyonu tanımlama

    def animate(self, instance):
        # bir animasyon nesnesi oluşturun. Bu nesne saklanabilir
        # ve her çağrıda yeniden kullanılabilir veya farklı widget'lar arasında
        # yeniden kullanılabilir.
        # += bir ardışık adımdır, &= paralel bir adımdır
        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))

        # animasyonu, "instance" argümanında geçirilen düğme üzerine uygulayın
        # Dikkat edilmesi gereken varsayılan 'click' animasyonu (fare basılıyken
        # düğmenin rengini değiştirme) değişmez.
        animation.start(instance)

    def build(self):
        # bir düğme oluşturun ve animate()
        # yöntemini on_press işleyici olarak ekleyin
        button = Button(size_hint=(0.3, 0.1), text='Animasyon Çalıştır',
                        background_color=(1, 0.2, 0.2, 1),  # Kırmızı tonu
                        color=(1, 1, 1, 1),  # Beyaz
                        font_size=24,
                        on_press=self.animate)
        return button

    # Uygulamayı çalıştırın
if __name__ == '__main__':
    TestApp().run()
