def display_items(items):
    if len(items) == 0:
        print("The list is empty.")
        return

    item_num = 1
    for item in items:
        print(f"{item_num}. {item}")
        item_num += 1


def main_loop():
    # This, [], is an empty list. We start with that.
    items = []

    user_input = ""

    while user_input != "q":
        display_items(items)

        user_input = input("Add, remove or quit (a/r/q)? ")

        if user_input == "a":
            new_item = input("What should I add? ")
            items.append(new_item)

        if user_input == "r":
            if len(items) == 0:
                print("There is nothing to remove.")
                continue

            index = select_item(items, "Remove which item? ")
            del items[index]


def select_item(items, prompt):
    # num_items == how many items are in the list
    num_items = len(items)

    # Now we want to give the user several tries
    # to make a valid choice. Therefore, we need
    # a loop.
    while True:
        item_num = input(prompt)
        item_num = int(item_num)

        # We check if the user's number is valid.
        if item_num < 1 or item_num > num_items:
            # The user's number is not valid.
            print(f"Valid numbers are 1 to {num_items}")
        else:
            # The user's number is valid, so let's return it.
            return item_num - 1


main_loop()
