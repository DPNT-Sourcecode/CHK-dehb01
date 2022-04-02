from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        skus = ['A', 'B', 'C', 'D', 'AAA', 'BB', 1, 'ABC12', 'AAABBAAA', 'BBBB', 'BBEE', "EE", "EEEEBB", "BEBEEE", "FF", "FFF", "FFFFFF", "VVV", "PPPPP", 'KK']
        solutions = [50, 30, 20, 15, 130, 45, -1, -1, 295, 90, 110, 80, 160, 160, 20, 20, 40, 130, 200, 120]
        for sku, solution in zip(skus, solutions):
            assert checkout_solution.checkout(sku) == solution