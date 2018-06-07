from tkinter import *
import math

class Application:
	def getandreplace(self):
		"""replace x with * and ÷ with /"""
		
		self.expression = self.e.get()
		self.newtext=self.expression.replace(self.div,'/')
		self.newtext=self.newtext.replace('x','*')

	def equals(self):
		"""when the equal button is pressed"""

		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)
	
	def clear(self): 
		"""when clear button is pressed,clears the text input area"""
		self.e.delete(0,END)
	
	def action(self,argi): 
		"""pressed button's value is inserted into the end of the text area"""
		self.e.insert(END,argi)
	
	def __init__(self,master):
		"""Constructor method"""
		master.title('Calulator for kids programming') 
		master.geometry()
		self.e = Entry(master, font = "Helvetica 44 bold",justify="center",width=10,fg="orange",highlightthickness=1,bd=0)
		self.e.grid(row=0,column=0,columnspan=4,ipady=4)
		self.e.focus_set() 		
		self.div='÷'
		self.width = 12
		self.height = 3

		#Generating Buttons
		Button(master,text="7",width=self.width,height=self.height,command=lambda:self.action('7')).grid(row=1, column=0)
		Button(master,text="8",width=self.width,height=self.height,command=lambda:self.action(8)).grid(row=1, column=1)
		Button(master,text="9",width=self.width,height=self.height,command=lambda:self.action(9)).grid(row=1, column=2)		
		Button(master,text='CLR',width=self.width,height=self.height,command=lambda:self.clear()).grid(row=1, column=3)
		Button(master,text="4",width=self.width,height=self.height,command=lambda:self.action(4)).grid(row=2, column=0)
		Button(master,text="5",width=self.width,height=self.height,command=lambda:self.action(5)).grid(row=2, column=1)
		Button(master,text="6",width=self.width,height=self.height,command=lambda:self.action(6)).grid(row=2, column=2)		
		Button(master,text="+",width=self.width,height=self.height,command=lambda:self.action('+')).grid(row=2, column=3)
		Button(master,text="1",width=self.width,height=self.height,command=lambda:self.action(1)).grid(row=3, column=0)
		Button(master,text="2",width=self.width,height=self.height,command=lambda:self.action(2)).grid(row=3, column=1)
		Button(master,text="3",width=self.width,height=self.height,command=lambda:self.action(3)).grid(row=3, column=2)		
		Button(master,text="-",width=self.width,height=self.height,command=lambda:self.action('-')).grid(row=3, column=3)
		Button(master,text="0",width=self.width,height=self.height,command=lambda:self.action(0)).grid(row=4, column=0)
		Button(master,text="x",width=self.width,height=self.height,command=lambda:self.action('x')).grid(row=4, column=1)
		Button(master,text="÷",width=self.width,height=self.height,command=lambda:self.action(self.div)).grid(row=4, column=2)
		Button(master,text="=",width=self.width,height=self.height,command=lambda:self.equals()).grid(row=4, column=3)

#Main
root = Tk()
obj = Application(master = root) #object instantiated
root.mainloop()
