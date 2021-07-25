print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')

menu = {
    "Appetizers": [
        "Wings",
        "Cookies",
        "Spring Rolls",
    ],
    "Entrees": [
        "Salmon",
        "Steak",
        "Meat Tornado",
        "A Literal Garden",
    ],
    "Desserts": [
        "Ice Cream",
        "Cake",
        "Pie",
    ],
    "Drinks": [
        "Coffee",
        "Tea",
        "Unicorn Tears",
    ],

}

print('\nAppetizers \n', '----------')
for i in menu["Appetizers"]:
    print(i)
print('\nEntrees \n', '----------')
for i in menu["Entrees"]:
    print(i)
print('\nDesserts \n', '----------')
for i in menu["Desserts"]:
    print(i)
print('\nDrinks \n', '----------')
for i in menu["Drinks"]:
    print(i)

print('\n \n***********************************')
print('** What would you like to order? **')
print('***********************************')

order = input('>')


def make_order(order):

    orders = []
    while order != 'quit':
        orders.append(order)
        if order in orders:
            count = orders.count(order)
            print(f'** {count} order of {order} have been added to your meal **')
        else:
            count = 1
            print(f'** {count} order of {order} have been added to your meal **')
        order = input('>')


make_order(order)
