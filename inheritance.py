class Person:

    def __init__(self, name, age, hobby, sex):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.sex = sex
    
    def hello(self):
        print(f'Hello my name is {self.name} and I love {self.hobby}')
    
    def gender(self):
        print(f'Hello my name is {self.name} and I am a {self.sex}')

    def boy(self):
        print("hello")

class Ultra(Person):
    def __init__(self, name, age, hobby, sex, iq):
        super().__init__(name, age, hobby, sex)
        self.iq = iq



class Male(Person):

    def __init__(self, name, age, hobby, sex, mood):
        super().__init__(name, age, hobby, sex)
        self.mood = mood

    def boy(self):
        print("yo")
    
    def happiness(self):
        print(f'I am {self.age} years old and I am very fucking {self.mood}')


class Female(Person):

    def __init__(self, name, age, hobby, sex, reputation):
        super().__init__(name, age, hobby, sex)
        self.reputation = reputation

    def girl(self):
        print("heeyy")

    def standing(self):
        print(f'Hello my name is {self.name}, I am a {self.sex} and with warsong gulch I am {self.reputation}')

class Uni(Ultra):
    def __init__(self, name, age, hobby, sex, iq, hair_color):
        super().__init__(name, age, hobby, sex, iq)
        self.hair_color = hair_color
    def child(self):
        print(f'Hi my name is {self.name} and I am {self.age} years old and my iq is {self.iq}, my hair color is {self.hair_color}.')
    


m1 = Male("Bob", 45, "Bowling", "Male", "Happy")
u3 = Uni("Heather", 54, "Horses", "Uni", 50, "black")
f1 = Female("Sarah", 21, "fashion", "female", "Exalted")
m2 = Male("Richard", 33, "eating", "Male", "Depressed")
f2 = Female("Joan", 88, "alcohol", "female", "Honored")
print(m1.happiness())
print(f1.standing())
print(m2.happiness())
print(f2.standing())

print(u3.child())
