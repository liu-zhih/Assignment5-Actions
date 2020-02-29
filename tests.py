import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_get_area(self):
        expected = 0
        self.assertEqual(expected, task.get_area(0))
        expected = 64
        self.assertEqual(expected, task.get_area(4.5))
        expected = 314
        self.assertEqual(expected, task.get_area(10))


if __name__ == '__main__':
    unittest.main()
