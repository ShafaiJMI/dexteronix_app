from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder
import requests

Window.clearcolor = (1, 1, 1, 1)
Builder.load_file('complaint.kv')

class ComplaintPage(GridLayout):
	"""docstring for ComplaintPage"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def register_complaint(self):
		bin_id = self.ids.bin_id.text
		complaint_type = self.ids.complaint_type.text
		complaint = self.ids.complaint.text
		message = self.ids.message
		url = "https://shafai.pythonanywhere.com/complaint/register/"

		if complaint_type == "" or complaint == "":
			message.text = "[color=#FF0000]Input Required[/color]"
		else:
			data = {
			"bin_id":bin_id,
			"complaint_type":complaint_type,
			"complaint":complaint
			}
			res = requests.post(url,data)
			if res.status_code ==  200:
				message.text = "[color=#00FF00]Complaint registered[/color]"
				self.clear_fields()
			else:
				message.text = "[color=#FF0000]Error Occured[/color]"
	def clear_fields(self):
		self.ids.bin_id.text =""
		self.ids.complaint_type.text =""
		self.ids.complaint.text =""

class ComplaintApp(App):
	def build(self):
		self.title = "Dexteronix Technologies"
		return ComplaintPage()

if __name__=='__main__':
	ComplaintApp().run()