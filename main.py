import json

class Inventory:
    def _init_(self):
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
        """Update an item's quantity or price"""
        for item in self.items:
            if item["name"] == name:
                if quantity:
                    item["quantity"] = quantity
                if price:
                    item["price"] = price
                return f"Item '{name}' updated."
        return f"Item '{name}' not found."
    
    def filter_items(self, price_limit=None, quantity_limit=None):
        """Filter items by price and quantity"""
        filtered_items = self.items
        if price_limit:
            filtered_items = [item for item in filtered_items if item["price"] <= price_limit]
        if quantity_limit:
            filtered_items = [item for item in filtered_items if item["quantity"] >= quantity_limit]
        return json.dumps(filtered_items, indent=4)

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
    inventory.add_item("Headphones", 50, 100)
    inventory.add_item("Tablet", 5, 250)
    print(inventory.view_items())
    print(inventory.filter_items(price_limit=1000, quantity_limit=10))  # Filtering items



mplement search and filter functionality for inventory items
Description: Added a filter_items method that allows filtering inventory items by price and quantity. This method accepts price_limit and quantity_limit parameters to filter the items accordingly.
