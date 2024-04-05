import unittest
import algorithms

palindromos = [
    "radar",
    "reconocer",
    "anilina",
    "neuquen",
    "arenera",
    "sometemos",
    "salas",
    "amor a roma",
    "anita lava la tina",
    "la ruta natural"
]



class AlgorithmsTests(unittest.TestCase):
    def test_direct_comparation(self):
        for i in palindromos:
            result = algorithms.direct_comparation(i)
            self.assertTrue(result, f"la palabra '{i}' deberia ser una palindromo")
    def test_inverse_comparation(self):
        for i in palindromos:
            result = algorithms.inverse_comparation(i)
            self.assertTrue(result,f"la palabra '{i}' deberia ser una palindromo")
    def test_deque_comparation(self):
        for i in palindromos:
            result = algorithms.deque_comparation(i)
            self.assertTrue(result, f"la palabra '{i}' deberia ser una palindromo")


if __name__ == "__main__":
   unittest.main()
