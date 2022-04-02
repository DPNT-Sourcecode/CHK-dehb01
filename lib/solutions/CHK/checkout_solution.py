from .helper_functions import calculate_discount
from .dicts import PRICE_LIST, OFFER_DICT, BUY_MULTI_GET_FREE_OFFERS

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus : str) -> int:
    if type(skus) != str: # input must be a string
        return -1

    valid_skus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    counts = {}
    # create a dict of zero counts for each sku
    for sku in valid_skus:
        counts[sku] = 0
    sku_list = list(skus)
    price_list = PRICE_LIST.copy()
    offer_dict = OFFER_DICT.copy()
    buy_multi_get_free_offers = BUY_MULTI_GET_FREE_OFFERS.copy()

    # count the totals of each sku
    for sku in sku_list:
        if sku not in valid_skus:
            return -1
        counts[sku] += 1
    
    # remove items from the basket that represent multi buy get one free
    for sku, offer in buy_multi_get_free_offers.items():
        sku_getting_for_free = offer[1]
        free_count = int(counts[sku] / offer[0])
        if counts[sku_getting_for_free] > free_count: # dont want to go into a negative count
            counts[sku_getting_for_free] -= free_count
        else: 
            counts[sku_getting_for_free] = 0
    
    # add up the checkout total
    checkout_total = 0
    for sku, count in counts.items():
        checkout_total += price_list[sku] * count
    
    # add up all the discounts
    total_discount = 0
    for sku, offer_list in offer_dict.items():
        total_discount += cal

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

