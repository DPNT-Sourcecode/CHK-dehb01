from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        test_list = [(1,2), (3,4), (5,6), (7,8)]
        solutions = [3, 7, 11, 15]
        for test, solution in zip(test_list, solutions):
            assert sum_solution.compute(test[0], test[1]) == solution
