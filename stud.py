class student:
	def getdata(self):
		self.name=input("enter your name: ")
		self.no=input("enter phone no:")
	
	def display(self):
		print(self.name)
		print(self.no)
	
x=int(input("enter the total ono f entries"))
for i in range(0,x):
	obj=student()
	obj.getdata()
	obj.display()
