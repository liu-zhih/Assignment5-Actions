import unittest
import task
from datetime import date


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    # def test_get_area(self):
    #     expected = 0
    #     self.assertEqual(expected, task.get_area(0))
    #     expected = 64
    #     self.assertEqual(expected, task.get_area(4.5))
    #     expected = 314
    #     self.assertEqual(expected, task.get_area(10))

    # def test_get_first_and_last_ele(self):
    #     test_list_1 = [1, 2, 3]
    #     expected = task.get_first_and_last_ele(test_list_1)
    #     self.assertEqual(expected[0], 1)
    #     self.assertEqual(expected[1], 3)

    #     test_list_2 = ['a', 'b', 'c', 'd']
    #     expected = task.get_first_and_last_ele(test_list_2)
    #     self.assertEqual(expected[0], 'a')
    #     self.assertEqual(expected[1], 'd')

    def test_get_days_bet_dates(self):
        expected = task.get_days_bet_dates(date(2020, 2, 20), date(2020, 2, 28))
        self.assertEqual(abs(expected.days), 8)
        expected = task.get_days_bet_dates(date(2020, 2, 28), date(2020, 2, 1))
        self.assertEqual(abs(expected.days), 27)
        expected = task.get_days_bet_dates(date(2020, 1, 1), date(2020, 2, 1))
        self.assertEqual(abs(expected.days), 31)


if __name__ == '__main__':
    unittest.main()
