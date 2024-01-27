from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import requests

class NewsApp(App):
    def build(self):
        self.title = 'Haber Uygulaması'
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.news_label = Label(text='[b]Türkçe haberler burada görünecek.[/b]', markup=True, halign='center')

        self.get_news()

        self.layout.add_widget(self.news_label)
        return self.layout

    def get_news(self):
        api_key = '0a2e4c287c70413cbb10f5167f44142f'
        api_url = f'https://newsapi.org/v2/top-headlines?country=tr&apiKey={api_key}'

        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            articles = data.get('articles', [])
            if articles:
                news_text = ''
                for article in articles:
                    news_text += f"\n\n{article['title']}\n{article['author']}\n{article['publishedAt']}"
                self.news_label.text = news_text
            else:
                self.news_label.text = 'Haber bulunamadı.'
        else:
            self.news_label.text = 'Haberler alınamadı. Lütfen API anahtarınızı kontrol edin.'

if __name__ == '__main__':
    NewsApp().run()
