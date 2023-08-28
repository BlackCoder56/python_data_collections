# Food dictionary
# It is storing all the food items names and their prices
# which will be used in the project
products = {
    "1": {
        "name": "Chips Plain",
        "price": 10000
    },
    "2": {
        "name": "Fried Chicken",
        "price": 6000
    },
    "3": {
        "name": "Matooke & Chicken stew",
        "price": 8000
    },
    "4": {
        "name": "Matooke & Beef",
        "price": 7000
    },
    "5": {
        "name": "Rice & chicken stew",
        "price": 8000
    },
    "6": {
        "name": "Rice & Beef",
        "price": 7500
    }
}
# drinks dictionary
drink_products = {
    "1": { 
        "name": "Fanta",
        "price": 2000
    },
    "2": {
        "name": "Pepsi",
        "price": 2000
    },
    "3": {
        "name": "Coca cola",
        "price": 2000
    },
    "4": {
        "name": "Mirinda",
        "price": 2000
    },
    "5": {
        "name": "Rwenzori",
        "price": 2000
    },
    "6": {
        "name": "Minute Maid",
        "price": 3000
    }
}


def display_menu():
    try:
        """
        This is the menu UI design!
        """
        print("|-----------------Menu---------------------|")
        print("|  opt  Food Item                  Price   |")
        print(
            "| - 1. " + products["1"]["name"] + "              ugx." + str(products["1"]["price"]) + "  |")
        print("| - 2. " + products["2"]["name"] + "            ugx." + str(products["2"]["price"]) + "   |")
        print("| - 3. " + products["3"]["name"] + "   ugx." + str(products["3"]["price"]) + "   |")
        print("| - 4. " + products["4"]["name"] + "           ugx." + str(products["4"]["price"]) + "   |")
        print("| - 5. " + products["5"]["name"] + "      ugx." + str(products["5"]["price"]) + "   |")
        print("| - 6. " + products["6"]["name"] + "              ugx." + str(products["6"]["price"]) + "   |")
        print("|------------------------------------------|")
        print("|  opt Drink Item                 Price    |")
        print("| - 1. " + drink_products["1"]["name"] + "                     ugx." + str(
            drink_products["1"]["price"]) + "  |")
        print("| - 2. " + drink_products["2"]["name"] + "                     ugx." + str(
            drink_products["2"]["price"]) + "  |")
        print("| - 3. " + drink_products["3"]["name"] + "                 ugx." + str(
            drink_products["3"]["price"]) + "  |")
        print("| - 4. " + drink_products["4"]["name"] + "                   ugx." + str(
            drink_products["4"]["price"]) + "  |")
        print("| - 5. " + drink_products["5"]["name"] + "                  ugx." + str(
            drink_products["5"]["price"]) + "  |")
        print("| - 6. " + drink_products["6"]["name"] + "               ugx." + str(
            drink_products["6"]["price"]) + "  |")
        print("|------------------------------------------|")
        print("|------------------------------------------|")

        # Waiter welcoming Customers
        # Customer enters a numeric value end of the question referencing the food item on the menu
        # choose_food gets value from console
        choose_food = input("Welcome to Fooders.. What can I get you...")

        # star1 variable gets food item name basing on the choose_food variable
        star1 = products[choose_food]["name"]

        # Food name got from star1 variable is referenced in quantity_1 input request
        # Customer enters the amount of food they want to eat, and it gets stored in quantity_1
        quantity_1 = input(f"How many plates of {star1}: ")

        # Customer enters a numeric value end of the question referencing the drink item on the menu
        # choose_drink gets value from console
        choose_drink = input("Choose Drink option:")

        # star2 variable gets food item name basing on the choose_drink variable
        star2 = drink_products[choose_drink]["name"]

        # Drink name got from star2 variable is referenced in quantity_2 input request
        # Customer enters the number of drinks they want to drink, and it gets stored in quantity_2
        quantity_2 = input(f"How many bottles of {star2}: ")

        """
        waiter() method takes in the choose_food, choose_drink, quantity_1 and quantity_2 as arguments
        """
        waiter(choose_food, choose_drink, quantity_1, quantity_2)

    # except prevents program from crushing in case of invalid input
    except:
        print("Invalid input")
        print("")


# waiter() function declaration
def waiter(f_name, d_name, f_qty, d_qty):
    # Variable initialization
    grand_total = 0
    food_qty = 0
    drinks_qty = 0

    """
    Getting names and prices of food items and drinks from Dictionary keys 
    which are being passed from as arguments in the this function from the display_menu() function
    """
    food_n = products[f_name].get("name")
    drink_n = drink_products[d_name].get("name")
    food_un = products[f_name].get("price")
    drink_un = drink_products[d_name].get("price")

    # Getting total cost of @food as food_qty
    # We're getting quantity the user inputted as passed through as f_qty or d_qty respectively
    # Then multiplying it to product price got from the respective dictionary through the keys respectively
    food_qty = products[f_name].get("price") * int(f_qty)
    drinks_qty = drink_products[d_name].get("price") * int(d_qty)

    # grand_total is iterated by food_qty and drinks_qty respectively
    grand_total += food_qty
    grand_total += drinks_qty

    # grand_total is then stored in Total variable for the final time
    Total = grand_total

    # Displaying exaggerated Receipt UI design
    print("")
    print("|-------------------Receipt--------------------------|")
    print("| Item Name                  Qty  Rate     Amount |")
    print(f"| {food_n} " + f"           {f_qty} " + f"  {food_un} " + f" {food_qty}  |")
    print(f"| {drink_n} " + f"              {d_qty}" + f"  {drink_un} " + f" {drinks_qty}  |")
    print("|----------------------------------------------------|")
    print(f"|      Total Bill: {Total}")
    print("|----------------------------------------------------|")
    # End of exaggerated Receipt UI design


# Calling the display_menu() function to start running the programme
display_menu()
