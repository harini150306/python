# oops concept:
# class and object:
# Create a class
# class Person:
#     # Constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Method
#     def greet(self):
#         print("Hello, my name is", self.name)

# # Create an object
# p1 = Person("John", 36)

# # Call the method
# p1.greet()


# init method
# # class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(self.name, "says Woof!")

# # Create object
# d1 = Dog("Buddy", 3)

# # Call method
# d1.bark()


# how to use self
# class car:
#     def __init__(self, brand):
#         self.brand = brand

#     def show(self):
#         print(self.brand)

# c1 = car("Ford")
# c1.show()

# class properties

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

# s1 = Student("Anna", "A")

# print(s1.grade)

# s1.grade = "B"

# print(s1.grade)

# class method

# class Rectangle:
#       def __init__(self,width,height):
#           self.width = width
#           self.height = height
#       def area(self):
#           return self.width*self.height
# r1 = Rectangle(5,3)
# print(r1.area())

class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies
    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book borrowed successfully")
        else:
            print("No copies available")
    def return_book(self):
        self.available_copies += 1
        print("Book returned successfully")
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available Copies:", self.available_copies)
s1 = Book("Python Basics", "Harini", 5)
s1.display()
s1.borrow_book()
s1.display()
s1.return_book()
s1.display()