''' OBJECTS AND CLASSES
An object is a collection of data (variables) and methods (functions). Similarly, a class is a blueprint for that object.

  1. Classes
  A class is considered a blueprint of objects. We can think of the class as a sketch (prototype) of a house. It contains all the details about the 
  floors, doors, windows etc. Based on these descriptions we build the house. Each house is an object. Since many houses can be made from the same 
  description, we can create many objects from a class. The variables inside a class are called attributes.

  2. Objects

  An object is a called instance of a class. For example, if Bike is a class then we can create objects like bike1 and bike2 from the class. The 
  syntax for creating an object is as follows:

  objectName = ClassName()
  '''

import random

# class dwarf_lb:
#   name = random.choice(["Med", "Kulet", "Ngalák", "Kuthdêng","Alak", "Agseth", "Lor", "Bomrek"])
#   height = random.randint (100, 152)
#   age = random.randint(12,170)
#   stress = 0
#   profession = random.choice(["Mudminder", "Plankmaster", "Animaster", "Minemaster", "Portal-lord", "Grey Mace", "Lapidist",])
#   if profession == "Mudminder":
#     guildhall = "Farmer's Guild"
#   elif profession == "Plankmaster":
#     guildhall = "Woodworker's Guild"
#   elif profession == "Animaster":
#     guildhall = "Ranger's Guild"
#   elif profession == "Minemaster":
#     guildhall = "Miner's Guild"
#   elif profession == "Lapidist":
#     guildhall = "Jeweller's Guild"
#   else:
#     guildhall = "Adventurer's Guild"

#The variables inside a class are called attributes.

# d1 = dwarf_lb()

#We have created here an object of the class. Using the . notation, we can access the attributes of the class.

# dwarf1.name = "Urist"
# dwarf1.height = 152

# print(f'{d1.name} is {d1.age} years old and {d1.height} centimetres tall. By profession, they are a {d1.profession} and therefore a member of the {d1.guildhall}.')

#Task 1: Create a Dwarf class. Each Dwarf should have a name, profession, and a happiness level. Allow these to be set during initialization and 
# retrieved via methods. For extra complexity, add a method that allows you to change a Dwarf's profession.

class Dwarf:
  def __init__(self, name, profession):
    self.name = name
    self.profession = profession
    self.happiness = 100
  def change_job(self, profession):
    if profession == self.profession:
      print("This is already their profession.")
    else:
      self.profession = profession
      print(f"{self.name} has changed career. They are now a {self.profession}).")

dw1 = Dwarf(
  random.choice(["Med", "Kulet", "Ngalák", "Kuthdêng","Alak", "Agseth", "Lor", "Bomrek"]),
  random.choice(["Mudminder", "Plankmaster", "Animaster", "Minemaster", "Portal-lord", "Grey Mace", "Lapidist",])
  )

print(dw1.name)
print(dw1.profession)
print(dw1.happiness)

dw1.change_job("warrior")

# 2. Dwarf Generator

# Create a function that randomly generates Dwarfs with names, professions, and a happiness level. Store these Dwarfs in a list.

# def dgen(population):
#   for pop in (population):

  