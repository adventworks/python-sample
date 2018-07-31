from unittest import TestCase

from application.main import sum_two


class TestSum(TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_two(1, 1), 2)

    def test_negative_numbers(self):
        self.assertEqual(sum_two(-1, -1), -2)
