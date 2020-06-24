class classA():
   name,program='Appsdc','Djangoworkshop'
   def method1():
      return 'i am from classA'

class classB():
   x,y=10,20
   def method2():
      return 'i am classB'

class classC(classB):
   p,q='python','django'

   def method3():
      return 'i am from class C'
obj=classC
print(obj.x)
print(obj.method2())
