class classA():
   a,b=20,30
   def disply():
      return 'i am from classA'

class classB(classA):
   c,d=40,50
   def display1():
      return 'i am from class B'

obj=classB
print(obj.a,obj.b,obj.c,obj.d)
print(obj.display1())
