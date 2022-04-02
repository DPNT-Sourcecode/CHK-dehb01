def calculate_discount(counts: dict, sku: str, offer_list: list, price_list: dict) -> int:
    """returns the amount to discount from total because of the multi offer on an item"""
    price = price_list[sku]
    count = counts[sku]

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



