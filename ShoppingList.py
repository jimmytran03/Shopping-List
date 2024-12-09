def create_shopping_list():
    shopping_list = []
    print("Enter items for your shopping list. Type 'done' to finish.")

    while True:
        item = input("Enter an item (or 'done' to finish): ")
        if item == 'done':
            break
        shopping_list.append(item)

    return shopping_list


def check_shopping_list(shopping_list):
    if not any(shopping_list):
        print("Your shopping list is empty. Add some items before going shopping!")
    else:
        print("Your shopping list:")
        for item in shopping_list:
            print(f"- {item}")


# Main program
shopping_list = create_shopping_list()
check_shopping_list(shopping_list)
