from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.label = Label(text = "Slide Me", on_touch_move = self.detect)
        return self.label

    def detect(self, instance, touch):
        def on_touch_left(touch):
            self.label.text = "Slide Left"
        def on_touch_right(touch):
            self.label.text = "Slide Right"
        def on_touch_down(touch):
            self.label.text = "Slide Down"
        def on_touch_up(touch):
            self.label.text = "Slide Up"

MyApp().run()
