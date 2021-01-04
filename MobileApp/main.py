from kivy.app import App
from kivy.uix.widget import Widget


class OxWidget(Widget):
    pass


class OxApp(App):
    def build(self):
        return OxWidget()



OxApp().run()
