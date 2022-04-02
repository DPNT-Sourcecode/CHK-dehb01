from .helper_functions import calculate_discount, calculate_STXYZ_discount
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

    sku_list = list(skus) # convert string to a list of each sku
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
        total_discount += calculate_discount(counts, sku, offer_list, price_list)

    total_discount += calculate_STXYZ_discount(counts, price_list)

    return checkout_total - total_discount