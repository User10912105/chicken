class Animal():
    def __init__(self,name):
      self.name = name
class chick(Animal):
    def __init__(self,name):
        super().__init__(self,name)
n=str(input("請輸入名字"))
print(n,'誕生了')
