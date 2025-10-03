"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for items in items_to_add:
        if items not in current_cart:
            current_cart[items] = 1
        else:
            current_cart[items] += 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    notes_dict = dict.fromkeys(notes, (1))
    return notes_dict
    
def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas |= recipe_updates
    return ideas
        
def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item in cart.keys():
        quantity = cart[item]
        aisle, refrigerate = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle, refrigerate]
    sorted_fulfillment_cart = dict(sorted(fulfillment_cart.items(), reverse=True))
    return sorted_fulfillment_cart

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    new_store_inv = {}
    for item in store_inventory.keys():
        ordered_quantity = fulfillment_cart.get(item, [0])[0]
        quantity = store_inventory[item][0] - ordered_quantity
        if quantity == 0:
            quantity = "Out of Stock"
        aisle, refrigerate = store_inventory[item][1:]
        new_store_inv[item] = [quantity, aisle, refrigerate]
    return new_store_inv
        
