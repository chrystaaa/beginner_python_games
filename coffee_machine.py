class CoffeeMachine:
    def __init__(self):
        # How much water, milk, and coffee the machine has
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

        # Drinks we can make, and what each one needs
        self.menu = {
            "espresso": {
                "ingredients": {"water": 50, "coffee": 18},
                "cost": 1.5
            },
            "latte": {
                "ingredients": {"water": 200, "milk": 150, "coffee": 24},
                "cost": 2.5
            },
            "cappuccino": {
                "ingredients": {"water": 250, "milk": 100, "coffee": 24},
                "cost": 3.0
            }
        }

        # Money earned so far
        self.money = 0.0

    # This shows how much stuff the machine has and how much money it made
    def show_report(self):
        print("\n-- MACHINE REPORT --")
        print("Water:", self.resources["water"], "ml")
        print("Milk:", self.resources["milk"], "ml")
        print("Coffee:", self.resources["coffee"], "g")
        print("Money: $", self.money)
        print()

    # Function to check if we have enough ingredients to make the drink
    def check_ingredients(self, ingredients_needed):
        for item in ingredients_needed:
            if ingredients_needed[item] > self.resources[item]:
                print("Sorry, not enough", item)
                return False
        return True

    # This lets the user put in coins and pays for the drink or refunds the costumer if the money dont cover the cost of the coffee
    def take_payment(self, drink_cost):
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickels = int(input("How many nickels? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01
            total_money = quarters + dimes + nickels + pennies
        except:
            print("Oops! You entered something wrong.")
            return False

        if total_money < drink_cost:
            print("Sorry, that’s not enough money. Refunding...")
            return False
        else:
            change = round(total_money - drink_cost, 2)
            if change > 0:
                print("Here’s your change: $", change)
            self.money += drink_cost
            return True

    # This takes ingredients out of the machine and gives the coffee
    def make_drink(self, name, ingredients):
        for item in ingredients:
            self.resources[item] -= ingredients[item]
        print("Here's your", name, ". Enjoy!\n")

    # This runs the machine
    def run(self):
        is_running = True
        print("Welcome to the Coffee Machine!\n")

        while is_running:
            # Prints the main menu
            print("Please choose an option:")
            print("1. Make coffee")
            print("2. Check ingredients")
            print("3. Turn off the machine")

            user_input = input("Enter 1, 2 or 3: ").strip()

            if user_input == "1":
                print("\nAvailable drinks: espresso, latte, cappuccino")
                choice = input("What would you like? ").lower()

                if choice in self.menu:
                    drink = self.menu[choice]
                    ingredients = drink["ingredients"]
                    price = drink["cost"]

                    if self.check_ingredients(ingredients):
                        if self.take_payment(price):
                            self.make_drink(choice, ingredients)
                else:
                    print("That’s not a valid drink option.\n")

            elif user_input == "2":
                self.show_report()

            elif user_input == "3":
                print("Turning off the machine. Goodbye!")
                is_running = False

            else:
                print("Invalid choice. Please type 1, 2, or 3.\n")

machine = CoffeeMachine()
machine.run()
