# Replace your while loop with this automated loop
items_to_add = [("apple", 1.50), ("milk", 3.00), ("done")]
budget = 50.0
shopping_list = []

print("Welcome to your Automated Python Grocery Assistant!")

for item_info in items_to_add:
    if item_info == 'done':
        break
        
    item, price = item_info
    print(f"\nProcessing item: {item} (${price})")

    if price <= budget:
        shopping_list.append(item)
        budget -= price
        print(f"Added {item}! Remaining budget: ${budget:.2f}")
    else:
        print(f"Sorry, {item} is too expensive! You only have ${budget:.2f} left.")

print("\n--- Final Summary ---")
print(f"Items bought: {shopping_list}")
print(f"Money remaining: ${budget:.2f}")

