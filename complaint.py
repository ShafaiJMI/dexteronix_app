from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest

Window.clearcolor = (1, 1, 1, 1)
Builder.load_file('complaint.kv')

class ComplaintPage(GridLayout):
	"""docstring for ComplaintPage"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.message = self.ids.message

	def register_complaint(self):
		bin_id = self.ids.bin_id.text
		complaint_type = self.ids.complaint_type.text
		complaint = self.ids.complaint.text
		url = "http://shafai.pythonnaywhere.com/complaint/register/"

		if complaint_type == "" or complaint == "":
			self.message.text = "[color=#FF0000]Input Required[/color]"
		else:
			json_data = {"bin_id":bin_id,"complaint_type":complaint_type,"complaint":complaint}
			headers = {'Content-type': 'application/json','Accept': 'application/json'}
			res = UrlRequest(url,
			on_failure=self.got_fail,
            on_error=self.got_error,
            debug=True,
            on_success=self.got_success,
            on_redirect=self.got_redirecton_success,
            req_body=json_data,
            req_headers=headers)

	def clear_fields(self):
		self.ids.bin_id.text =""
		self.ids.complaint_type.text =""
		self.ids.complaint.text =""

	def got_success(self, request, data):
		self.message.text = "[color=#00FF00]Complaint registered[/color]"
		self.clear_fields()

	def got_fail(self, request, data):
		self.message.text = "[color=#FF0000]Request Failed[/color]"

	def got_error(self, request, data):
		self.message.text = "[color=#FF0000]Error Occured[/color]"

	def got_redirecton_success(self, request, data):
		self.message.text = "[color=#FF0000]Redirected[/color]"

class ComplaintApp(App):
	def build(self):
		self.title = "Dexteronix Technologies"
		return ComplaintPage()

if __name__=='__main__':
	ComplaintApp().run()