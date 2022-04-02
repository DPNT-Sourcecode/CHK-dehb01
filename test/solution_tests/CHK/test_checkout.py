from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        skus = ['KK', "K", "S", "T", "X", "XXX"]
        solutions = [120, 70, 20 ,20, 17, 45]
        for sku, solution in zip(skus, solutions):
            assert checkout_solution.checkout(sku) == solution