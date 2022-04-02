from .helper_functions import calculate_A_discount

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus : str) -> int:
    if type(skus) != str: # input must be a string
        return -1

    valid_skus = ['A', 'B', 'C', 'D', 'E', 'F']
    sku_list = list(skus)
    price_list = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
    }

    A_count = 0
    B_count = 0
    E_count = 0
    F_count = 0

    B_discount = 15 # offer is 2 for 45, a saving of 15 pounds
    F_discount = 10 # offer is effectively 3 for 20, a saving of 10 pounds
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
        if sku == 'F':
            F_count += 1
        checkout_total += price_list[sku]
    
    A_total_discount = calculate_A_discount(A_count)
    E_discounts_to_apply = int(E_count / 2)
    F_discounts_to_apply = int(F_count / 3)

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

    # Apply F discounts
    checkout_total = checkout_total - (F_discounts_to_apply * F_discount)

    return checkout_total
