from lib.solutions.HLO.hello_solution import hello
from solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        names = ['Jeff', 'Bob', 'Sam', 'Jerry']
        for name in names:
            assert hello_solution.hello(name) == f"Hello, {name}!"