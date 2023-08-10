# Make a class called character.
# you should initialise it with name, race and role and a step counter

class Character:
  def __init__(self, name, race, role):
    # when you initialise a character, you MUST provide a name, a race and a role
    self.name = name
    # these must be provided at character creation
    self.race = race
    self.role = role
    # when a new character is initialised, they have a step_counter at 0
    self.step_counter = 0
    # this does not have to be provided at character creation

  # method
  def speak(self, words):
    print(f"{self.name} says, '{words}'")
      
  # method
  def walk(self):
    self.step_counter += 1
    print(f"{self.name} has walked {self.step_counter} step(s) so far!")

class Wizard(Character):
  # initialise a wizard with everything it inherits from the super-class (character) and the wizard class
  def __init__(self, name, race, role, spell):
    # initialise the super class with the values, too
    # hey, character class, here is the parameters you need
    super().__init__(name, race, role)
    self.spell = spell

  def cast_spell(self):
    print(f"{self.name} casts the spell: {self.spell}.")

class Ranger(Character):
  def __init__(self, name, race, role, ability):
    super().__init__(name, race, role)
    self.ability = ability
  
  def use_ability(self):
    print(f"{self.name} uses {self.ability}.")

class Shepherd(Character):
  def __init__(self, name, race, role, language):
    super().__init__(name, race, role)
    self.language = language
	
  def speak_language(self):
      print(f"{self.name} speaks {self.language}")

# TODO: look up object oriented code to learn more about this pattern of constructors

class Inventory:
  def __init__(self, character):
    # this named parameter is required
    self.character = character

    # this is initialised with a set value
    self.items = []
    self.carrying_capacity = 10

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    self.items.remove(item)

  def display_inventory(self):
    print(f"{self.character.name}'s Inventory contains: ")
    for item in self.items:
      print(item)

# as this method sees it, what does self.character object look like

# aragorn {
#   name: "Aragorn",
#   role: "Ranger",
#   race: "Numenorian",
#   inventory: {
#    items: []
#   }
# }

# self.character

aragorn = Ranger("Aragorn", "Numenorian", "Ranger", "Tracking")
treebeard = Shepherd("Fangorn", "Ent", "Shepherd", "Entish")
radagast = Wizard("Radagast the Brown", "Istar", "Protector", "Speak to Animals")

aragorn.speak("Not nearly frightened enough.")
aragorn.walk()
aragorn.walk()
aragorn.inventory = Inventory(aragorn)
aragorn.inventory.add_item("Elven Rope")
aragorn.inventory.display_inventory()
aragorn.use_ability()
treebeard.speak("I am no tree! I am an ent.")
treebeard.walk()
treebeard.inventory = Inventory(treebeard)
treebeard.inventory.add_item("Basin of magic water")
treebeard.inventory.display_inventory()
treebeard.speak_language()
radagast.speak("It's not as though it's black magic!")
radagast.walk()
radagast.inventory = Inventory(radagast)
radagast.inventory.add_item("Sebastian, the pet hedgehog")
radagast.inventory.display_inventory()
radagast.cast_spell()