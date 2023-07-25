# The lesson seems to discuss a lot of different specific functions and how they can be implemented in lists.

dwarves = ["Uthar", "Areb", "Momuz", "Moldath", "Olin", "Olon", "Lor"]

# The above is an example of a list in python.

dwarves.sort()

# This is an example of a list having one of the in-built python functions applied to it. In this case, the list will be sorted into ascending order.
# Similarly, if we had a list of numbers and applied the same sort function to it, we would have a list in descending order. 

# print (dwarves) {Put into notes to declutter terminal}.

# A tuple is a container where we can store different values. It is similar to a list, but it has a few key differences. A good example of a tuple is co-ordinates.

coordinates = (4, 5) # So this is a co-ordinate and also a tuple. An important thing to note is that tuples are immutable once they are set.

# print(coordinates[0]) # This will return 4 in the print statement. {Put into notes to declutter terminal}.

# The main difference between lists and tuples is that lists are mutable and tuples aren't. However, you *can* make a list of tuples.

#Functions - A function is, in simple terms, a collection of code that performs a specific task. Consequently, calling functions are extremely helpful 
# for efficient coding. In Python, we create functions as follows:

def say_hi(name, age): 
    print("Hello " + name + ", you are " + str(age) + " years old!")

# Note: Python code must be indented, anything outside the indent will not be included in the function.

# say_hi("Jordan", "29") {Put into notes to declutter terminal}.

# Functions can also be passed parameters - a piece of information provided for the function to use. This is done above. You can have multiple parameters. See above.
# Sometimes when we call a function we want information to be communicated from the task. This is the use of the return function.

def cube(num):
    return num*num*num
    
result = cube(25)
# print(result) {Put in notes to declutter terminal.}

# It is important to note that no code can be included in a function after the line of code with the return statement. Also, return statements can print any 
# data type.

# Dwarf is in the tavern 
# if dwarf is hungry and thirsty 
#    dwarf takes a minced meal and an alcoholic beverage 
# otherwise if dwarf is thirsty
#     dwarf takes alcoholic beverage
# otherwise if dwarf is both
#     dwarf takes minced meal 

in_tavern = True
is_hungry = False
is_thirsty = False

# {Put into notes to declutter terminal.}if in_tavern:
#     print("The dwarf is in the tavern.")
# else:
#     print("The dwarf isn't in the tavern.")

# {Put into notes to declutter terminal.}if in_tavern and is_hungry and is_thirsty:
#     print("The dwarf digs into a minced meal and a goblet of grog.")
# elif in_tavern and is_hungry and not is_thirsty:
#     print("The dwarf digs into a minced meal.")
# elif in_tavern and is_thirsty and not is_hungry:
#     print("The dwarf grabs a goblet of grog.")
# elif in_tavern and not is_hungry and not is_thirsty:
#     print("The dwarf declines libation AND victuals. Beware! They might be a vampire.")

# Comparisons can be made inside if statements. 

def oldest_dwarf(age1, age2, age3):
    if age1 >= age2 and age1 >=age3:
        return age1
    elif age2 >= age1 and age2 >= age3:
        return age2
    else:
        return age3
    
# {Put into notes to declutter terminal.} print(oldest_dwarf(56, 174, 122))

# There are many comparison operators, including == which means equal to. Also: <= (less than or equal to), >= (greater than or equal to), != (not equal to).

#Calculator attempt

# {Put into notes to declutter terminal.} number1 = float(input("Enter first number:"))
# op = (input("Enter the operator:"))
# number2 = float(input("Enter second number:"))

# {Put into notes to declutter terminal.}if op == "+":
#     print(number1+number2)
# elif op == "/":
#     print(number1/number2)
# elif op == "*":
#     print(number2*number1)
# elif op == "-":
#     print(number1-number2)
# else:
#     print("Invalid operator!")

# Dictionaries!

# A dictionary is a structure in python that allows us to store information in *key value pairs*. When the dev wants to access a specific piece of info in the dictionary
# we can refer to that information using the key value paired with that information. In physical dictionaries, the lexeme is the key that refers to the information
# which is the denotation in this analogy.
# 
# First, we name the dictionary, and then we open curly brackets. 

# {Put into notes to declutter terminal.} monthConversions = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
#     "Apr" : "April",
#     "May" : "May",
#     "Jun" : "June",
#     "Jul" : "July",
#     "Aug" : "August",
#     "Sep" : "September",
#     "Oct" : "October",
#     "Nov" : "November",
#     "Dec" : "December",
# }

# print(monthConversions["Oct"]) is one way to attain the paired information. Another way is to do the following:

# {Put into notes to declutter terminal.} print(monthConversions.get("Don", "Invalid Key"))

# While Loops

# A while loop is a structure that allows program to loop, executing a block of code multiple times, until a certain condition is false. 
# The loop condition, which is also sometimes the loop guard, provides the value which must be true for the code to execute another loop.

# {Put into notes to declutter terminal.}i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# The shorthand for variable plus an increment of 1 is v += 1, where v is variable.

# {Put into notes to declutter terminal.} print("Done with loop!")

# Guessing game!

secret_word = "bacon"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess (HINT: the word is a popular breakfast meat):")
        guess_count += 1
    else: 
        out_of_guesses = True
    
if out_of_guesses: 
    print("La-hoo-sa-her! Better luck next time.")
else: 
    print("You got it! Congratulations!")
