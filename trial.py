shopping_list = []
budget = 50.0

print("Welcome to your Python Grocery Assistant!")

while True:
    item = input("\nEnter item to add (or type 'done'): ")
    
    if item == 'done':
        break
        
    try:
        price = float(input("Enter price of the item: "))
    except ValueError:
        print("Please enter a valid number for the price.")
        continue

    if price <= budget:
        shopping_list.append(item)
        budget -= price
        print(f"Added {item}! Remaining budget: ${budget:.2f}")
    else:
        print(f"Sorry, {item} is too expensive! You only have ${budget:.2f} left.")

print("\n--- Final Summary ---")
print(f"Items bought: {shopping_list}")
print(f"Money remaining: ${budget:.2f}")
