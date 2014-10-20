import unittest
from example import Square

class testSquare(unittest.TestCase):
    def setUp(self):
        self.square_object = Square()

    def testWrongSquare(self):
        # Test with argument = 2
        arg = 2
        result = self.square_object.wrong_square(arg)
        self.assertEqual(result, 4)

        # Test again with argument = 3
        arg = 3
        result = self.square_object.wrong_square(arg)
        self.assertEqual(result, 9)

    def testRightSquare(self):
        # Test with argument = 2
        arg = 2
        result = self.square_object.right_square(arg)
        self.assertEqual(result, 4)

        # Test again with argument = 3
        arg = 3
        result = self.square_object.right_square(arg)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()

