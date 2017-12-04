name = input("Please enter your name : ")
age = int(input("How old are you, {}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {} year(s)".format(18-age))