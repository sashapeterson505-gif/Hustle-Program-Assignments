# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Sasha Peterson
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Snacks and Drinks
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.


class Snack:
    def __init__(self, name, price, flavor):
        self.name = name
        self.price = price
        self.flavor = flavor

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price:.2f}, "{self.flavor}")'

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative.")
        else:
            self.price = price

    def deliver(self):
        return f"Delivering {self.name} ({self.flavor})"

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: it'll print "no price cant be negative"
#   Paste the message you see here: price cannot be negative


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.

class Drink:
    def __init__(self, name, price, size, brand):
        self.brand = brand
        self.name = name
        self.price = price
        self.size = size

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price:.2f}, "{self.size}", "{self.brand}")'

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative.")
        else:
            self.price = price

    def deliver(self):
        return f"Delivering {self.name} ({self.size})"


# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: objects of the different classes respond to the same method in their own way just with different names 

# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: item1 = Cookie("Oatmeal Cookie", 1.50, "oatmeal", "cookie")

class Candy(Snack):
    def __init__(self, name, price, flavor, snack_type):
        super().__init__(name, price, flavor)
        self.snack_type = snack_type

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price:.2f}, "{self.flavor}", "{self.snack_type}")'

    def deliver(self):
        return f"Delivering {self.name} ({self.snack_type})"
    
class Soda(Drink):
    def __init__(self, name, price, size, brand):
        super().__init__(name, price, size, brand)
        self.brand = brand

    def deliver(self):
        return f"Delivering {self.name} ({self.brand})"

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Cookie(Snack):
    def __init__(self, name, price, flavor, snack_type):
        super().__init__(name, price, flavor)
        self.snack_type = snack_type

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price:.2f}, "{self.flavor}", "{self.snack_type}")'

    def deliver(self):
        return f"Delivering {self.name} ({self.snack_type})"

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to the cart")
        print("Items in cart:", self.items)

    def checkout(self):
        total = sum(item.get_price() for item in self.items)
        return total


# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.


# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.

class IceCream(Snack):
    def __init__(self, name, price, flavor, type):
        super().__init__(name, price, flavor)
        self.type = type

    def deliver(self):
        return f"Delivering {self.name} ({self.type})"

    def __str__(self):
        return f"{self.name} - ${self.price}"

menu = {
    1: Cookie("Oatmeal Cookie", 1.50, "oatmeal", "cookie"),
    2: Candy("Gummy Bears", 1.25, "strawberry", "gummy"),
    3: Soda("Cola", 1.75, "medium", "Coca-Cola"),
    4: IceCream("Vanilla", 2.50, "vanilla", "scoop")
}

cart = Cart()

print("Menu:", menu)
print("Cart:", cart.items)

selected_item_number = int(input("Enter the number of the item you want to add to the cart: "))

if selected_item_number in menu:
    cart.add_item(menu[selected_item_number])
else:
    print("item not found in menu.") 


# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: it will keep asking for input because its a loop

print("welcome to the store! enter the number of the item you want to add to the cart or 'done' to finish shopping:")

while True: 
    choice = input("Enter ur choice (number, or 'done'): ")

    if choice == 'done':
        break
    elif choice.isdigit():
        selected_item_number = int(choice)
        if selected_item_number in menu:
            cart.add_item(menu[selected_item_number])
        else:
            print("item not found in menu.") 
    else:
        print("Invalid input.")

# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.

# PREDICT: the full output is 
# Menu: {1: Cookie("Oatmeal Cookie", 1.50, "oatmeal", "cookie"), 2: Candy("Gummy Bears", 1.25, "strawberry", "gummy"), 3: Soda("Cola", 1.75, "medium", "Coca-Cola")}
# Cart: []
# Enter the number of the item you want to add to the cart: 1
# Added Oatmeal Cookie to the cart
# Items in cart: [Cookie("Oatmeal Cookie", 1.50, "oatmeal", "cookie")]

# EXPLANATION: soo i was completely wrong in my prediction, the actual output: 
#Menu: {1: <__main__.Cookie object at 0x10b800c20>, 2: <__main__.Candy object at 0x10b801160>, 3: <__main__.Soda object at 0x10b8a86e0>}
#Cart: []
#Enter the number of the item you want to add to the cart: 2
#Added Gummy Bears to the cart
#Items in cart: [<__main__.Candy object at 0x10b801160>]
#welcome to the store! enter the number of the item you want to add to the cart or 'done' to finish shopping:
#Enter ur choice (number, or 'done'): 2
#Added Gummy Bears to the cart
#Items in cart: [<__main__.Candy object at 0x10b801160>, <__main__.Candy object at 0x10b801160>]
#Enter ur choice (number, or 'done'): 1
#Added Oatmeal Cookie to the cart
#Items in cart: [<__main__.Candy object at 0x10b801160>, <__main__.Candy object at 0x10b801160>, <__main__.Cookie object at 0x10b800c20>]
#Enter ur choice (number, or 'done'): 1
#Added Oatmeal Cookie to the cart
#Items in cart: [<__main__.Candy object at 0x10b801160>, <__main__.Candy object at 0x10b801160>, <__main__.Cookie object at 0x10b800c20>, <__main__.Cookie object at 0x10b800c20>]
#Enter ur choice (number, or 'done'): done

# i did this completly wrong.. i dont know where i went wrong because my code is running without any problems or erros
# i fixxed it with the help of ai, my print menu printed the whole dictionary, and the same for the cart


# EXPLANATION 2:
#Menu: {1: Cookie("Oatmeal Cookie", 1.50, "oatmeal", "cookie"), 2: Candy("Gummy Bears", 1.25, "strawberry", "gummy"), 3: Soda("Cola", 1.75, "medium", "Coca-Cola"), 4: IceCream("Vanilla", 2.50, "vanilla")}
#Cart: []
#Enter the number of the item you want to add to the cart: 1
#Added Oatmeal Cookie to the cart
#Items in cart: [Cookie("Oatmeal Cookie", 1.50, "oatmeal", "cookie")]
#welcome to the store! enter the number of the item you want to add to the cart or 'done' to finish shopping:
#Enter ur choice (number, or 'done'): 4
#Added Vanilla to the cart
#Items in cart: [Cookie("Oatmeal Cookie", 1.50, "oatmeal", "cookie"), IceCream("Vanilla", 2.50, "vanilla")]
#Enter ur choice (number, or 'done'): done


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================

# added icecream to the menu 