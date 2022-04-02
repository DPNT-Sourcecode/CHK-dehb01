from .helper_functions import calculate_A_discount

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus : str) -> int:
    if type(skus) != str: # input must be a string
        return -1

    valid_skus = ['A', 'B', 'C', 'D', 'E']
    sku_list = list(skus)
    price_list = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }
    A_count = 0
    B_count = 0
    E_count = 0
    B_discount = 15 # offer is 2 for 45, a saving of 15 pounds
    checkout_total = 0
    for sku in sku_list:
        if sku not in valid_skus:
            return -1
        if sku == 'A':
            A_count += 1
        if sku == 'B':
            B_count += 1
        if sku == 'E': 
            E_count += 1
        checkout_total += price_list[sku]
    
    A_total_discount = calculate_A_discount(A_count)
    E_discounts_to_apply = int(E_count / 2)

    B_count_for_discounts = B_count - E_discounts_to_apply # effectively remove the Bs from basket before applying th discount for B
    B_discounts_to_apply = int(B_count_for_discounts / 2)

    # Apply A discounts
    checkout_total = checkout_total - A_total_discount

    # Apply B discounts
    checkout_total = checkout_total - (B_discounts_to_apply * B_discount)

    # Apply E discounts
    if B_count > E_discounts_to_apply:
        checkout_total = checkout_total - (E_discounts_to_apply * 30) 
    if E_discounts_to_apply >= B_count:
        checkout_total = checkout_total - (B_count * 30) 
    return checkout_total
