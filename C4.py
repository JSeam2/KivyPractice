from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
		Button:
			text: 'Settings'
			on_press: root.manager.current = 'settings'
		Button:
			text: 'Quit'
            on_press: app.stop()
<SettingsScreen>:
	BoxLayout:
		Label:
			text: 'Settings Screen'
		Button:
			text: 'Back to Menu'
			on_press: root.manager.current = 'menu'
""")


# Build Screens
class MenuScreen(Screen):
	pass

class SettingsScreen(Screen):
    pass

# Screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name = 'menu'))
sm.add_widget(SettingsScreen(name = 'settings'))


class MyApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()
