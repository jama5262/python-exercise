import unittest
from appQ2 import Ship

class TestShip(unittest.TestCase):

    def test_ship(self):
        self.assertEqual(Ship(15, 10).is_worth_it(), False)
        self.assertEqual(Ship(100, 10).is_worth_it(), True)
        self.assertEqual(Ship(1, 1).is_worth_it(), False)
        self.assertEqual(Ship(0, 1).is_worth_it(), False)

if __name__ == '__main__':
    unittest.main()
