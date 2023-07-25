# Tasks

## 1. Dwarf Class Definition

Create a Dwarf class. Each Dwarf should have a name, profession, and a happiness level. Allow these to be set during initialization and retrieved via methods. For extra complexity, add a method that allows you to change a Dwarf's profession.

```py
class Dwarf:
    def __init__(self, name, profession, happiness):
        self.name = name
        self.profession = profession
        self.happiness = happiness

    def get_info(self):
        return self.name, self.profession, self.happiness

    def change_profession(self, new_profession):
        self.profession = new_profession
```

## 2. Dwarf Generator

Create a function that randomly generates Dwarfs with names, professions, and a happiness level. Store these Dwarfs in a list.

```py
import random

names = ['Urist', 'Zan', 'Meng', 'Datan', 'Logem', 'Rith', 'Sibrek']
professions = ['Miner', 'Woodworker', 'Stonecrafter', 'Jeweler', 'Metalsmith', 'Brewer', 'Farmer']

def generate_dwarfs(n):
    dwarfs = []
    for _ in range(n):
        name = random.choice(names)
        profession = random.choice(professions)
        happiness = random.randint(1, 10)
        dwarfs.append(Dwarf(name, profession, happiness))
    return dwarfs
```

## 3. Simulate a year

Create a basic simulation of a Dwarf Fortress year. Over the course of the year, Dwarfs' happiness can change - each month, roll a die for each Dwarf. On a 1 or 2, decrease happiness by one. On a 5 or 6, increase happiness by one.

```py
def simulate_year(dwarfs):
    for _ in range(12):
        for dwarf in dwarfs:
            roll = random.randint(1, 6)
            if roll in [1, 2] and dwarf.happiness > 1:
                dwarf.happiness -= 1
            elif roll in [5, 6] and dwarf.happiness < 10:
                dwarf.happiness += 1
```

## 4. Annual Report

At the end of the year, print a report of your Dwarfs - their names, professions, and happiness levels.

```py
def print_report(dwarfs):
    print("Annual Dwarf Report:")
    for dwarf in dwarfs:
        print(f"Name: {dwarf.name}, Profession: {dwarf.profession}, Happiness: {dwarf.happiness}")
```

## 5. Dwarf Fortress Game

Put it all together. Generate a list of Dwarfs, simulate a year, then print a report.

```py
def play_game():
    dwarfs = generate_dwarfs(7)
    simulate_year(dwarfs)
    print_report(dwarfs)

play_game()
```
