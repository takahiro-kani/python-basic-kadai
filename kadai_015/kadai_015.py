class Human:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def print_info(self):
    print(self.name,self.age)
hage = Human("ハゲ",46)
hage.print_info()
