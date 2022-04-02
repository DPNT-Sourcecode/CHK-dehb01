PRICE_LIST = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }

OFFER_DICT = {
    "A": [(3,130), (5,200)],
    "B": [(2, 45)],
    "F": [(3, 20)],
    "H": [(5,45), (10,80)],
    "K": [(2,150)],
    "P": [(5,200)],
    "Q": [(3, 80)],
    "U": [(4, 120)],
    "V": [(2,90), (3,130)],
}


BUY_MULTI_GET_FREE_OFFERS = {
    "E": (2, 'B'),
    "N": (3, 'M'),
    "R": (3, 'Q')
}

def calculate_A_discount(A_count: int) -> int:
    """returns the amount to discount from total because of the multi offer on item A"""
    buy_5_discounts = int(A_count / 5)
    buy_5_discount = buy_5_discounts * 50
    remainder_of_A = A_count % 5
    buy_3_discounts = int(remainder_of_A / 3)
    buy_3_discount = buy_3_discounts * 20
    return buy_5_discount + buy_3_discount



