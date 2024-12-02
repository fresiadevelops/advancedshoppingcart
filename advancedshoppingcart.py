class ItemToPurchase:
    """
    Class representing shopping cart items.
    Includes name, price, quantity, and description attributes.
    """
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        # Item initialization with default or provided values
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_cost(self):
        """
        Prints the item's cost as:
        <name> <quantity> @ $<price> = $<total>
        """
        total_cost = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${total_cost:.2f}")
        return total_cost

    def print_item_description(self):
        """
        Prints the item's description as:
        <name>: <description>
        """
        print(f"{self.name}: {self.description}")


class ShoppingCart:
    """
    Class representing a shopping cart.
    Manages a collection of ItemToPurchase objects and provides methods to
    add, remove, modify items, and calculate totals.
    """
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Shopping cart initiation with default or provided customer name and date
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # List to store ItemToPurchase objects

    def add_item(self, item):
        """
        Adds an item (ItemToPurchase object) to the cart.
        """
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """
        Removes a shopping cart item by name.
        If the item is not found, prints a message.
        """
        found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        """
        Modifies a cart item's attributes (description, price, quantity) in the cart.
        If the item is not found, prints a message.
        """
        found = False
        for item in self.cart_items:
            if item.name == modified_item.name:
                found = True
                # Update attributes only if the new value is not default
                if modified_item.description != "none":
                    item.description = modified_item.description
                if modified_item.price != 0.0:
                    item.price = modified_item.price
                if modified_item.quantity != 0:
                    item.quantity = modified_item.quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """
        Returns the total quantity of all items in the cart.
        """
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        """
        Returns the total cost of all items in the cart.
        """
        return sum(item.price * item.quantity for item in self.cart_items)

    def print_total(self):
        """
        Outputs the total cost of all items in the cart.
        If the cart is empty, prints a message.
        """
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        """
        Outputs the descriptions of all items in the cart.
        """
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    """
    Displays interaction menu for shopping cart.
    Allows the user to add, remove, modify items, view descriptions, or quit.
    """
    while True:
        # Display the menu
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'a':
            # Add an item to the cart
            print("ADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        elif choice == 'r':
            # Remove an item from the cart
            print("REMOVE ITEM FROM CART")
            name = input("Enter the name of the item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            # Modify an item's attributes
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            modified_item = ItemToPurchase(name=name, quantity=quantity)
            cart.modify_item(modified_item)
        elif choice == 'i':
            # Output item descriptions
            cart.print_descriptions()
        elif choice == 'o':
            # Output shopping cart total
            cart.print_total()
        elif choice == 'q':
            # Quit the menu
            break
        else:
            # Invalid input
            print("Invalid option. Try again.")


# Main program
if __name__ == "__main__":
    # Shopping cart initialization with user-provided name and date
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()
    shopping_cart = ShoppingCart(customer_name, current_date)

    # Display the cart's initial details
    print(f"\nCustomer name: {shopping_cart.customer_name}")
    print(f"Today's date: {shopping_cart.current_date}")

    # Call the menu to interact with the shopping cart
    print_menu(shopping_cart)
