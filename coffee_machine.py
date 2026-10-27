from EK_lesson06 import coffee
import datetime

class CoffeeMachine:
    def __init__(self):
        self.__orders = []

    def __choose_from(self, options, prompt): # builds menus and prompts based on the coffee choices
        items = list(options)
        print(prompt)
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item.value}")
        while True:
            choice = input("Please choose a number:  ")
            try:
                if int(choice) < 1:
                    raise IndexError
                return items[int(choice) - 1]
            except IndexError:
                print("Please choose a number between 1 and", len(items))
            except ValueError:
                print("Invalid choice. Please choose a number between 1 and", len(items))

    def __build_order(self, order_name=None): #default value for order_name is None, otherwise it can be passed
        if order_name is None:
            order_name = str(input("Please give me your name:  ")) # input name

        order_time = datetime.datetime.now()  # get date

        # run the coffee menus and prompts
        coffee_type = self.__choose_from(coffee.CoffeeType, "What kind of coffee would you like?")
        coffee_size = self.__choose_from(coffee.CoffeeSize, "What size cup would you like?")
        cream_type = self.__choose_from(coffee.CoffeeCream, "Would you like cream in your coffee?")

        return coffee.Coffee(order_name, order_time, coffee_type.value, coffee_size.value, cream_type.value)


    def print_last_order(self):
        # print out the coffee order for confirmation
        print(f"{self.__orders[-1].get_name()}, you are ordering a {self.__orders[-1].get_size().lower()} {self.__orders[-1].get_coffee_type().lower()} {self.__orders[-1].get_cream().lower()}.")

    def take_order(self):
        #  append to orders list
        self.__orders.append(self.__build_order())
        self.print_last_order()



    def list_orders(self):
        if not self.__orders:
            print("No orders yet")
            return
        for o in self.__orders:
            print(o.get_name(), o.get_time(), o.get_coffee_type(), o.get_size(), o.get_cream())

    def update_order(self):
        try:
            self.__orders[-1] = self.__build_order(self.__orders[-1].get_name())
            self.print_last_order()
        except IndexError:
            print("No orders to update") # if list is empty



    def delete_order(self):
        try:
            removed = self.__orders.pop()
            print("Deleted order for", removed.get_name())
        except IndexError:
            print("No orders to delete")

    def save_orders(self):
        if not self.__orders: # if the orders list is empty
            print("No orders to save")
            return
        filename = datetime.datetime.now().strftime("saved_orders/orders_%Y%m%d_%H%M%S.txt")
        with open(filename, "w") as f:
            for o in self.__orders:
                f.write(f"{o.get_name()};{o.get_time()};{o.get_coffee_type()};{o.get_size()};{o.get_cream()}\n")
        print("Orders saved to", filename)