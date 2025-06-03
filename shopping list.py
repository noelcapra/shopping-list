
def want_continue1():
    if input("Do you want to continue? (yes/no)").lower() == "yes":
        return True
    else:
        return False


def shopping_list():
    shopping_list = []

    while True:

        print("1. Add item")
        print("2. Remove item")
        print("3. Display items")
        print("4. Exit")

        answer = input("What would you like to do? Please input 1, 2, 3, or 4: ")
        if answer == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
        elif answer == "2":
            item = input("Enter item to remove: ")
            shopping_list.remove(item)
        elif answer == "3":
            for i in shopping_list:
                print(i)
        elif answer == "4":
            break

        if not want_continue1():
            print("Thank you for shopping list!")
            break

shopping_list()
