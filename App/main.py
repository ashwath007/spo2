from kivy.app import App
from kivy.uix.button import Button


class Spo2App(App):
    def build(self):
        return Button(
            text='I am DJV',
            pos=(50,50)
            )


if __name__ == '__main__':
    Spo2App().run()
