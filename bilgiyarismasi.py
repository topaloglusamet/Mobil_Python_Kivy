from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class QuizApp(App):
    def build(self):
        self.question_index = 0
        self.score = 0

        self.questions = [
            {'question': 'Başkentimiz neresidir?', 'options': ['Ankara', 'İstanbul', 'İzmir'], 'correct': 'Ankara'},
            {'question': 'Python hangi programlama dilidir?', 'options': ['Java', 'C++', 'Python'], 'correct': 'Python'},
            {'question': 'Dünyanın en yüksek dağı neresidir?', 'options': ['Everest', 'K2', 'Makalu'], 'correct': 'Everest'}
        ]

        main_layout = BoxLayout(orientation='vertical')

        self.question_label = Label(text=self.questions[self.question_index]['question'], font_size=20, halign='center', size_hint_y=None, height=100)
        main_layout.add_widget(self.question_label)

        for option in self.questions[self.question_index]['options']:
            btn_option = Button(text=option, on_press=self.check_answer, background_color=(0.5, 0.7, 1, 1), size_hint_y=None, height=60)
            main_layout.add_widget(btn_option)

        return main_layout

    def check_answer(self, instance):
        selected_answer = instance.text
        correct_answer = self.get_correct_answer()

        if selected_answer == correct_answer:
            self.score += 1

        self.question_index += 1

        if self.question_index < len(self.questions):
            self.update_question()
        else:
            self.display_result()

    def get_correct_answer(self):
        return self.questions[self.question_index]['correct']

    def update_question(self):
        self.question_label.text = self.questions[self.question_index]['question']

        for child in self.root.children:
            if isinstance(child, Button):
                child.text = self.questions[self.question_index]['options'][self.root.children.index(child) - 1]

    def display_result(self):
        result_label = Label(text=f'Skorunuz: {self.score}/{len(self.questions)}', font_size=24, halign='center')
        self.root.clear_widgets()
        self.root.add_widget(result_label)

if __name__ == '__main__':
    QuizApp().run()
