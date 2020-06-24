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

class classD(classA,classC,classB):
   a,b=30,40
   def method4():
      return 'i am from class D'

obj=classD
print(obj.name,obj.p)
print(obj.method1(),obj.method3())
