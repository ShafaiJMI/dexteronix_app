from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
#from kivy.uix.boxlayout import BoxLayout

class ComplaintPage(Widget):
	def __init__(self):
		self.title = "Dexteronix Technologies"
		self.window = GridLayout()
		self.window.cols = 1
		self.window.size_hint = (0.6,0.7)
		self.window.spacing = (0.8,0.9)
		self.window.pos_hint = {'center_x':0.5,'center_y':0.5}
		self.pagetitle = Label(text="Register Your Complaint here",font_size=18,color="#000000")
		self.window.add_widget(self.pagetitle)
		self.bin_id = TextInput(hint_text='Bin ID',multiline=False,background_color=(1, 1, 1, 1),padding_y=(10,10),size_hint=(1,0.3))
		self.window.add_widget(self.bin_id)
		self.complaint_type = TextInput(hint_text='Complaint Type',multiline=False,background_color=(1, 1, 1, 1),line_height=18,padding_y=(10,10),size_hint=(1,0.3))
		self.window.add_widget(self.complaint_type)
		self.complaint = TextInput(hint_text='Complaint',multiline=True,background_color=(1, 1, 1, 1),padding_y=(10,10))
		self.window.add_widget(self.complaint)
		self.loginbutton = Button(text='Submit',background_color=(0,0,1,1),font_size=24,size_hint=(1,0.4))
		self.window.add_widget(self.loginbutton)

class DexApp(App):
	def build(self):
		self.title = "Dexteronix Technologies"
		self.window = GridLayout()
		self.window.cols = 1
		self.window.size_hint = (0.6,0.7)
		self.window.spacing = (0,5)
		self.window.pos_hint = {'center_x':0.5,'center_y':0.5}
		self.window.add_widget(Image(source="dex_logo.jpg"))
		self.emailinput = TextInput(hint_text='Your email',multiline=False,font_size=18,background_color=(1, 1, 1, 1),padding_y=(10,10),size_hint=(1,0.3))
		self.window.add_widget(self.emailinput)
		self.passwordinput = TextInput(hint_text='Password',multiline=False,password=True,font_size=18,background_color=(1, 1, 1, 1),padding_y=(10,10),size_hint=(1,0.3))
		self.window.add_widget(self.passwordinput)
		self.loginbutton = Button(text='Login',background_color='#0ca94f',font_size=24,size_hint=(1,0.4))
		self.loginbutton.bind(on_press=self.callback)
		self.window.add_widget(self.loginbutton)
		
		return self.window
		
	def callback(self,instance):
		return ComplaintPage()

class ComplaintApp(App):
	def build(self):
		self.title = "Dexteronix Technologies"
		self.window = GridLayout()
		self.window.cols = 1
		self.window.size_hint = (0.6,0.7)
		self.window.spacing = (0,5)
		self.window.pos_hint = {'center_x':0.5,'center_y':0.5}
		self.pagetitle = Label(text="Register Your Complaint here",font_size=18,color="#000000")
		self.window.add_widget(self.pagetitle)
		self.bin_id = TextInput(hint_text='Bin ID',multiline=False,background_color=(1, 1, 1, 1),padding_y=(10,10),size_hint=(1,0.3))
		self.window.add_widget(self.bin_id)
		self.complaint_type = TextInput(hint_text='Complaint Type',multiline=False,background_color=(1, 1, 1, 1),line_height=18,padding_y=(10,10),size_hint=(1,0.3))
		self.window.add_widget(self.complaint_type)
		self.complaint = TextInput(hint_text='Complaint',multiline=True,background_color=(1, 1, 1, 1),padding_y=(10,10))
		self.window.add_widget(self.complaint)
		self.loginbutton = Button(text='Submit',background_color=(0,0,1,1),font_size=24,size_hint=(1,0.4))
		self.window.add_widget(self.loginbutton)
		
		return self.window

if __name__=='__main__':
	DexApp().run()