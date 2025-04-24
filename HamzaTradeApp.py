from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text="مرحباً بك في تطبيق التداول")
        self.add_widget(self.label)

        self.button = Button(text="اضغطني")
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

    def on_button_press(self, instance):
        self.label.text = "تم الضغط!"

class HamzaTradeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    HamzaTradeApp().run()
