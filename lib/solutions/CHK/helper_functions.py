def calculate_discount(counts: dict, sku: str, offer_list: list, price_list: dict) -> int:
    """returns the amount to discount from total because of the multi offer on an item"""
    price = price_list[sku]
    count = counts[sku]


    # offer[0] represents how many need to be bought, offer[1] is the price
    if len(offer_list) == 2: # there is a large and small multi offer
        large_offer = offer_list[1]
        small_offer = offer_list[0]
        large_count = int(count / large_offer[0])
        large_discount = large_count * ((price * large_offer[0]) - large_offer[1])
        remainder = count % large_offer[0]
        small_count = int(remainder / small_offer[0])
        small_discount = small_count * ((price * small_offer[0]) - small_offer[1])
        return large_discount + small_discount
    
    if len(offer_list) == 1:
        offer = offer_list[0]
        discounts = int(count/ offer[0])
        total = discounts * ((price * offer[0]) - offer[1])
        return total

def calculate_STXYZ_discount(counts: dict, price_list: dict) -> int:
    sku_list = ['S', 'T', 'X', 'Y', 'Z']
    combined_count = 0
    total_cost_without_discount = 0
    for sku in sku_list:
        count = counts[sku]
        combined_count += count
        total_cost_without_discount += price_list[sku] * count
    discounts_to_make = int(combined_count / 3)
    return total_cost_without_discount - (45 * discounts_to_make)




