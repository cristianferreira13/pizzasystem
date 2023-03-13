class Customer:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

class Menu:
    def __init__(self, pizza_items):
        self.pizza_items = pizza_items

    def get_pizza_items(self):
        return self.pizza_items

class PizzaItems:
    def __init__(self, pizza_type, pizza_size, toppings, quantity):
        self.pizza_type = pizza_type
        self.pizza_size = pizza_size
        self.toppings = toppings
        self.quantity = quantity

    def get_pizza_type(self):
        return self.pizza_type

    def get_pizza_size(self):
        return self.pizza_size

    def get_toppings(self):
        return self.toppings

    def get_quantity(self):
        return self.quantity

class PizzaOrder:
    def __init__(self, customer, pizza_items, pickup_delivery):
        self.customer = customer
        self.pizza_items = pizza_items
        self.pickup_delivery = pickup_delivery

    def get_customer(self):
        return self.customer

    def get_pizza_items(self):
        return self.pizza_items

    def get_pickup_delivery(self):
        return self.pickup_delivery

class AddPayment:
    def __init__(self, pizza_order, payment_type, payment_amount):
        self.pizza_order = pizza_order
        self.payment_type = payment_type
        self.payment_amount = payment_amount

    def get_pizza_order(self):
        return self.pizza_order

    def get_payment_type(self):
        return self.payment_type

    def get_payment_amount(self):
        return self.payment_amount

class PickupPizza:
    def __init__(self, pizza_order):
        self.pizza_order = pizza_order

    def get_pizza_order(self):
        return self.pizza_order

class DeliverPizza:
    def __init__(self, pizza_order):
        self.pizza_order = pizza_order

    def get_pizza_order(self):
        return self.pizza_order


# Core Functionality
def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter customer phone number: ")
    address = input("Enter customer address: ")
    return Customer(name, phone, address)

def view_menu():
    print("Here is our menu:")
    print("Pizza Type: Personal pan, Thin crust, Hand tossed, or Deep dish")
    print("Pizza Size: Small, Medium, Large")
    print("Toppings: Cheese, Pepperoni, Sausage, Olives, Green Peppers, Pineapple")
    print("Quantity: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

def add_pizza_items():
    pizza_type = input("What type of pizza would you like? ")
    pizza_size = input("What size of pizza would you like? ")
    toppings = input("What toppings would you like? ")
    quantity = input("How many pizzas would you like? ")
    return PizzaItems(pizza_type, pizza_size, toppings, quantity)

def choose_pickup_delivery():
    choice = input("Would you like to pick up your pizza or have it delivered? ")
    return choice

def view_order_details(customer, pizza_items, pickup_delivery):
    print("Customer Name: " + customer.get_name())
    print("Phone Number: " + customer.get_phone())
    print("Address: " + customer.get_address())
    print("Pizza Type: " + pizza_items.get_pizza_type())
    print("Pizza Size: " + pizza_items.get_pizza_size())
    print("Toppings: " + pizza_items.get_toppings())
    print("Quantity: " + pizza_items.get_quantity())
    print("Pickup or Delivery: " + pickup_delivery)

def get_user_choice():
    confirm = input("Is the order above correct?(Yes/No)")
    if confirm == "Yes":
        print("Your confirmation number is #42069.")
    elif confirm == "No":
        print("Please start over from the beginning.")
    else:
        print("Invalid response")
        return (get_user_choice())
    
def main():
    # User Input
    customer = add_customer()
    view_menu()
    pizza_items = add_pizza_items()
    pickup_delivery = choose_pickup_delivery()

    # Core Functionality
    pizza_order = PizzaOrder(customer, pizza_items, pickup_delivery)
    view_order_details(customer, pizza_items, pickup_delivery)
    get_user_choice()
    
main()