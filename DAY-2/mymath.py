from packages import math   # (folder name,filename)

#from packages.math import math

obj=math.Math  # object=filename.classname
print(dir(obj))

print(obj.even(20))

print(obj.odd(1))

print(obj.add(10,10))

num1=int(input('enter num1 value'))
num2=int(input('enter num2 value'))
print(obj.pow(num1,num2))
