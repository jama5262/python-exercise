import unittest
from unittest.mock import patch
import appQ4

class TestShip(unittest.TestCase):

    @patch('appQ4.getInput', return_value='Y')
    def test_retryGame(self, input):
        self.assertEqual(appQ4.askAgain(), True)

    @patch('appQ4.getInput', return_value='N')
    def test_quitGame(self, input):
        self.assertEqual(appQ4.askAgain(), False)


if __name__ == '__main__':
    unittest.main()
