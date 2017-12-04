shopping_list = ["milk", "pasta", "eggs", "bread", "rice", #spam
                 ]
nasty_food_item = ''
for item in shopping_list:
    if item == "spam":
        #continue
        nasty_food_item = item
        break
else:
    print("I'll enjoy the food that has no spam")

if nasty_food_item:
    print("Can't I have anything without spam in it")
