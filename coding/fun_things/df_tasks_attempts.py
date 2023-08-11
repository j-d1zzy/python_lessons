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
    
    self.happiness = 50
        
    self.mood = ""
    
    self.guildhall = ""
    if self.profession == "Mudminder":
      self.guildhall = "Farmer's Guild"
    elif self.profession == "Plankmaster":
      self.guildhall = "Woodworker's Guild"
    elif self.profession == "Animaster":
      self.guildhall = "Ranger's Guild"
    elif self.profession == "Minemaster":
      self.guildhall = "Miner's Guild"
    elif self.profession == "Lapidist":
      self.guildhall = "Jeweller's Guild"
    else:
      self.guildhall = "Fighter's Guild"

  
  def change_job(self, profession):
    if profession == self.profession:
      print("This is already their profession.")
    else:
      self.profession = profession
      print(f"{self.name} has changed career. They are now a {self.profession} of the {self.guildhall}).")

# dw1 = Dwarf(
#   random.choice(["Med", "Kulet", "Ngalák", "Kuthdêng","Alak", "Agseth", "Lor", "Bomrek"]),
#   random.choice(["Mudminder", "Plankmaster", "Animaster", "Minemaster", "Portal-lord", "Grey Mace", "Lapidist",])
#   )

# print(dw1.name)
# print(dw1.profession)
# print(dw1.happiness)

# dw1.change_job("warrior")

# 2. Dwarf Generator

# Create a function that randomly generates Dwarfs with names, professions, and a happiness level. Store these Dwarfs in a list.

def generate_dwarves(amount_of_dwarves: int) -> list[Dwarf]:
  dwarves: list[Dwarf] = []
  
  # The ':list [Dwarf]' above is another example of types, and it helps to inform both the developer and the program
  # what parameters can be accepted into the parentheses.
  
  for _ in range(amount_of_dwarves):

    # integers are not iterable. In order to allow us to iterate through the list, we can apply the range function.

    name: str = random.choice(["Med", "Kulet", "Ngalák", "Kuthdêng","Alak", "Agseth", "Lor", "Bomrek"])
    profession: str = random.choice(["Mudminder", "Plankmaster", "Animaster", "Minemaster", "Portal-lord", "Grey Mace", "Lapidist"])
    dwarf: Dwarf = Dwarf(name, profession)
    dwarves.append(dwarf)
  
  return dwarves

my_dwarves = generate_dwarves(7)

  #Create a basic simulation of a Dwarf Fortress year. Over the course of the year, Dwarfs' happiness can change - each 
  # month, roll a die for each Dwarf. On a 1 or 2, decrease happiness by eight. On a 5 or 6, increase happiness by eight.

def simulate_year(my_dwarves):
  
  # Define a function to simulate a year, use the generated list of dwarves, in this case called my_dwarves .

  months: list = ["Granite", "Slate", "Felsite", "Hematite", "Malachite", "Galena", "Limestone", "Sandstone", "Timber", "Moonstone", "Opal", "Obsidian"]
  
  # Establish a list for the months of the year.

  for month in months:
    # For loop: for each month in the months list we've just made, do the following:

    print(f"\nSimulating {month}:\n")
    # Helpful indicator of simulation progress.

    for dwarf in my_dwarves:
      roll = random.randint(1,6)
      #For each dwarf in the my_dwarves variable, roll a 1d6. Dependant on the result, alter the happiness level:

      if roll < 3:
        dwarf.happiness -= 8
      
      elif roll > 4:
        dwarf.happiness += 8
      
      dwarf.happiness = max(0, min(100, dwarf.happiness))
      # Notice, when used as a clamping mechanism, max dictates the min value, and min dictates the max.

      if dwarf.happiness < 24:
        dwarf.mood = "miserable"
      elif 24 <= dwarf.happiness <= 49:
        dwarf.mood = "grumpy"
      elif 50 <= dwarf.happiness <= 74:
        dwarf.mood = "cordial"
      else:
        dwarf.mood = "exuberant"

      # For verisimilitude, we have chosen to represent the happiness levels as moods. However, for error-checking reasons, I have included the
      # dwarf.happiness in the print statement so that we can clearly see the increments and decrements.

      print(f"{dwarf.name}, {dwarf.profession} of the {dwarf.guildhall}, is feeling {dwarf.mood} ({dwarf.happiness}) in {month}.")
      # Report to check functionality.

simulate_year(my_dwarves)

# Pass the my_dwarves variable into the simulate_year function.