from kivy.app import App
from kivy.uix.label import Label
from kivy.gesture import Gesture, GestureDatabase


class MyApp(App):
    def build(self):
        self.label = Label(text = "Slide Me", on_touch_move = self.detect)
        return self.label

    def detect(self, instance, touch):
        threshold = 0.05
        if touch.dx > 0 and abs(touch.dy) < threshold:
            self.label.text = "Slide Right"
        elif touch.dx < 0 and abs(touch.dy) < threshold:
            self.label.text = "Slide Left"
        elif abs(touch.dx) < threshold and touch.dy > 0:
            self.label.text = "Slide Up"
        elif abs(touch.dx) < threshold and touch.dy < 0:
            self.label.text = "Slide Down"
        # print touch


MyApp().run()
