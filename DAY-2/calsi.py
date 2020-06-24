class calsi():
   def __init__(self,a,b):
      self.a=a
      self.b=b

   def add(self,c): # external parameter
      return self.a+self.b+c

a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))

obj=calsi(a,b)
print(obj.add(c))

