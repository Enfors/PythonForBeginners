# Let's call our list 'items', since calling it
# 'list' is a bad idea.

items = []

user_input = ""

while user_input != "q":

    if len(items) == 0:
        print("The list is empty.")
    else:
        item_num = 0

        for item in items:
            print(f"{item_num}: {item}")
            item_num += 1

    # Just print an empty line
    print()
    user_input = input("Add, delete or quit (a/d/q)? ")

    if user_input == "a":
        new_item = input("What should I add? ")
        items.append(new_item)

    if user_input == "d":
        if len(items) == 0:
            print("There is nothing to delete.")
        else:
            delete_index = input("Enter number of item: ")
            delete_index = int(delete_index)
            del items[delete_index]

print("Goodbye!")
