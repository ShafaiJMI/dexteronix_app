from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from login import LoginWindow
from complaint import ComplaintPage

Window.clearcolor = (1, 1, 1, 1)
from kivy.uix.boxlayout import BoxLayout

class MainPage(BoxLayout):
	"""docstring for ComplaintPage"""
	login_widget = LoginWindow()
	complaint_widget = ComplaintPage()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ids.login_screen.add_widget(self.login_widget)
		self.ids.comp_screen.add_widget(self.complaint_widget)
		
class MainApp(App):
	def build(self):
		self.title = "Dexteronix Technologies"
		return MainPage()

if __name__=='__main__':
	MainApp().run()