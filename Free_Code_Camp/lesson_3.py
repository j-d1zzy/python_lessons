#### Lesson 3! #### 

'''Reminder of the BASICS

1.  COMMENTARY
    Hash is used for comments.

2.  PRINT FUNCTIONS
    print("Jordan") 
    This is a print function. However, if you will need to print the same thing many times, you can use a variable for efficiency. 

3.  VARIABLES
    name = "Jordan"
    age = "29"

    We can use underscore to have multi-word names for variables. This is called Snake-Case and is usually all lower case. For instance:

    full_name = "Jordan Doyle"

    We can also set multiple values to a variable at once:

    width, height = 5, 10
    print(width)
    print (height)

4.  FUNCTIONS can accept variables we set as arguments, including those writen in Snake Case. See below:
    
    print(name + " is " + age + " years old.")

    print(full_name)

    your_name = input("Please enter your name: ")

    print(your_name)

    The assigned values in the function's code are called DEFAULT arguments, and they will allow the code to proceed even if the user doesn't 
    fill in the parameters themselves whilst calling the function.

5.  OPERATORS and OPERANDS
    Consider the expression 4 + 5 = 9. Here, 4 and 5 are operands, whilst the construct that manipulates them (+) is called the operator.

    It is important to remember that = is an assignment operator, but == is a comparison operator. 
'''


'''Tip Calculator App

food_amount = float(input("\nHow much did your food cost? \n£"))
tip_percent = float(input("What percent would you like to tip by?\n"))
tip_amount = int(food_amount*(tip_percent/100))
total = (food_amount + tip_amount)
print("*****************************************************\nAt £" + str(food_amount) + " your tip will be £" + str(tip_amount) + " for a total of £" + str(total) + ".\n*****************************************************")
'''


'''Mini Weather App

The app will advise us to take an umbrella out if it's raining, otherwise to get our sunglasses.

weather = input("What is the weather outside right now? ")

if weather == "rain":
    print("Get under your umbrella ella ella, ay ay.")
else:
    print("Sunglasses for the masses!")

# Pythonic Code:

# score = 59
# if score >= 60 and score <= 100:
#     print("Pass.")
# if 60 <= score <= 100:
#     print("Pass.")
# This second if function is considered to be more pythonic than the first if function, because it is more compact. 
# else:
#     print("You failed.")

# def say_my_name():
#     print("Hi Jordan.")

# This code alone will not print anything because the function has not been called. 

# say_my_name()

# Once the function is called, by putting the parentheses at the end, it will run the function. It allows us to run big chunks of code once.
# To increase the dynamism of the functions that we're using, we're going to use a variable instead of a string. In this case, we have provided a parameter to the function.

# def name_2(name="Friend", greeting="Heya,"):
#   print(f"{greeting} {name}!")
# '''

#   The defined name_2 function will accept two arguments, name and greeting, which it will then use to greet the user. 

#   >>> name_2(Jordan)
#   "Heya, Jordan!"
#   '''

# name_2(greeting = "Hiya, ", name = "Jordan!")

# The arguments above are called named arguments. These are distinct from positional arguments, which use the position of the variable in the function:

# name_2("Jordan", "Hello")

# Return in a function

# def sum(a, b):
#     return a+b

# num = sum(4, 12)
 
# print(num)

#### Tip Calculator App ####

'''food_amount = float(input("\nHow much did your food cost? \n£"))
tip_percent = float(input("What percent would you like to tip by?\n"))
tip_amount = int(food_amount*(tip_percent/100))
total = (food_amount + tip_amount)
print("*****************************************************\nAt £" + str(food_amount) + " your tip will be £" + str(tip_amount) + " for a total of £" + str(total) + ".\n*****************************************************")'''

# def tip_calc(
#       food = float(input("\nHow much did your food cost? \n£")), 
#       tip_percent = float(input("What percent would you like to tip by?\n"))):
    
#     tip = int(food * (tip_percent / 100))
    
#     total = (food + tip)
#     print(
#        f"*****************************************************\nYour food and tip come to a total of £{total}.\n*****************************************************")

# tip_calc(100, 10)

# There is a technique called hinting, which combines coding and commenting. For example:
# def weather_to_instruction(weather: str) -> None:
#   ''' The ': str' beside 'weather' is one of these hints, telling the reader that weather must be a string, or, as in the case of '-> None', 
#   that the function shouldn't return anything.'''
#   if weather == 'rain':
#     print("Umbrella time!")

#### Bigger Guy Exercise ####
'''Write a function bigger_guy that takes in two numbers and returns the bigger one.'''

# def bigger_guy(a: float, b: float):
#     if a == b:
#        print("These two values are equal.")
#        quit()
#        '''Without the inclusion of the quit() function here, we immediately run into rather serious issues. Firstly, if 0, 0 is given as the
#        actual parameters for the formal arguments, you will run into behaviours such as the printing of None in the console because the program
#        has not been instructed to stop. Following the logic of the program, the function will next compare the size of a and b and try to 
#        return the result; however, returning nothing will return 'None' in the console. Therefore, to avoid this, we must quit the program when 
#        0 is passed to the function for both active parameters. 
       
#        Moreover, for this function, the order of the code is essential to its function. As a data type, 0 does not seem to class as a float.
#        We know this because when the if statement immediately above is swapped with the elif statement immediately above, 0, 0 is recognised
#        as true by the program for not being a float, which causes the program to print("Invalid entry...") and quit(), which is wrong, as 
#        most users will consider 0 a number. 0 is likely a common cause of errors. Be mindful of this.'''
#     elif a is not float or b is not float:
#        print("Invalid entry. Please enter numbers.")
#        quit()
#        '''This else if function protects against the inclusion of inappropriate parameters. This is essential because strings can actually be
#        assessed in a greater than or less than operators, in the case of single letters. The program will assess the letters in terms of 
#        alphabetical position, therefore it will not cause an error and will return a letter - which is not what we want for this program.'''
#     elif a < b:
#       return b
#     else:
#       return a
# print(bigger_guy("H", "d"))