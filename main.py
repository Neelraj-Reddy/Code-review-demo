import json

class Inventory:
    def _init_(self):
        self.items = []
    
    def add_item(self, name, quantity, price):
        """Add a new item to the inventory"""
        item = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "discount": 0  # Added discount field
        }
        self.items.append(item)
        return f"Item '{name}' added successfully."
    
    def view_items(self):
        """View all items in the inventory"""
        if not self.items:
            return "No items in inventory."
        return json.dumps(self.items, indent=4)

    def update_item(self, name, quantity=None, price=None, discount=None):
        """Update an item's quantity, price, or discount"""
        for item in self.items:
            if item["name"] == name:
                if quantity:
                    item["quantity"] = quantity
                if price:
                    item["price"] = price
                if discount is not None:
                    item["discount"] = discount
                return f"Item '{name}' updated."
        return f"Item '{name}' not found."

    def apply_discount(self, name, discount_percentage):
        """Apply a discount to an item"""
        for item in self.items:
            if item["name"] == name:
                item["discount"] = discount_percentage
                item["price"] *= (1 - discount_percentage / 100)  # Apply discount to price
                return f"Discount of {discount_percentage}% applied to '{name}'."
        return f"Item '{name}' not found."

    def delete_item(self, name):
        """Delete an item from the inventory"""
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return f"Item '{name}' deleted successfully."
        return f"Item '{name}' not found."

if _name_ == "_main_":
    inventory = Inventory()
    inventory.add_item("Laptop", 10, 1200)
    inventory.add_item("Phone", 30, 800)
    print(inventory.view_items())
    print(inventory.apply_discount("Laptop", 10))  # Applying 10% discount
    print(inventory.view_items())
