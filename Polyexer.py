class HotDrink:
    def __init__(self, sub, type, temp):
        self.sub = sub
        self.type = type
        self.temp = temp

    def display_Info(self):
        return f"{self.sub} - Type: {self.type}, Temperature: {self.temp}"
    
class Coffee(HotDrink):
    def __init__(self, sub, type, temp):
        super().__init__(sub, type, temp)

class Tea(HotDrink):
    def __init__(self, sub, type, temp):
        super().__init__(sub, type, temp)

class HotChocolate(HotDrink):
    def __init__(self, sub, type, temp):
        super().__init__(sub, type, temp)

coffee = Coffee("Coffee", "Espresso", "Hot")
tea = Tea("Tea", "Green Tea", "Warm")
hotchocolate = HotChocolate("Hot Chocolate", "Dark Chocolate", "Very Hot")

print(coffee.display_Info())
print(tea.display_Info())
print(hotchocolate.display_Info())

