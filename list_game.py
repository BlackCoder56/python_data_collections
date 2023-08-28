from _ast import Continue

food_menu = ["Rice", "Fish"]


def options(opt):
    if opt == "1":
        print("\n")
        print("|-----------Menu------------|")
        for i in range(len(food_menu)):
            print("| " + str(i + 1) + ". " + food_menu[i])
        print("|--------------------------|")

        # option = input("Enter option: ")

    elif opt == "2":
        while True:
            new_food = input("Enter New Food to menu: ")
            food_menu.append(new_food)
            option = input("Do you want to display menu?(yes or no): ")
            if option == "yes":
                print("\n")
                print("|-----------Menu------------|")
                for i in range(len(food_menu)):
                    print("|" + str(+i + 1) + ". " + food_menu[i])
                print("|----------------------------|")
                print("")
                option = input("Do you want to add new Food to menu?(yes or no): ")
                if option == "yes":
                    continue
                elif option == "no":
                    break
                else:
                    pass

            elif option == "no":
                print("ended")
                print("\n")
            else:
                pass

1
def container():
    print("")
    print("|^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|1. Get menu            |")
    print("|2. Add food to menu    |")
    print("|3. Exit                |")
    print("|_______________________|")
    option = input("Enter option(1 or 2): ")
    options(option)


def prints():
    print("///////////////////////")
    print("1. Get menu")
    print("2. Add food to menu")
    print("3. Exit")
    print("///////////////////////")


while True:
    container()
