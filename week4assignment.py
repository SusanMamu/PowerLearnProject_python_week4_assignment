class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return ("Hello, my name is " + self.name + ". I am " + str(self.age) + " years old. I am a " + self.gender + ".")

person1 = Person("Susan", 20, "Female")
print(person1.introduce())
