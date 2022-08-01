from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

Window.clearcolor = (1, 1, 1, 1)
Builder.load_file('home.kv')

class HomePage(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	def nextpage(self):
		self.parent.parent.current = "comp_screen"
class HomeApp(App):
	def build(self):
		self.title = "Dexteronix Technologies"
		return HomePage()

if __name__ == "__main__":
	HomeApp().run()