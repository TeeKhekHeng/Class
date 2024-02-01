class Phone:
    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year
    
    def display_info(self):
        return f"{self.name}, brand of {self.brand}, launched at {self.year}."

class Smartphone(Phone):
    def __init__(self, name, brand, year, os):
        super().__init__(name, brand, year)
        self.os = os
    
    def display_info(self):
        return f"{self.name}, brand of {self.brand}, launched at {self.year} and processed in {self.os}."

class Basicphone(Phone):
    def __init__(self, name, brand, year, is_touch_screen):
        super().__init__(name, brand, year)
        self.is_touch_screen = is_touch_screen
    
    def display_info(self):
        return f"{self.name}, brand of {self.brand}, launched at {self.year} and {self.is_touch_screen} touch screen."
    
#Creating instances
iphone = Smartphone("iPhone 13", "Apple", 2021, "iOS")
nokia = Basicphone("3310", "Nokia", 2000, False)

#Accessing methods
print(iphone.display_info())
print(nokia.display_info())
