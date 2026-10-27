from EK_lesson06 import coffee
from EK_lesson06 import coffee_machine


def main():

    running = True
    machine = coffee_machine.CoffeeMachine()

    orders = []

    while running:
        print("")
        print("This is Helen's coffee machine")
        print("1. Order mew coffee")
        print("2. See list of previous coffee orders")
        print("3. Change the last coffee order")
        print("4. Delete the last coffee order")
        print("0. Exit")

        choice = input("Which choice would you like to make?  ")

        match choice:
            case "1":
                machine.take_order()

            case "2":
                machine.list_orders()

            case "3":
                machine.update_order()

            case "4":
                machine.delete_order()

            case "0":
                machine.save_orders()
                print("Exiting...")
                running = False

            case _:
                print("Invalid choice")


main()


