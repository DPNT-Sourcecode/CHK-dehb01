from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        skus = ['A', 'B', 'C', 'D', 'AAA', 'BB', 1, 'ABC12', 'ACAAZ', 'AAABBAAA', 'BBBB']
        solutions = [50, 30, 20, 15, 130, 45, -1, -1, -1, 305, 90]
        for sku, solution in zip(skus, solutions):
            assert checkout_solution.checkout(sku) == solution