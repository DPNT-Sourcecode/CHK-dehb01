from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        skus = ["X",'KK', "K", "S", "T", "X", "XXX", "SSSZ", "ZZZS"]
        solutions = [17, 120, 70, 20 ,20, 17, 45, 65, 65]
        for sku, solution in zip(skus, solutions):
            assert checkout_solution.checkout(sku) == solution