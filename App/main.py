from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class AddButton(Button):
    def __init__(self, **kwargs):
        super(AddButton, self).__init__(**kwargs)
        self.text="Add News"
        self.pos=(100,50)
        self.size_hint=(.25,.25)


class Spo2App(App):
    def build(self):
        return AddButton()





if __name__ == '__main__':
    Spo2App().run()
