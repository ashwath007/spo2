from kivy.app import App
from kivy.uix.button import Button


class AddButton(Button):
    pass 


class Spo2App(App):
    def build(self):
        return AddButton(
            text="Add",
            pos=(100,100),
            size_hint=(100,50)
        )





if __name__ == '__main__':
    Spo2App().run()
