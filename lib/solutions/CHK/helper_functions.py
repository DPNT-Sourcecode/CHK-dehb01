def calculate_A_discount(A_count: int) -> int:
    """returns the amount to discount from total because of the multi offer on item A"""
    buy_5_discounts = int(A_count / 5)
    buy_5_discount = buy_5_discounts * 50
    remainder_of_A = A_count % 5
    buy_3_discounts = int(remainder_of_A / 3)
    buy_3_discount = buy_3_discounts * 20
    return buy_5_discount + buy_3_discount
