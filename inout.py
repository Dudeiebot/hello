menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# these is a typical output and input restaurant kind of goods and services.
def get_user_input():
    while True:
        try:
            user_input = input("Item: ").title()
        except EOFError:              #helps to end the session with ctrl d
            print("Order ended.")
            return None
        
        if user_input in menu:
            return user_input
        else:
            print(f"{user_input} not found in menu.")
'''
def validate_more_items():
    while True:      if you want to make it more user efficient.
        more_items = input("Add more items? (y/n)").lower()
        if more_items in ('y', 'n'):
            return more_items == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
'''

def calculate_total_cost(selected_items):
    total_cost = sum(menu[item] for item in selected_items)
    return total_cost

def main():
    selected_items = []
    while True:
        user_input = get_user_input()
        if user_input is None:
            break
        selected_items.append(user_input)
        #if not validate_more_items():
        #    break
    
    if len(selected_items) == 0:
        print("No items selected.")
    else:
        total_cost = calculate_total_cost(selected_items)
        print(f"Selected items: {', '.join(selected_items)}")
        print(f"Total cost: {total_cost}")

if __name__ == '__main__':
    main()
