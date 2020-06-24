class student():
   def __init__(self,name):
      print('this is paramatarized constructor')
      self.stu=name
   def show(self):
      return 'hello',self.stu
obj=student('sai')
print(obj.show())
