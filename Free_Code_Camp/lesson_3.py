# Has is used for comments.

# print("Jordan")

# Above is a print function. However, if you will need to print the same thing many times, you can use a variable for efficiency. 

# name = "Jordan"
# age = "29"

# print(name + " is " + age + " years old.")

# We can use underscore to have multi-word names for variables. This is called Snake-Case and is usually all lower case.

# full_name = "Jordan Doyle"

# print(full_name)

# # We can also set multiple values to a variable at once:

# width, height = 5, 10
# print(width)
# print (height)

# your_name = input("Please enter your name: ")

# print(your_name)

# Tip Calculator App

# food_amount = float(input("\nHow much did your food cost? \n£"))
# tip_percent = float(input("What percent would you like to tip by?\n"))
# tip_amount = int(food_amount*(tip_percent/100))
# total = (food_amount + tip_amount)
# print("*****************************************************\nAt £" + str(food_amount) + " your tip will be £" + str(tip_amount) + " for a total of £" + str(total) + ".\n*****************************************************")

# Consider the expression 4 + 5 = 9. Here, 4 and 5 are operands, whilst the construct that manipulates them (+) is called the operator.

# Now, we're making a little weather app.

# The app will advise us to take an umbrella out if it's raining, otherwise to get our sunglasses.

# weather = input("What is the weather outside right now? ")

# if weather == "rain":
#     print("Get under your umbrella ella ella, ay ay.")
# else:
#     print("Sunglasses for the masses!")

# It is important to remember that = is an assignment operator, but == is a comparison operator. 

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

#def name_2(name="Friend", greeting="Heya,"):
  #print(f"{greeting} {name}!")
'''
  The defined name_2 function will accept two arguments, name and greeting, which it will then use to greet the user. 

  The assigned values in the function's code are called default arguments, and they will allow the code to proceed even if the user doesn't fill in the parameters themselves
  whilst calling the function.

  >>> name_2(Jordan)
  "Heya, Jordan!"
  '''

# name_2(greeting = "Hiya, ", name = "Jordan!")

# The arguments above are called named arguments. These are distinct from positional arguments, which use the position of the variable in the function:

# name_2("Jordan", "Hello")

# Return in a function

# def sum(a, b):
#     return a+b

# num = sum(4, 12)
 
# print(num)

# Tip Calculator App

# food_amount = float(input("\nHow much did your food cost? \n£"))
# tip_percent = float(input("What percent would you like to tip by?\n"))
# tip_amount = int(food_amount*(tip_percent/100))
# total = (food_amount + tip_amount)
# print("*****************************************************\nAt £" + str(food_amount) + " your tip will be £" + str(tip_amount) + " for a total of £" + str(total) + ".\n*****************************************************")

def tip_calc(food = float(input("\nHow much did your food cost? \n£")), tip_percent = float(input("What percent would you like to tip by?\n"))):
    tip = int(food * (tip_percent / 100))
    total = (food + tip)
    print(f"*****************************************************\nYour food and tip come to a total of £{total}.\n*****************************************************")

tip_calc(100, 10)