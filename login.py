from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder

Window.clearcolor = (1, 1, 1, 1)
Builder.load_file('login.kv')

class LoginWindow(GridLayout):
	"""docstring for LoginWindow"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def validate_user(self):
		email_in = self.ids.email_input
		password_in = self.ids.password_input
		message = self.ids.message

		email = email_in.text
		password = password_in.text

		if email == "" or password == "":
			message.text = "[color=#ff0000]Input Required[/color]"
		else:
			if email=="user" and password =="123":
				message.text = "[color=#00ff00]Logging in[/color]"
				self.parent.parent.current = 'comp_screen'
			else:
				message.text = "[color=#ff0000]Invalid Email or Password[/color]"
		
class LoginApp(App):
	def build(self):
		self.title = "Dexteronix Technologies"
		return LoginWindow()

if __name__ == "__main__":
	LoginApp().run()
