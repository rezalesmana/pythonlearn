name = input("What is your name? ")
age = int(input("How old are you, {}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to 18-30 holiday, {}!".format(name))
else:
    print("I'm sorry, you're not allowed to go to 18-31 holiday right now, {}.".format(name))