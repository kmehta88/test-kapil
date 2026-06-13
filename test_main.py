import io
import unittest
from unittest.mock import patch

from add_two_numbers import add_numbers
from main import main
from multiply_two_numbers import multiply_numbers


class CalculatorTests(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1090, 200), 1290)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(1090, 200), 218000)

    def test_main_prints_sum_and_product(self):
        with patch("builtins.input", side_effect=["1090", "200"]):
            with patch("sys.stdout", new_callable=io.StringIO) as output:
                main()

        self.assertEqual(output.getvalue(), "Sum: 1290.0\nProduct: 218000.0\n")


if __name__ == "__main__":
    unittest.main()
