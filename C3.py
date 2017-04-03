"""
Investment value calculator
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout = GridLayout(cols = 2, rows = 5, row_force_default = True,
                            row_default_height = 40)

        layout.add_widget(Label(text = "Investment Amount"))
        self.inv_amt = TextInput(text = '', multiline = False)
        layout.add_widget(self.inv_amt)

        layout.add_widget(Label(text = "Years"))
        self.years = TextInput(text = '', multiline = False)
        layout.add_widget(self.years)

        layout.add_widget(Label(text = "Annual Interest Rate"))
        self.air = TextInput(text = '', multiline = False)
        layout.add_widget(self.air)

        layout.add_widget(Label(text = "Future Value"))
        self.fv = Label(text = "0")
        layout.add_widget(self.fv)

        layout.add_widget(Button(text = "Calculate", on_press = self.calc))

        return layout

    def calc(self, btn):
        IA = int(self.inv_amt.text)
        Y = int(self.years.text)
        AIR = float(self.air.text)

        print IA, Y , AIR

        FV = IA * ((1 + ((AIR/12.0)/100.0)) ** (Y*12.0))
        print FV

        self.fv.text = u'{}'.format(round(FV,2))

MyApp().run()
