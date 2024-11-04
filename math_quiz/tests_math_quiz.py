import unittest
from math_quiz import test_generate_random_integer, select_operator, calculate_answer


class TestMathGame(unittest.TestCase):

    def test_test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = test_generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_operator(self):
        """Test that select_operator returns one of the valid operators."""
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Run multiple times to ensure all operators can be selected
            result = select_operator()
            self.assertIn(result, valid_operators)


    def test_calculate_answer(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 3, '-', 2),  # 5 - 3 = 2
                (4, 3, '*', 12),  # 4 * 3 = 12
                (10, 5, '+', 15),  # 10 + 5 = 15
                (7, 2, '-', 5),  # 7 - 2 = 5
                (6, 2, '*', 12),  # 6 * 2 = 12
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                _, answer = calculate_answer(num1, num2, operator)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
