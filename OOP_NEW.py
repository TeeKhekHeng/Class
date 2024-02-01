class person:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
    def giveRaise(self, ratio):
        self.ratio = ratio
        self.pay = (self.pay*self.ratio)+self.pay
        return self.pay
    def lastName(self):
        x = self.name
        x = x.split()
        return f"{x[-1]}" 
    
class manager(person):
    def __init__(self, name, age, pay):
        super().__init__(name, age, pay)
    def giveRaise(self, ratio):
        super().giveRaise(ratio)
    def lastName(self):
        return f"{super().lastName()}"
    
bob = person('Bob Smith', 42, 10000)
sue = person(name='Sue Jones', age=45, pay=20000)
tom = manager(name='Tom Doe', age=52, pay=30000)
db = [bob, sue, tom]
for obj in db:
    obj.giveRaise(.10)
for obj in db:
    print(obj.lastName(), '=>', obj.pay)

