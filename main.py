import json

class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, quantity, price):
        """Add a new item to the inventory"""
        item = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        self.items.append(item)
        return f"Item '{name}' added successfully."
    
    def view_items(self):
        """View all items in the inventory"""
        if not self.items:
            return "No items in inventory."
        return json.dumps(self.items, indent=4)

    def update_item(self, name, quantity=None, price=None):
        """Update an item's quantity or price in inventory"""
        for item in self.items:
            if item["name"] == name:
                if quantity:
                    item["quantity"] = quantity
                if price:
                    item["price"] = price
                return f"Item '{name}' updated."
        return f"Item '{name}' not found."

    def delete_item(self, name):
        """Delete an item from the inventory"""
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return f"Item '{name}' deleted successfully."
        return f"Item '{name}' not found."

if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Laptop", 10, 1200)
    inventory.add_item("Phone", 30, 800)
    print(inventory.view_items())
