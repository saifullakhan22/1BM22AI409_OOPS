class dog:
  def __init__(self,name,size,breed='unknow',dob='unknow'):
    self.name = name
    self.size = size
    self.breed = breed
    self.dob = dob
  
  def bark(self):
    print(f'{self.name} says bow bow')

name1 = input("enter dog name")
size1 = input(f'enter {name1} size')
breed1 = input(f'enter breed of {name1}')or "unknown"
dob1 = input(f'enter breed of {name1}')or "unnknown"

dog1 = dog(name1,size1,breed1,dob1)

print(dog1.name,dog1.size,dog1.breed,dog1.dob)

dog1.bark()
