from kivy.app import App
from kivy.uix.widget import Widget


class OxWidget(Widget):
    pass


class OxApp(App):
    def buld(self):
        return OxWidget()


if __name__ == '__main__':
    OxApp().run()
