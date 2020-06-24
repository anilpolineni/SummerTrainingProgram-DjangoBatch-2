class student():
   def __init__(self):
      print('this is non paramatarized constructor')
   def show(self,name):
      return('hello',name)
obj=student()
print(obj.show('anil'))
