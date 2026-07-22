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

# Snack is one type of item sold in the store.
class Snack:
    def __init__(self, name, price, flavor):
        self.name = name
        self.price = price
        self.flavor = flavor

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative.")
        else:
            self.price = price

    def deliver(self):
        return f"Delivering {self.name} ({self.flavor})"


# Drink is another type of item sold in the store.
class Drink:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative.")
        else:
            self.price = price

    def deliver(self):
        return f"Delivering {self.name} ({self.size})"


# ============================================================
# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
# ============================================================

# Candy inherits from Snack and adds a snack_type attribute.
class Candy(Snack):
    def __init__(self, name, price, flavor, snack_type):
        super().__init__(name, price, flavor)
        self.snack_type = snack_type

    def deliver(self):
        return f"Delivering {self.name} ({self.snack_type})"


# Cookie inherits from Snack and adds a snack_type attribute.
class Cookie(Snack):
    def __init__(self, name, price, flavor, snack_type):
        super().__init__(name, price, flavor)
        self.snack_type = snack_type

    def deliver(self):
        return f"Delivering {self.name} ({self.snack_type})"


# Soda inherits from Drink and adds a brand attribute.
class Soda(Drink):
    def __init__(self, name, price, size, brand):
        super().__init__(name, price, size)
        self.brand = brand

    def deliver(self):
        return f"Delivering {self.name} ({self.brand})"


# Juice inherits from Drink and adds a flavor attribute.
class Juice(Drink):
    def __init__(self, name, price, size, flavor):
        super().__init__(name, price, size)
        self.flavor = flavor

    def deliver(self):
        return f"Delivering {self.name} ({self.flavor})"


# ============================================================
# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
# ============================================================

# Create sample snacks and drinks for the store.
snack1_cookie = Cookie("Cookie", 1.50, "chocolate chip", "oatmeal")
snack2_candy = Candy("Candy", 1.25, "strawberry", "gummy")
snack3_chips = Snack("Chips", 2.50, "salted")

drink1_soda = Soda("Cola", 1.75, "medium", "Coca-Cola")
drink2_juice = Juice("Orange Juice", 2.00, "small", "orange")
drink3_water = Drink("Water", 1.00, "small")


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# Add store inventory, order logic, and checkout functions below.


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================