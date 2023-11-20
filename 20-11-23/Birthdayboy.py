class Birthdayboy:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def birthday(self):
    self.age += 1

vas = Birthdayboy('vasanth',20)

print(vas.name,vas.age)

vas.birthday()

print(vas.name,vas.age)
