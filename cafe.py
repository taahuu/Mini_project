def greet(name):
    print(f"Hello {name}, please enjoy your day")

name=input("Dear Customer please Enter your name : ").title()

greet(name)

Menu={
    "Coffee":110,
    "Burger":150,
    'Pizza':180,
    'Cold Coffee':150
}
print('''"Coffee":110,
"Burger":150,
'Pizza':180,
'Cold Coffee':150''')
amt=0
i=1
t=True
while t:
    item_1=input(f"Order Your Dish No {i}: ").title()
    if item_1 =='N':
        break

    if item_1 not in Menu:
        print("This is not available")
        item_1=input(f"Please order another dish: ")
    else:
        amt+=Menu[item_1]
        i+=1
print(f"Your Total Amount is {amt}")
print(f"Have a Good Meal , {name} \nPlease visit Again")