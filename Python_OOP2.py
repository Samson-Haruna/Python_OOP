#INHERITANCE
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"my name is{self.name} and i am {self.age} years old")


class Cat(Pet):
    def __init__(self,name, age, color):
        super().__init__(name,age) # calling an atribute from the super class Pet
        self.color = color

    def speak(self):
        print("moew")

    def show(self):
        print(f"my name is {self.name} i am {self.age} years old and i am {self.color} in color")

class Dog(Pet):
    def speak(self):
        print("bark")      

c = Cat('mike',15,'brown') 
c.show()

