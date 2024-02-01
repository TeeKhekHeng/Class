#Declaring the Main Class LibraryItem. 
class LibraryItem:
    def __init__(self, title, author, item_id):
        #3 variables had been declared below
        self.title = title
        self.author = author
        self.item_id = item_id
    
    def display_info(self):
        #This function is to display the info of the item in library
        return f"Title: {self.title}, Author: {self.author}, Item_id: {self.item_id}"

#Declaring the SubClass Book and inherit with the main class
class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id) #Used in copying the declaration done in the main class
        #Declaration of variable which is not included in the main class
        self.genre = genre
    
    def display_info(self):
        #Rewrite since another new variable is add on
        return f"Title: {self.title}, Author: {self.author}, Item_id: {self.item_id}, Genre: {self.genre}"

#Declaring the SubClass DVD and inherit with the main class
class DVD(LibraryItem):
    def __init__(self, title, author, item_id, director):
        super().__init__(title, author, item_id)
        #Declaration of variable which is not included in the main class
        self.director = director
    
    def display_info(self):
        #Rewrite since another new variable is add on
        return f"Title: {self.title}, Author: {self.author}, Item_id: {self.item_id}, Director: {self.director}"

#Variable is created and inserting information
Novel = Book("Harry Potter", "J.K. Rowling", 123, "Scientific")
Movie = DVD("Kung Fu Panda", "Jack Mark", 345, "Tom Holland")

#Print out the result after the function. 
print(Novel.display_info())
print(Movie.display_info())