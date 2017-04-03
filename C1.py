from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        self.label = Label(text = "Programming is fun", on_touch_down = self.alternate)
        return self.label

    def alternate(self, instance, touch):
        if self.label.text == "Programming is fun":
            self.label.text = "It is fun to program"
        else:
            self.label.text = "Programming is fun"

MyApp().run()
